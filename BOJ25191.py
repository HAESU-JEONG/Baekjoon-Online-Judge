chicken = int(input())
coke, beer = map(int, input().split())

count = coke // 2 + beer

if chicken > count:
    print(count)
else:
    print(chicken)