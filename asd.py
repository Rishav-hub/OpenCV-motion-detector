n,t=map(int, input().split())
lane=list(map(int, input().split()))

for n in range(0,t):
    i,j=map(int, input().split())
    c=j+1
    print(min(lane[i:c]))
