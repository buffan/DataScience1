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


def search_and_write(query_text):
    """
    Queries twitter for the given string
    Inputs: query_text - Text for which twython should query twitter
    """
    tokens = read_tokens("apiKeys.txt")
    twitter = Twython(**tokens)
    
    try:
        search_results = twitter.search(q=query_text, count=100, 
                                        result_type='mixed')
    except TwythonError as e:
      print(e)

    save_file = query_text[1:] + ".txt"
    directory = "tweets"
    save_file = join(directory, save_file)
    print(save_file)
    with open(save_file, 'w') as f:
        for tweet in search_results['statuses']:
            # Filter tweets with newlines so tweets can be stored in file 
            # through newlines
            if '\n' not in tweet['text']:
                f.write(tweet['text'].encode('utf-8') + '\n')
                f.write("{} {}\n".format(tweet['retweet_count'], 
                        tweet['favorite_count']))


def main():
    query_text = "#ImWithHer"
    search_and_write(query_text)
    query_text = "#TrumpPence16"
    search_and_write(query_text)



main()
