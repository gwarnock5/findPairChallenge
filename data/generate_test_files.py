# Python3 code to demonstrate
# to generate random number list
# using list comprehension + randrange()
import random
import csv
 
import numpy as np
 
# print the list of 10 integers from 3  to 7
data = list(np.random.randint(low = 1,high=500000,size=500000))
data_set = set(data)

# opening the csv file in 'w+' mode
file = open('dataFiveHundred.csv', 'w+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerow(data_set)