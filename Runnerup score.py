n = int(input())
arr = map(int, input().split())
scores=list(set(arr))
scores.sort()
print(scores[-2])
