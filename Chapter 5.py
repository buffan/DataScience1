# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:39:10 2016

@author: Andrew
"""

import numpy as np
import pandas as pd
import random



# Create series of data
data = pd.Series(np.random.randint(0, 500, 100))

num_points = len(data)
largest_value = max(data)
smallest_value = min(data)
sorted_values = sorted(data)
second_smallest = data[1]
second_largest = data[len(data)-2] # data[-2] does not work (pandas bug)

mean = data.mean() # returns float
def book_mean(x):
    return sum(x)/len(x)
    

median = data.median()
def book_median(x):
    x.sort()
    mid = len(x)//2
    if mid % 2 == 1:
        return x[mid]
    else:
        return (x[mid] + x[mid+1])/2 # alternatively can be written using mean function with hi and low

def quantile(x, p):
    p_index = int(p*len(x))
    return x[p_index]

tenthQ = data.quantile(0.1)
twentyFifthQ = data.quantile(0.25)
fiftiethQ = data.quantile() # default arg = 0.5
seventyFifthQ = data.quantile(0.75)
ninetiethQ = data.quantile(0.9)

from collections import Counter
def book_mode(x):
    counts = Counter(x)
    max_count = max(count.values())
    return [x_i for x_i, count in counts.iteritems() if count == max_count]
    
mode = data.mode() # returns dataframe of all modes

def data_range(data):
    return max(data) - min(data)

# Book
def de_mean(x):
    x_bar = mean(x) # x with a bar across the top often represents the average of x
    return [x_i - x_bar for x_i in x]
    
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum([x_i**2 for x_i in x])/(n-1)

# Pandas
variance = data.var()

# Book
from math import sqrt
def standard_dev(x):
    return sqrt(variance(x))
    
# Pandas
standard_deviation = data.std()

def interquartile_range(data):
    return data.quantile(0.75) - data.quantile(0.25)
    
IQR = interquartile_range(data)

covariant_data = np.matrix([[x for x in range(100)], [x + random.random() for x in range(100)]])
covariant_data = pd.DataFrame(covariant_data)

# Book
def book_covariance(x, y):
    n = len(x)
    return np.dot(de_mean(x), de_mean((y)))
    
# Pandas
covariance = covariant_data[1].cov(covariant_data[0])

# Book
def book_correlation(x, y):
    x_stdev = x.std()
    y_stdev = y.std()
    if x_stdev and y_stdev:
        return covariance(x, y) / x_stdev / y_stdev

# Pandas
correlation = covariant_data[1].corr(covariant_data[1])
print(correlation)
