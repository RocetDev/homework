
for file in [open('1_A.txt'), open('1_B.txt')]:
    n = [int(x) for x in file]
    count = 0
    s = 0
    mx = 0
    b = [0]*666
    for i in n:
        s += i
        if s % 666 == 0: count += 1
        




