import pickle
import operator

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
from collections import Counter
import math
import statistics
from pprint import pprint
from tabulate import tabulate



# open a file, where you stored the pickled data
file = open('training_data.pkl', 'rb')
#file=open('validation_data.pkl', 'rb')

# dump information to that file
data = pickle.load(file)

# close the file
file.close()


#schemes
sch = list(zip(*data))[2]

#flatten
flatTup = tuple(sum(sch, []))

#print(flatTup)
unique_t = set(flatTup)


#dolgok, ennyiszer, szétszedve
items = []
counts = []
for item in unique_t:
    items.append(item)
    counts.append(flatTup.count(item))
    #print(f"Count of {item} ------------  {flatTup.count(item)}")



#PANDAS
df = pd.DataFrame(zip(items, counts), columns=['SCHEMAS','COUNTS'])
print("------------------------")
print(df)

print("---------SUM------------")
print(df.sum())

print("---------MEAN--------------")
print(df.mean())

print("---------DESCRIBE---------------")
print(df.describe())

print("----------MOST USED--------------")
print(df.max())


print("------------------------")
print(df.sort_values(by="COUNTS", ascending=False).head(30))



#házanként miből mennyi?
#tuple sok listával-> minden listára kéne egy kimutatás hogy a házban milyen arányban vannak a dolgok

example_list = sch
test = ['wall']

score=[]
score_all = []
for item in example_list:
    score = [sum(s in test for s in lst) for lst in example_list]
    score_all = [len(i) for i in example_list]

#%arany - jelen esetben falak aránya, de mást is meg lehet nézegetni

product = list(map(lambda x,y: x/y ,score,score_all))

aranyok = zip(score, score_all,product)

print(tabulate(aranyok))


def Average(lst):
    return sum(lst) / len(lst)

print(Average(product))

###nagyobb dataframe készítése?

#minden oszlop egy elemlista
#minden sor egy fajtalista
#mennyi van az adott elemből benne
