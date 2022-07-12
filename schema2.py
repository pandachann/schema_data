import pickle
import operator

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
from collections import Counter
import math
import statistics

# open a file, where you stored the pickled data
file = open('training_data.pkl', 'rb')

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

#miből mennyi van
# count of each element in tuple

#dolgok, ennyiszer, szétszedve
items = []
counts = []
for item in unique_t:
    items.append(item)
    counts.append(flatTup.count(item))
    #print(f"Count of {item} ------------  {flatTup.count(item)}")


plt.plot(items, counts)
plt.show()
c = np.column_stack((items, counts))

#PANDAS

df = pd.DataFrame(zip(items, counts), columns=['SCHEMAS','COUNTS'])
print("------------------------")
print(df)

print("------------------------")
print(df.sum())

print("------------------------")
print(df.mean())

print("------------------------")
print(df.describe())

print("------------------------")
print(df.max())


print("------------------------")
print(df.sort_values(by="COUNTS", ascending=False).head(30))



#házanként miből mennyi?
#tuple sok listával-> minden listára kéne egy kimutatás hogy a házban milyen arányban vannak a dolgok


















