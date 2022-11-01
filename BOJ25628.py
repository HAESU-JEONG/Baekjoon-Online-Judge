bread, patty = map(int, input().split())
bread_pair = bread // 2

if bread_pair < patty:
    print(bread_pair)
else:
    print(patty)