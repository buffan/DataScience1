import re
from twython import Twython, TwythonError
from os.path import join

# Requires Authentication as of Twitter API v1.1

def read_tokens(tokens_file):
    """
    Reads API key tokens from the given file
    Inputs: tokens_file - name of tokens file. Key and value should be
                seperated by a space, with each pairing on a separate line
    Outputs: dictionary containing keys of token names with values of token 
                values
    """
    tokens = {}
    with open(tokens_file) as f:
        for line in f:
            key, value = line.split()
            tokens[key] = value
    return tokens


def search_and_write(user):
    """
    Queries twitter for given user's tweets. Records tweet, retweets, and favorites
    Inputs: user - User for which twython should query twitter
    """
    tokens = read_tokens("apiKeys.txt")
    twitter = Twython(**tokens)
    
    try:
        search_results = twitter.get_user_timeline(screen_name=user, include_rts=False, exclude_replies=True, count=200)
    except TwythonError as e:
      print(e)

    save_file = user + ".txt"
    directory = "tweets"
    save_file = join(directory, save_file)
    print(save_file)
    with open(save_file, 'w') as f:
        for tweet in search_results:
            # Tweets stored in file by newlines
            if '\n' not in tweet['text']:
                text = tweet['text']
                cleaned_text = ' '.join([word for word in text.split() 
                    if 'https://t.co' not in word])
                f.write(cleaned_text.encode('utf-8') + '\n')
                f.write('{} {}\n'.format(tweet['retweet_count'], tweet['favorite_count']))

def main():
    user = "HillaryClinton"
    search_and_write(user)
    user = "realDonaldTrump"
    search_and_write(user)



main()
