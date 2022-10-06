import matplotlib.pyplot as plt
from numpy import *

# CREATING EMPTY ARRAY FOR STORING CONTROL POINT INPUT
array_x = array([])
array_y = array([])

for i in range(4):
    value_x = int(input(f"Enter x  coordinate of {i}th control point: "))
    array_x = append(array_x, value_x)
    value_y = int(input(f"Enter y coordinate of {i}th control point: "))
    array_y = append(array_y, value_y)

# plt.plot(array_x, array_y, 'o')
# plt.show()

x = array([])
y = array([])

t = 0
while t < 1:
    # FOR drawing straight line
    # put_x = (1-t) * array_x[0] + t * array_x[1]
    # put_y = (1 - t) * array_y[0] + t * array_y[1]
    #
    # Parabolic Arc
    # put_x = pow(1 - t, 2) * array_x[0] + 2 * t * pow(1 - t, 1) * array_x[1] + pow(t, 2) * array_x[2]
    # put_y = pow(1 - t, 2) * array_y[0] + 2 * t * pow(1 - t, 1) * array_y[1] + pow(t, 2) * array_y[2]

    # CUBIC CURVE
    put_x = pow(1 - t, 3) * array_x[0] + 3 * t * pow(1 - t, 2) * array_x[1] + 3 * t * t * pow(1 - t, 1) * array_x[2]\
            + pow(t, 3) * array_x[3]
    put_y = pow(1 - t, 3) * array_y[0] + 3 * t * pow(1 - t, 2) * array_y[1] + 3 * t * t * pow(1 - t, 1) * array_y[2] \
            + pow(t, 3) * array_y[3]

    x = append(x, put_x)
    y = append(y, put_y)
    t += 0.01
    # print(x)

plt.title("CUBIC CURVE")
plt.plot(array_x, array_y, 'o')
plt.plot(array_x, array_y, color='b', label='control point')
plt.plot(x, y, color='g', label='curve')
plt.legend()
plt.show()

# How TO DRAW POINTS ON PYTHON

# import matplotlib.pyplot as plt
# x = range(1,10)
# y = range(1,10)
# plt.plot(x,y,'o')
# plt.show()
