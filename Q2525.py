#Baekjoon Question 2525

c_hour, c_minute = map(int, input().split())
time = int(input())
remaining = c_minute + time
while remaining >= 60:
    remaining -= 60
    if c_hour != 23:
        c_hour += 1
    else:
        c_hour = 0

print("{} {}".format(c_hour, remaining))
