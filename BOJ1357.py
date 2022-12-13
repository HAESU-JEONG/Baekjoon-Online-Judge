x, y = input().split()

list_x = list(x)
list_y = list(y)

rev_x = reversed(list_x)
rev_y = reversed(list_y)

total = int(''.join(rev_x)) + int(''.join(rev_y))
list_total = list(str(total))
rev_total = reversed(''.join(list_total))

print(int(''.join(rev_total)))