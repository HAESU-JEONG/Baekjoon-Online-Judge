n = int(input())

def star(length):
    if length == 3:
        return ['***', '* *', '***']
    
    arr = star(length // 3)
    stars = []

    for i in arr:
        stars.append(i*3)
    
    for i in arr:
        stars.append(i + ' ' * (length // 3) + i)
    
    for i in arr:
        stars.append(i * 3)
    
    return stars
print('\n'.join(star(n)))