num = int(input())
for _ in range(num):
    a, b = input().split()
    num_a = int(a, 2)
    num_b = int(b, 2)
    result = num_a + num_b
    print(format(result, 'b'))