#Beakjoon Q10871
n, x = map(int, input().split())
temp = []
temp.extend(input().split())

for i in temp:
    if int(i) < x:
        print("{}".format(int(i)), end=" ")