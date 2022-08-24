import sys
input = sys.stdin.readline

n = int(input())
num_card = []
find_num = []

num_card = list(map(int, input().split()))

num_dic = dict()

for i in num_card:
    if i in num_dic:
        num_dic[i] += 1
    else:
        num_dic[i] = 1

m = int(input())
find_num = list(map(int, input().split()))

for i in find_num:
    if i in num_dic:
        print(num_dic[i], end=" ")
    else:
        print(0, end = " ")