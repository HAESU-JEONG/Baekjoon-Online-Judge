A, B, C = map(int, input().split())
D = int(input())

hour = A
minute = B
sec = C + D % 60

D = D // 60

if sec >= 60:
    minute += 1
    sec -= 60

minute += D % 60
D = D // 60

if minute >= 60:
    hour += 1
    minute -= 60

hour += D % 24
if hour >= 24:
    hour -= 24

print(hour, minute, sec)