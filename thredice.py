for _ in range(int(input())):
    
    x,y = map(int,input().split())
    count = 0
    
    for i in range(1,7):
        if i>x+y:
            count+=1 
            
    print(count/6)
