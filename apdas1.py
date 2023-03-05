# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:25:55 2023

@author: shanf
"""

import pandas as pd
import matplotlib.pyplot as plt

ef = pd.read_excel('bill.xlsx')
print(ef)


def line():
    plt.figure()
    plt.plot(ef['YEAR'], ef['Mark Zuckerberg'], label='Mark Zuckerberg')
    plt.plot(ef['YEAR'], ef['Jeff Besos'], label='Jeff Besos')
    plt.plot(ef['YEAR'], ef['Bill Gates'], label='Bill Gates')
    plt.plot(ef['YEAR'], ef['Warren Buffett'], label='Warren Buffett')
    plt.xlabel('Years')
    plt.ylabel('Net worth in billions')
    plt.title('Net Worth comparison of billionares')
    plt.legend()
    plt.show()


line()

df = pd.read_excel('bi22.xlsx')
print(df)


def bar():
    colours = ['red', 'green', 'blue', 'yellow', 'black']
    name = df['Name']
    nw = df['Net Worth']
    plt.figure()
    plt.bar(name, nw, color=colours)
    plt.xlabel('Billionares')
    plt.ylabel('Net worth in billions')
    plt.title('Net worth comparison in 2022')
    plt.show()


bar()
