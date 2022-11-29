#range(lw, up) lowerbound assumed but not upperbound
#random.sample(a,b) takes the list of a and picks b elements from a randomly
#test for 34 to succeed && for 100 to fail
#linearsearch
import random
numbs = random.sample(range(0,100), 100) 
xf = False
for i in range(0, len(numbs)):
    print("Order in sample: %d - Value: %d" % (i, numbs[i]))
    if (numbs[i] == 34):
        print("Hallelujah match above!")
        xf = True
    
if not(xf): 
    print("Sadly no match.")



