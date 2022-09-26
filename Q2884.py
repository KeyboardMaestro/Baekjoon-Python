#Baekjoon Question 2884
try:
    hour, minute = map(int, input().split())
    if minute >= 45:
        print("{} {}".format(hour, minute-45))
    else:
        temp = minute - 45
        if hour == 0:
            print("{} {}".format(23, 60+temp))

        else:
            print("{} {}".format(hour-1, 60+temp))

except ValueError:
    print(" 0 <= h <= 23, 0 <= m <= 59")

