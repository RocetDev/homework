
for file in [open('3_A.txt'), open('3_B.txt')]:
    n = [int(x) for x in file]
    s = 0
    k = 0
    count = 0
    b = [0]*11
    for i in n:
        s += i
        if i % 5 == 0:
            k += 1
        if k % 11 == 0:
            count += 1
        count += b[k%11]
        b[k%11] += 1
    print(count)


