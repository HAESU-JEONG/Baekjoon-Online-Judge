T = input()
P = input()

if P in T:
    print(T.count(P))
    while True:
        if len(T) < len(P):
            break

        index = T.find(P)
        T = ''.join(list(T[index + len(P) + 1:]))
        print(index + 1, end = " ")