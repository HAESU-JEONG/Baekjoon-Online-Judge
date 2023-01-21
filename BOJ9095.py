t = int(input())

def hap(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return hap(num-1) + hap(num-2) + hap(num-3)

for _ in range(t):
    n = int(input())
    print(hap(n))