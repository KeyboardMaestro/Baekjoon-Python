#Baekjoon Question25304

total = int(input())
numbers = int(input())
sum = 0
for i in range(0 ,numbers) :
    a, b = map(int, input().split())
    sum += (a*b)

if (sum == total) :
    print("Yes")
else:
    print("No")