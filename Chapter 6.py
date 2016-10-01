# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:19:36 2016

@author: Andrew
"""


from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import random
from collections import defaultdict

def assign_kids():
    return (random.choice(['boy', 'girl']) for _ in range(2))
    
def assemble_child_count():
    d = defaultdict(int)
    d["both girls"]
    d["older girl"]
    d["either girl"]
    
    random.seed()
    for _ in range(1000):
        older, younger = assign_kids()
        d['both girls'] += int(older == 'girl' and younger == 'girl')
        d['older girl'] += int(older == 'girl')
        d['either girl'] += int(older == 'girl' or younger == 'girl')
    
    return d    
    

def plot_children(d):    
    results = {}
    results['P(both | older)'] = d['both girls']/d['older girl']
    results['P(both | either)'] = d['both girls']/d['either girl']
    labels, counts = zip(*results.items())
    
    xs = [i+0.1 for i, _ in enumerate(labels)]
    plt.bar(xs, counts)
    plt.xticks([i+0.5 for i, _ in enumerate(labels)], labels)
    plt.ylim([0, 0.6])
    plt.show()
    

def show_probability_distribution():
    x = np.linspace(stats.uniform.ppf(0.001), stats.uniform.ppf(0.999), 1000)
    plt.plot(x, stats.uniform.cdf(x))
    plt.title("Uniform cdf")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()
    
    plt.plot(x, stats.uniform.pdf(x))
    plt.title("Uniform pdf")
    plt.xlim(0, 1)
    plt.ylim(0, 1.1)
    plt.show()
    
    
def show_normal_distributions():
    mus = [0, -2, 0, 1]
    sigmas = [1, 1, 3, 0.5]
    x = np.linspace(stats.norm.ppf(0.001), stats.norm.ppf(0.999), 1000)  
    xs = [(x, mu, sigma) for mu, sigma in zip(mus, sigmas)]  
    
    for x, mu, sigma in xs:
        plt.plot(x, stats.norm.pdf(x, loc=mu, scale=sigma), label='mu={}, sigma={}'.format(mu, sigma))
    plt.legend(loc='best')
    plt.title("Normal probability distributions")
    plt.ylim(0, 0.5)
    plt.xlim(-5, 5)
    plt.show()
    
    for x, mu, sigma in xs:
        plt.plot(x, stats.norm.cdf(x, loc=mu, scale=sigma), label='mu={}, sigma={}'.format(mu, sigma))
    plt.legend(loc='best')
    plt.title("Normal cumulative distributions")
    plt.ylim(-0.01, 1.01)
    plt.xlim(-4, 4)
    plt.show()
    

def invert_normal_cdf():
    x = np.linspace(stats.norm.ppf(0.001), stats.norm.ppf(0.999), 1000)  
    
    plt.plot(x, stats.norm.cdf(x))
    zs = [-2, 0, 1]
    colors = ['#ff0000', '#0000ff', '#00ff00']
    for z, color in zip(zs, colors):
        plt.axvline(z, color=color, ls='--')
        plt.axhline(stats.norm.cdf(z), ls='--', color=color)
        print('cdf({})'.format(z), '=', stats.norm.cdf(z))
    plt.title("Inverse cumulative distribution")
        
    plt.show()
        
    
def main():
    plot_children(assemble_child_count())
    show_probability_distribution()
    show_normal_distributions()
    invert_normal_cdf()
    


main()