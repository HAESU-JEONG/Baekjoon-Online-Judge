hamberger = []
drink = []

hamberger.append(int(input()))
hamberger.append(int(input()))
hamberger.append(int(input()))
drink.append(int(input()))
drink.append(int(input()))

min_hamberger = min(hamberger)
min_drink = min(drink)

print(min_hamberger + min_drink - 50)