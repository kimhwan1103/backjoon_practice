hour, min = map(int, input().split())
add_min = input()
add_min = int(add_min)

hour += add_min // 60
min += add_min % 60

if min >= 60:
    hour += 1
    min -= 60
if hour >= 24:
    hour -= 24

print(hour, min)