from twython import Twython, TwythonError
from os.path import join

# Requires Authentication as of Twitter API v1.1

def read_tokens(tokens_file):
    tokens = {}
    with open(tokens_file) as f:
        for line in f:
            key, value = line.split()
            tokens[key] = value
    return tokens


def search_and_write(twitter, query_text):
    try:
        search_results = twitter.search(q=query_text, count=100, result_type='mixed')
    except TwythonError as e:
      print(e)

    save_file = query_text[1:] + ".txt"
    directory = "tweets"
    save_file = join(directory, save_file)
    print(save_file)
    with open(save_file, 'w') as f:
        for tweet in search_results['statuses']:
            # Filter tweets with newlines so tweets can be stored in file through newlines
            if '\n' not in tweet['text']:
                f.write(tweet['text'] + '\n')
                f.write("{} {}\n".format(tweet['retweet_count'], tweet['favorite_count']))


def main():
    tokens = read_tokens("apiKeys.txt")
    twitter = Twython(**tokens)

    query_text = "#ImWithHer"
    search_and_write(twitter, query_text)
    query_text = "#TrumpPence16"
    search_and_write(twitter, query_text)



main()
