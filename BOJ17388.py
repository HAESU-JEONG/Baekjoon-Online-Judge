Soongsil, Korea, Hanyang = map(int, input().split())
sum_total = Soongsil + Korea + Hanyang

if sum_total >= 100:
    print("ok")
else:
    min_univ = min(Soongsil, Korea, Hanyang)
    if min_univ == Soongsil:
        print("Soongsil")
    elif min_univ == Korea:
        print("Korea")
    else:
        print("Hanyang")