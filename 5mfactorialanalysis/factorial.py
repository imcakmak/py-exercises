#python read file
f = open('test.dat', 'r')
#install via pip install tqdm if you don't have it
from tqdm import tqdm

#create array with 10 elements
a = [0] * 10

print("Computing...")
for ch in tqdm(f.read()):
    for i in range(0,10):
        if ch == str(i):
            a[i] = a[i] + 1
            break
#close the file
f.close()
print(a)

# The number of times numbers from 0 to 9 occurs in 5 million factorial:
# [4255608, 3007682, 3007868, 3010002, 3010331, 3004800, 3008184, 3002771, 3007690, 3008446]