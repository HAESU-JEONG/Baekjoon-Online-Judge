mingok = list(map(int, input().split()))
manse = list(map(int, input().split()))

if sum(mingok) > sum(manse) or sum(mingok) == sum(manse):
    print(sum(mingok))
else:
    print(sum(manse))