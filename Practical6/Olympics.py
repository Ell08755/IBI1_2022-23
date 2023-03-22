# This is the Olympic cost task.
# import pyplot, matplotlib and numpy
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
# list the costs and use sorted function, print
costs = [1, 8, 15, 7, 5, 14, 43, 40]
print('sorted costs list:', sorted(costs))
# create a dictionary, input all the information
Olympic_cost = {}
Olympic_cost = {'Los Angeles 1984': 1, 'Seoul 1988': 8, 'Barcelona 1992': 15, 'Atlanta 1996': 7, 'Sydney 2000': 5, 'Athens 2003': 14, 'Beijing 2008': 43, 'London 2012': 40}
# sort the dictionary (learn from https://www.cnblogs.com/harvyxu/p/8547458.html 2023/3/22) and print
Olympic_cost = dict(sorted(Olympic_cost.items(), key=lambda x: x[1]))
print('sorted Olympic cost dictionary:', Olympic_cost)
# set up colors, intervals, width, font-size of bar-chart
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple', 'pink']
ind = np.arange(len(Olympic_cost.keys()))
mpl.rcParams['font.size'] = 8
width = 0.35
plt.bar(ind, Olympic_cost.values(), width)
# set up bar-chart's label, title, x and y ticks using plt
plt.ylabel('Costs')
plt.title('The cost of hosting the Summer Olympic Games')
plt.xticks(ind, Olympic_cost.keys())
plt.xticks(rotation=20)
plt.yticks(np.arange(0, 50, 5))
plt.bar(Olympic_cost.keys(), Olympic_cost.values(), color=colors)
plt.show()

# some to-be-tested codes
# colors = np.random.rand(len(costs))
# plt.bar(Olympic_games, costs, color=colors)
