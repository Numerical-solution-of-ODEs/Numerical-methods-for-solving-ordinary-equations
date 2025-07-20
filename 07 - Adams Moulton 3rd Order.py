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

def moulton_3(x0 , y0 , h , n, f):
    k=np.zeros(3)
    y=np.zeros(n+1)
    y1= np.zeros(n+3)
    y2= np.zeros(n+3)
    y[0]=y0
    y1[0]=y0
    y2[0]=y0
    for i in range(0,n):
        k[0]= y[i]
        k[1]= y[i]+ (h/2)*calculate(x0+h*i,k[0],f)
        k[2]= y[i]+ (h)*((-1)*calculate(x0+h*i,k[0],f)+(2)*calculate(x0+h*i+h/2,k[1],f))
        y[i+1]=y[i]+ h*((1/6)*calculate(x0+h*i,k[0],f)+(2/3)*calculate(x0+h*i+h/2,k[1],f)+(1/6)*calculate(x0+(i+1)*h,k[2],f))    
    
    for i in range(0,n):
        y1[1]=y[1]
        y1[2]=y[2]
        y1[i+3]= y1[i+2]+ (h/12)*(23*calculate(x0+(i+2)*h,y1[i+2],f)-16*calculate(x0+(i+1)*h,y1[i+1],f)+5*calculate(x0+i*h,y1[i],f))

    for i in range (0,n):
        y2[1]=y1[1]
        y2[2]=y1[2]

        y2[i+3]= y2[i+2]+ (h/24)*(9*calculate(x0+(i+3)*h,y1[i+3],f)+19*calculate(x0+(i+2)*h,y2[i+2],f)-5*calculate(x0+(i+1)*h,y2[i+1],f)+calculate(x0+i*h,y[i],f))

        print('y %i = %f' % (i+1, y2[i+1]))

    x=np.zeros(n+3)
    for i in range(0,n+3):
        x[i]=x0 + h * i   

    plt.plot(x, y2, 'r')
    plt.show()  


f = str(input("If y'=f(x,y) , Please Enter f(x,y) : \n", ))
x = float(input("Please Enter x0 :\n"))
y = float(input("Please Enter y0 :\n"))
h = float(input("Please Enter Step Lenth (h) :\n"))
n = int(input("Please Enter Number Of Steps (n) : \n"))

moulton_3(x,y,h,n,f)

input("Click Enter To Close.")