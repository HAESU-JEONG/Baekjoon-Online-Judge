h, m = input().split()

h = int(h)
m = int(m)

origin_total_minute = h * 60 + m
new_total_minute = origin_total_minute - 45

if new_total_minute < 0:
    new_total_minute = new_total_minute + 24 * 60

new_hour = new_total_minute // 60
new_minute = new_total_minute % 60

print(new_hour, new_minute)