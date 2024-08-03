nestList=[]
tempscore=[]
result=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    nestList.append([name,score])
    tempscore.append(score)
        
    tempscore=list(set(tempscore))
    tempscore.sort()
    second_lowest_value=tempscore[1]
    
for i in range(len(nestList)):
    if(nestList[i][1] == second_lowest_value):
        result.append(nestList[i][0])
    result.sort()
    
for i in result:
    print(i)
