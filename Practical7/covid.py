import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# change to .csv directory
os.chdir("C:/Users/ell/IBI1_2022-23/Practical7")
# Test unix's pwd and ls in Python
print(os.getcwd())
print(os.listdir())
# read the full_data.csv into computer, store the heads of columns
covid_data = pd.read_csv('full_data.csv')
headers = covid_data.columns.values
# print '1st to 5th' rows of the file, except the first row without data (0-4)
# print(covid_data.head(5))
# get brief information of .csv
# covid_data.info()
# print detail information of .csv
# print(covid_data.describe())
# The mean of new cases is 194.546773, and the standard deviation is 2083.395028
# Total_cases's range is 0~777798
# reach for specific values in .csv, iloc means 'Index to LOCate'
# print(covid_data.iloc[0,0])
# print(covid_data.iloc[2,0:5]) # print row2 col0~5, but vertically
# print(covid_data.iloc[0:2,:]) # print full row0 and row1, horizontally, why here no row 2
# print(covid_data.iloc[0:10:2,0:5]) # print row0,2,4,6,8 col0-5, I think it is [0,10) with interval 2
print(covid_data.iloc[0:1000:100, 1]) # 2nd col from every 100th row from the first 1000 （0-999） rows(inclusive)
# 2 ways to show first three rows' first, second and fourth col
# normal way
# print(covid_data.iloc[0:3,[0,1,3]])
# boolean way
# my_columns = [True, True, False, True, False, False] # set-up answer slots for "Do you want to see this row?"
# shorter or longer -> error
# print(covid_data.iloc[0:3,my_columns]) # row0,1,2 [0,3)
# LOC uses column names
# print(covid_data.loc[2:4,"date"]) # [2,4] row2,3,4 inclusive way why???
# print(covid_data.loc[0:81, "total_cases"]) # Afghanistan
# another way to show
Aftc = pd.DataFrame(columns=headers)
for i in range(len(covid_data)):
    if covid_data.loc[i, 'location'] == 'Afghanistan':
        Aftc.loc[len(Aftc)] = covid_data.loc[i, :]
        # add new data into a new line in the frame, effective cuz dataframe starts from 0
columns_1 = [False, False, False, False, True, False]
print(Aftc.loc[:, columns_1])
# 2020/3/31 means
new_data = pd.DataFrame(columns=headers)
# exclude world data here
for i in range(len(covid_data)):
    if covid_data.loc[i, 'date'] == '2020-03-31':
        if covid_data.loc[i, 'location'] != 'World':
            new_data.loc[len(new_data)] = covid_data.loc[i, :]
print(new_data.loc[:, ['location', 'new_cases', 'new_deaths']])
print('covid new deaths & cases without world on 2020/3/31\n', np.mean(new_data.loc[:, ['new_cases', 'new_deaths']], axis=0))
# axis=0 means calculation along columns
new_cases = new_data.loc[:, 'new_cases']
labels = ['new cases']
plt.boxplot(new_cases, labels=labels)
plt.title('New cases on 2020/3/31 without world')
plt.show()
new_deaths = new_data.loc[:, 'new_deaths']
plt.boxplot(new_deaths, labels=['new deaths'])
plt.title('New deaths on 2020/3/31 without world')
plt.show()
# worldwide
world = pd.DataFrame(columns=headers)
for i in range(len(covid_data)):
    if covid_data.loc[i, 'location'] == 'World':
        world.loc[len(world)] = covid_data.loc[i, :]
plt.plot(world['date'], world['new_cases'],  'r--', label='new cases')  # r+ means red +, bo means blue dot, why here can world[date]
plt.plot(world['date'], world['new_deaths'], 'b--', label='new deaths')
plt.xticks(world.loc[0:len(world):4, 'date'], rotation=-90)
plt.title('New cases and new deaths worldwide')
plt.rcParams.update({'font.size': 10})
# plt.rc('font', size=12)
plt.xticks(fontsize=6)
plt.legend()
plt.show()
#
maxc = pd.DataFrame(columns=headers)
for i in range(len(covid_data)):
    if covid_data.loc[i, 'location'] != 'World':
        if covid_data.loc[i, 'total_cases'] > 10000:
            maxc.loc[len(maxc)] = covid_data.loc[i, :]
countries = maxc['location']
final_countries = countries.unique()
print('Question: Are there places in the World where there have been more than 10,000 total infections(as of 31 March)? If so, where are they?')
for item in final_countries:
    print(item)