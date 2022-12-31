import matplotlib.pyplot as plt
import numpy as np


#Quadratic time O(n^2)


list = np.random.randint(0,100,15) #our list to sort
x = np.arange(0,15,1) #numbers from 0 to 15, were gonna use this to print our graphic later


indexing_length = len(list) - 1
sorted = False

while not sorted:
    sorted = True
    for i in range(0, indexing_length):
        plt.bar(x, list)
        plt.pause(0.01)
        plt.clf()
        if list[i] > list[i+1]:
            sorted = False
            list[i], list[i+1] = list[i+1], list[i]
     

plt.show()
plt.pause(0)
print(list)