a, b = map(int, input().split())
c = int(input())

total_minute = a * 60 + b + c

if total_minute >= 60*24:
    total_minute = total_minute - 60 * 24

hour = total_minute // 60
minute = total_minute % 60

print(hour, minute)