# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:25:55 2023

@author: shanf
"""

# importing modules
import pandas as pd
import matplotlib.pyplot as plt

# read the data from the bill excel file
ef = pd.read_excel('bill.xlsx')
# print the dataset as output
print(ef)

# define the function of line graph to represent the above data as line plot


def line():
    plt.figure()
    # plotting lineplot for Mark Zuckerberg
    plt.plot(ef['YEAR'], ef['Mark Zuckerberg'], label='Mark Zuckerberg')
    # plotting lineplot for Jeff Besos
    plt.plot(ef['YEAR'], ef['Jeff Besos'], label='Jeff Besos')
    # plotting lineplot for Bill Gates
    plt.plot(ef['YEAR'], ef['Bill Gates'], label='Bill Gates')
    # plotting lineplot for Warren Buffett
    plt.plot(ef['YEAR'], ef['Warren Buffett'], label='Warren Buffett')
    plt.xlabel('Years')  # setting X axis label to Years
    # setting Y axis label to Net worth in billions
    plt.ylabel('Net worth in billions')
    # calling the title function to set the title name for plot
    plt.title('Net Worth comparison of billionares')
    plt.legend()  # calling legend function to set the legends
    plt.show()  # to show the plot


# read the data from the bi22 excel file
df = pd.read_excel('bi22.xlsx')
# print the dataset as output
print(df)


# define the function of bar graph to represent the above data as a bar plot
def bar():
    # defining colours list for the colours of different bars
    colours = ['red', 'green', 'blue', 'yellow', 'black']
    name = df['Name']  # setting a list of names for the plot
    nw = df['Net Worth']  # setting a list of net worth for the plot
    plt.figure()
    # calling bar function to plot the bar chart
    plt.bar(name, nw, color=colours)
    plt.xlabel('Billionares')  # setting X label  to Billionares
    # setting Y label to Net worth in billions
    plt.ylabel('Net worth in billions')
    # calling the title function to set the title name for plot
    plt.title('Net worth comparison in 2022')
    plt.show()  # to show the plot


# raed the data from the pie excel file
gf = pd.read_excel("pie.xlsx")
# print the dataset as output
print(gf)


# define the function of pie chart to represent the above data as pie chart
def pie():
    plt.figure(figsize=(15, 15))
    # using groupby and plot.pie functions to plot the pie chart
    gf.groupby(gf['Nationality']).size().plot(kind='pie', autopct='%.2f%%')
    plt.legend()  # calling the legend functions to set the legend
    # calling the title function to set the title name for plot
    plt.title('International distribution of Billionares')
    plt.show()
# calling the show function to display the plot


line()  # function call for line plot
bar()  # function call for bar plot
pie()  # function call for pie chart
