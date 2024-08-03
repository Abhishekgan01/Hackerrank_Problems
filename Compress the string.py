from itertools import *
n=input()
for i,j in groupby(n):
    print(tuple([len(list(j)), int(i)]),end=" ")

'''
Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
'''

# n=input()
# for i,j in (groupby(n)):
#     print(i,len(list(j)))