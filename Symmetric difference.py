
int(input())
M = set(map(int, input().split()))
int(input())
N = set(map(int, input().split()))

for i in sorted(M.symmetric_difference(N)):
    print(i)