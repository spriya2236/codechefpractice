for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if(x>=y):
        print('pizza')
    elif(x<y and x>=z):
        print('burger')
    else:
        print('nothing')
