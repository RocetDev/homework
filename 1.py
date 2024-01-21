



for file in [open('1_A.txt'), open('1_B.txt')]:
    n = [int(x) for x in file]
    s = 0
    mx = 0
    b = [10**10]*1000
    for i in n:
        s += i
        if s % 1000 == 0:
            mx = s
        else:
            mx = max(mx, s-b[s%1000])
        b[s%1000] = min(s, b[s%1000])
        
    print(mx)





