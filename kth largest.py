import heapq
'''def kthlargest(arr,k):
    arr=[-num for num in arr]
    heapq.heapify(arr)
    for x in range(k):
        d=heapq.heappop(arr)
    return -d
arr=[3,4,8,6,5,2]
print(arr)

while True:
    opt=input('Enter k value(Enter no to break):')
    if(opt=='no'):
        break
    k=int(opt)
    if k<=len(arr):
        print(f"{k}nd largest is",{kthlargest(arr,k)})
        continue
    else:
        print('Index out of Range')'''


def goldenwire(arr):
    heapq.heapify(arr)
    tot_cost=0
    while len(arr)>1:
        w1=heapq.heappop(arr)
        w2=heapq.heappop(arr)
        tot_cost+=(w1+w2)
        heapq.heappush(arr,(w1+w2))
    return tot_cost
    
arr=list(map(int,input().split(',')))
print('Total Cost:',goldenwire(arr))

        
