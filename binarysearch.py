#range(lw, up) lowerbound assumed but not upperbound
#random.sample(a,b) takes the list of a and picks b elements from a randomly
#test for 34 to succeed && for 100 to fail
#binarysearch
import random
import math
numbs = random.sample(range(0,100), 100) 
numbs.sort() #sorts lists
for i in range(0, len(numbs)):
    print("Order in sample: %d - Value: %d" % (i, numbs[i]))
    

j = 1
k = len(numbs)
mj = 1
lknfr = 34
while not((j-k) == 2):
    if (lknfr > numbs[math.floor((k+j)/2)-1]):
        j = math.floor(k+j/2)
    else:
        k = math.floor(k+j/2)

print("k " + k)
print("j: " + j)
print(numbs[k]-1)

