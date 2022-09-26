# BaekJoon Question 14681
try:
    x_value = int(input())
    y_value = int(input())
    quadrant = 0
    if x_value == 0 | y_value == 0:
        raise ValueError
    else:
        if (x_value > 0 & y_value > 0):
            quadrant = 1
        elif x_value < 0 < y_value:
            quadrant = 2
        elif x_value < 0 and y_value < 0:
            quadrant = 3
        else:
            quadrant = 4
        print("{}".format(quadrant))
except ValueError:
    print(" x and y value must not be 0 to be on 1 to 4 quadrant")
