testcase = int(input())

for _ in range(testcase):
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))
    idx = list(range(len(num_list)))
    idx[m] = 'target'

    cnt = 0

    while True:
        if num_list[0] == max(num_list):
            cnt += 1
            if idx[0] == 'target':
                print(cnt)
                break
            else:
                num_list.pop(0)
                idx.pop(0)
        else:
            num_list.append(num_list.pop(0))
            idx.append(idx.pop(0))