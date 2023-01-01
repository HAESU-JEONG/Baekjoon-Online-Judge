def isPrime(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

m = int(input())
n = int(input())
prime_list = []
for i in range(m, n+1):
    if isPrime(i):
        prime_list.append(i)

if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list))
    print(prime_list[0])