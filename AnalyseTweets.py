# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 21:59:17 2016

@author: Andrew
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats as stats
from collections import Counter


def create_data_dict(tweets_file):
    data = {}
    retweets = []
    favorites = []
    lengths = []
    isTweet = True
    with open(tweets_file, encoding='utf8') as f:
        # lines alternate between tweet text and retweet & favorite data
        for line in f:
            if isTweet:
                lengths.append(len(line))
            else:
                rts, favs = line.split()
                retweets.append(int(rts))
                favorites.append(int(favs))
            isTweet = not isTweet
            
    data['retweets'] = np.array(retweets)
    data['favorites'] = np.array(favorites)
    data['tweet_length'] = np.array(lengths)
    
    return data



def bin_and_count(data, bin_size, title, xlabel, ylabel="Count"):
    #data_range = max(data) - min(data)
    binned = [n//bin_size * bin_size for n in data]
    hist = Counter(binned)
    
    plt.bar([x-4 for x in hist.keys()],
         hist.values(),
         8)
    plt.xlim(0, max(binned) + max(binned)*10//100)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


def plot_cor(x, y, title, xlabel, ylabel):
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    
    
    
def perform_t_test(a, b):    
    have_equal_variances = levenes_less_than_alpha(a, b)
    result_str = "using equal variances"
    if not have_equal_variances:
        result_str = "not " + result_str
    print(result_str)
    t_test_results = stats.ttest_ind(a, b, equal_var=have_equal_variances)
    return t_test_results


def levenes_less_than_alpha(a, b):
    alpha = 0.05
    result = stats.levene(a, b)
    return result.pvalue <= alpha
    

def print_measures(trump_data, clinton_data, key):
    trump_mean = np.average(trump_data[key])
    clinton_mean = np.average(clinton_data[key])
    trump_std = np.std(trump_data[key])
    clinton_std = np.std(clinton_data[key])    
    print("{} averages: Trump = {}, Clinton = {}".format(key.title(), trump_mean, clinton_mean))
    print("{} standard deviations: Trump = {}, Clinton = {}\n".format(key, trump_std, clinton_std))
    

def calc_correlation(data, key1, key2):
    a_series = pd.Series(data[key1])
    b_series = pd.Series(data[key2])
    correlation = a_series.corr(b_series)
    print("Correlation between {} and {} = {}".format(key1, key2, correlation))

def main():
    clinton_data = create_data_dict(r"tweets\HillaryClinton.txt")
    
    bin_and_count(clinton_data['retweets'], 1000, "Hillary Clinton retweets", "Binned retweets")
    bin_and_count(clinton_data['favorites'], 1000, "Hillary Clinton favorites", "Binned favorites")
    bin_and_count(clinton_data['tweet_length'], 10, "Hillary Clinton tweet length", "Binned tweet length")
    
    plot_cor(clinton_data['tweet_length'], clinton_data['retweets'], "Hillary Clinton Retweets vs Tweet length", "Tweet Length", "Retweets")
    calc_correlation(clinton_data, 'tweet_length', 'retweets')
    plot_cor(clinton_data['tweet_length'], clinton_data['favorites'], "Hillary Clinton Favorites vs Tweet length", "Tweet Length", "Favorites")
    calc_correlation(clinton_data, 'tweet_length', 'favorites')

    trump_data = create_data_dict(r"tweets\realDonaldTrump.txt")
    
    bin_and_count(trump_data['retweets'], 1000, "Donald Trump retweets", "Binned retweets")
    bin_and_count(trump_data['favorites'], 1000, "Donald Trump favorites", "Binned favorites")
    bin_and_count(trump_data['tweet_length'], 10, "Donald Trump tweet length", "Binned tweet length")
    
    plot_cor(trump_data['tweet_length'], trump_data['retweets'], "Donald Trump Retweets vs Tweet length", "Tweet Length", "Retweets")
    calc_correlation(trump_data, 'tweet_length', 'retweets')
    plot_cor(trump_data['tweet_length'], trump_data['favorites'], "Donald Trump Favorites vs Tweet length", "Tweet Length", "Favorites")
    calc_correlation(trump_data, 'tweet_length', 'favorites')
    
    
    print("Tweets considered: Trump = {}, Clinton = {}\n".format(len(clinton_data['retweets']), len(trump_data['retweets'])))
    print_measures(trump_data, clinton_data, "retweets")
    print_measures(trump_data, clinton_data, "favorites")
    print_measures(trump_data, clinton_data, "tweet_length")
    
    alpha = 0.05
    
    print("T-test on Retweets:")
    retweets_t_test = perform_t_test(clinton_data['retweets'], trump_data['retweets'])
    if retweets_t_test.pvalue > alpha:
        print("Clinton and Trump get statistically equal retweets with p = {}\n".format(retweets_t_test.pvalue))
    else:
        more_retweets = "Trump" if np.average(trump_data['retweets']) > np.average(clinton_data['retweets']) else "Clinton"
        print("{} Gets more retweets with p = {}\n".format(more_retweets, retweets_t_test.pvalue))
    
    print("T-test on Favorites:")
    favorites_t_test =perform_t_test(clinton_data['favorites'], trump_data['favorites'])
    if favorites_t_test.pvalue > alpha:
        print("Clinton and Trump get statistically equal favorites with p = {}\n".format(favorites_t_test.pvalue))
    else:
        more_favorites = "Trump" if np.average(trump_data['favorites']) > np.average(clinton_data['favorites']) else "Clinton"
        print("{} Gets more favorites with p = {}\n".format(more_favorites, favorites_t_test.pvalue))
    
    print("T-test on tweet length:")
    favorites_t_test =perform_t_test(clinton_data['tweet_length'], trump_data['tweet_length'])
    if favorites_t_test.pvalue > alpha:
        print("Clinton and Trump have statistically equal tweet lengths with p = {}".format(favorites_t_test.pvalue))
    else:
        more_favorites = "Trump" if np.average(trump_data['favorites']) > np.average(clinton_data['favorites']) else "Clinton"
        print("{} produces longer tweets with p = {}".format(more_favorites, favorites_t_test.pvalue))
    
    
    
main()