# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 19:08:32 2016

@author: Andrew
"""

# matplotlib
# Page 38

from matplotlib import pyplot as plt

years = [1945, 1955, 1965, 1975, 1985, 1995, 2005, 2015]
gdp = [352.2, 420.5, 775.7, 1895, 4320.1, 8654.2, 12567.8, 18492.6]

plt.plot(years, gdp, color='green', marker='^', linestyle='dashed')

plt.title("Nominal GDP")

plt.ylabel("Billions of $")
plt.show()

# Bar Charts
# Page 39

from matplotlib import pyplot as plt


movies = ['Ben Hall', 'Annie-Hurr', 'Casarojo', 'Stalin', 'East Floor Tale']
num_oscars = [6, 12, 4, 9, 11]

xs = [i+0.1 for i, _ in enumerate(movies)]
plt.bar(xs, num_oscars)

plt.ylabel('Num Academy Awards')
plt.title('My Fave Movies')

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()

# Bar Charts
# Page 40

from matplotlib import pyplot as plt
from collections import Counter

grades = [62, 20, 1, 18, 57, 30, 19, 12, 62, 31, 79, 87, 17, 46, 18]
hist = Counter(grade//10 * 10 for grade in grades)
plt.bar([x-4 for x in hist.keys()],
         hist.values(),
         8)
         
plt.axis([-5, 105, 0, 5])
plt.xticks([10*i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of exam 1 grades")
plt.show()

# Bar Charts
# Page 41

from matplotlib import pyplot as plt

mentions = [1000, 1005]
years = [2020, 2021]

plt.bar([year-0.4 for year in years], mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times someone says my name")
plt.ticklabel_format(useOffset=False)
plt.axis([2019.5, 2021.5, 999, 1006])
plt.title("Yuge increase")
plt.show()

# Corrected bar chart
# Page 42

from matplotlib import pyplot as plt

plt.bar([year-0.4 for year in years], mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times someone says my name")
plt.ticklabel_format(useOffset=False)
plt.axis([2019.5, 2021.5, 0, 1050])
plt.title("Less yuge")
plt.show()

# Line charts
# Page 43

from matplotlib import pyplot as plt

variance = [2**x for x in range(0, 9)]
bias_squared = variance[::-1]
total_error = [x+y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label = 'variance')
plt.plot(xs, bias_squared, 'r-.', label = 'bias^2')
plt.plot(xs, total_error, 'b:', label = 'total error')

plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()

# Scatterplots
# Page 44

from matplotlib import pyplot as plt
from random import randrange

friends = [randrange(60, 80) for _ in range(10)]
minutes = [randrange(120, 240) for _ in friends]
labels = [chr(ord('a')+i) for i, _ in enumerate(friends)]

plt.scatter(friends, minutes)

for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy = (friend_count, minute_count),
                 xytext = (5, -5),
                 textcoords = 'offset points'
                 )
                 
plt.title("Daily Minutes vs. Number of friends")
plt.xlabel("# of friends")
plt.ylabel("Daily minutes spent on site")
plt.show()

# Misleading axis
# Page 45

from matplotlib import pyplot as plt

test_1_grades = [randrange(80, 100) for _ in range(20)]
test_2_grades = [randrange(60, 100) for _ in test_1_grades]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes aren't compatible")
plt.xlabel("Test 1 grade")
plt.ylabel("Test 2 grade")
plt.show()

# Corrected axes
# Page 46

from matplotlib import pyplot as plt

plt.scatter(test_1_grades, test_2_grades)
plt.axis("equal")
plt.title("Matching axes")
plt.xlabel("Test 1 grade")
plt.ylabel("Test 2 grade")
plt.show()