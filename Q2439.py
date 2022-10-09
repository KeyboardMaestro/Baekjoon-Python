#Baekjoon Question2439

numbers = int(input())

for j in range(0, numbers):
    for i in range(1, numbers-j):
        print(" ", end = "")
    for k in range(0, j+1):
        print("*", end="")
    print("")