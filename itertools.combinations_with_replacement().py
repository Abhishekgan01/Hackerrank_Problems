from itertools import combinations_with_replacement
s,n=input().split(' ')

for i in list(combinations_with_replacement(sorted(s),int(n))):
    print(''.join(i))

'''
Sample Input

HACK 2

Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
'''