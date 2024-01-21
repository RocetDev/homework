

for file in [open('4_A.txt'), open('4_B.txt')]:
    n = [int(x) for x in file]
    s = 0
    count = 0
    mx = -1
    b = [10**10] * 3
    for i in n:
        s += i
        if i % 5 == 0:
            count += 1
        if count % 3 == 0:
            mx = max(mx, s)
        if count % 3 != 0:
            mx = max(mx, s-b[count%3])
            
        b[count%3] = min(b[count%3], s)
        
    print(mx)
            
        




