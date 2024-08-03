from itertools import combinations

n=input()
s=list(input().split(' '))
k=int(input())
c=0

for i in (combinations(s,k)):
    if 'a' in i:
        c=c+1
print(c/len(list(combinations(s,k))))

'''
Sample Input

4 
a a c d
2
Sample Output

0.8333
Explanation

All possible unordered tuples of length 2 comprising of indices from 1 to 4 are:


Out of these 6 combinations, 5 of them contain either index 1 or index 2 which are the indices that contain the letter a ''.
(i.e) a a c d - aa,ac,ad,ac,ad,cd - therefore output should be like 5/6

'''