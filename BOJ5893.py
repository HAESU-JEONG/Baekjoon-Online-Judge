bin_string = '0b' + input()
n = int(bin_string, 2)
n = n * 17
bin_number = bin(n)
print(bin_number[2:])