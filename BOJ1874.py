num = int(input())
count = 0
stack = []
result = []
check = False
for _ in range(num):
    x = int(input())
    while count < x:
        count += 1
        stack.append(count)
        result.append("+")
    
    if stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        check = True
        break

if check:
    print("NO")
else:
    print("\n".join(result))