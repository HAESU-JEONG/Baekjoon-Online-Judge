n, w, h, l = map(int, input().split())

width_l = w // l
height_l = h // l
result = width_l * height_l

if result > n:
    print(n)
else:
    print(result)