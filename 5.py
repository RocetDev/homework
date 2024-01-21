

for file in [open('5_A.txt'), open('5_B.txt')]:
    n = [int(x) for x in file]
    s = 0
    mn = 10**10
    count = 0
    b = [0]*len(n)
    for i in n:
        s += i
        if i % 3 ==0 : count += 1
        if count == 10: mn = min(mn, s)
        if count > 10: mn = min(mn, s-b[count-10])
            
        b[count] = max(b[count], s)
        
        
    print(mn)            


