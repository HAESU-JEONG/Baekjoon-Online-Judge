n, m = map(int, input().split())
board = []
cnt_list = []

for i in range(n):
    board.append(input())

for a in range(n - 7):
    for b in range(m - 7):
        w_index = 0
        b_index = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] == 'B':
                        w_index += 1
                    else:
                        b_index += 1
                else:
                    if board[i][j] == 'B':
                        b_index += 1
                    else:
                        w_index += 1
        
        cnt_list.append(w_index)
        cnt_list.append(b_index)

print(min(cnt_list))