string = input()
cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in cro:
    string = string.replace(i, "^")
print(len(string))