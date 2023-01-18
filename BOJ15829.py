n = int(input())
string_list = list(input())
ans = 0

for i in range(n):
    ans += ((ord(string_list[i]) - 96) * (31 ** i))
print(ans % 1234567891)