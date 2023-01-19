num = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]

for _ in range(num):
    fibo_num = int(input())
    length = len(zero)
    if fibo_num >= length:
        for i in range(length, fibo_num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[fibo_num], one[fibo_num])