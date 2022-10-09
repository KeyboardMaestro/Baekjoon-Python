#Baekjoon Question11022

testcases = int(input())
for i in range(1,testcases+1):
    a, b = map(int,input().split())
    print("Case #{}: {} + {} = {}".format(i, a, b,a+b))