
import numpy as np
from numpy import sin
from numpy import cos
from numpy import tan
from numpy import sinh
from numpy import cosh
from numpy import tanh

from matplotlib import pyplot as plt


def calculate(value1, value2, function):
    x = value1
    y = value2
    return eval(function)


def adams(x0, y0, h, n, f):
    y = np.zeros(n + 1)
    t = np.zeros(n + 1)
    a = np.zeros(n+2)
    y[0] = y0
    t[0] = y0
    a[0] = y0

    for i in range(0, n):
        y[i + 1] = y[i] + h * calculate(x0 + h * i, y[i], f)

    for j in range(0, n):
        t[j + 1] = t[j] + (h / 2) * calculate(x0 + h * j, t[j], f) + (h / 2) * calculate(x0 + h * (j + 1), y[j + 1], f)
        print( 'y %i = %f'% (j + 1, t[j + 1]))
    for i in range(0,n):
        a[1] = t[1]
        a[i+2]=a[i+1] + (h/2)*(3*calculate( x0+h*(i+1), a[i+1], f) - calculate(x0+h*i , a[i],f))
        print('y %i = %f'% (i+1, a[i+1]) )

    x=np.zeros(n+2)
    for i in range(0,n+2):
        x[i]=x0 + h * i

    plt.plot(x, a, 'r')
    plt.show()


f = str(input("If y'=f(x,y) , Please Enter f(x,y) : \n", ))
x = float(input("Please Enter x0 :\n"))
y = float(input("Please Enter y0 :\n"))
h = float(input("Please Enter Step Lenth (h) :\n"))
n = int(input("Please Enter Number Of Steps (n) : \n"))
adams(x, y, h, n, f)
input("Click Enter To Close.")