t=int(input())
for i in range(t):
    s=0
    st=list(map(int,input().split()))
    pl=list(map(int,input().split()))
    for j in range(st[1]):
            if pl[j] == 0:
                s+=st[2]
            else :
                s+=st[3]
    print(s)
