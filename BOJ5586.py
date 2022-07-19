string = input()

joi = string.count("JOI")
ioi = 0
i = 0

while True:
    index = string.find("IOI", i, len(string))
    if index < 0 or i > len(string):
        break
    ioi += 1
    i = index + 1


print(joi)
print(ioi)