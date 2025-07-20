from tkinter import N
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

def euler(x0, y0, h, n, f):
    y = np.zeros(n+1)
    y[0] = y0

    for i in range(0, n ):
        y[i + 1] = y[i] + h * calculate(x0 + h * i, y[i], f)
        print('y %i = %f' % (i+1, y[i+1]))

    x=np.zeros(n+1)
    for i in range(0,n+1):
        x[i]=x0 + h * i

    plt.plot(x, y, 'r')
    plt.show()


def eu_rich(x0 , y0 , h , n , f):
    y_h=euler(x0 , y0 , h , 2*n+3 , f)
    y_2h=euler(x0 , y0 , 2*h , n , f)

    y_hat = np.zeros(n+1)
    y_hat[0]=y0

    for i in range (0 ,n):
        y_hat[i+1]=2*y_h[2*(i+1)] - y_2h[i+1]
        print('y_richardson %i = %f' % (i+1, y_hat[i+1]))

    x=np.zeros(n+1)
    for i in range(0,n+1):
        x[i]=x0 + h * i
    

    plt.plot(x, y_hat, 'red')
    plt.plot(x,y_2h, 'green')
    plt.show()

def imp_rung_2 (x0 , y0 , h, n , f):
    z=np.zeros(2)
    k=np.zeros(2)
    y=np.zeros(n+1)
    y[0]=y0

    for i in range (0 , n):
        z[0]= y[i]
        z[1]= y[i]+(1/2)*h*calculate(x0+i*h , y[i] , f)

        k[0] = y[i] + (1/4)* h *(calculate( x0+i*h , z[0] , f) - calculate(x0+ (i+ 2/3 )*h , z[1] , f))
        k[1] = y[i] + (1/12)*h *(3* calculate (x0+i*h , z[0] , f )+ 5* calculate(x0+(i+2/3)*h , z[1] , f))

        y[i+1]= y[i] + (1/4)*h *(calculate(x0+i*h , k[0], f)+ 3* calculate(x0+(i+2/3)*h , k[1] , f))
        
        print('y %i = %f' % (i+1, y[i+1]))

    x=np.zeros(n+1)
    for i in range(0,n+1):
        x[i]=x0 + h * i

    plt.plot(x, y, 'r')
    plt.show()


def rung_2 (x0 , y0 , h, n , f):
    k=np.zeros(2)
    y=np.zeros(n+1)
    y[0]=y0

    for i in range (0 , n ):
        k[0]=y[i]
        k[1]=y[i]+(1/2)*h*calculate(x0+i*h , y[i] , f)
        
        y[i+1] = y[i] + (1/2) * h* (calculate(x0 + i *h , k[0] , f) + calculate(x0+ (i+1) * h , k[1] , f))
        
        print('y %i = %f' % (i+1, y[i+1]))

    x=np.zeros(n+1)
    for i in range(0,n+1):
        x[i]=x0 + h * i

    plt.plot(x, y, 'r')
    plt.show()   

def runge_3 (x0 , y0 , h , n, f):
    k=np.zeros(3)
    y=np.zeros(n+1)
    y[0]=y0

    for i in range(0,n):
        k[0]= y[i]
        k[1]= y[i]+ (h/2)*calculate(x0+h*i,k[0],f)
        k[2]= y[i]+ (h)*((-1)*calculate(x0+h*i,k[0],f)+(2)*calculate(x0+h*i+h/2,k[1],f))
        y[i+1]=y[i]+ h*((1/6)*calculate(x0+h*i,k[0],f)+(2/3)*calculate(x0+h*i+h/2,k[1],f)+(1/6)*calculate(x0+(i+1)*h,k[2],f))

        print('y %i = %f' % (i+1, y[i+1]))

    x=np.zeros(n+1)
    for i in range(0,n+1):
        x[i]=x0 + h * i   

    plt.plot(x, y, 'r')
    plt.show()    

def rung_4 (x0 , y0 , h, n , f):
    k=np.zeros(4)
    y=np.zeros(n+1)
    y[0]=y0

    for i in range (0 , n ):
        k[0]=y[i]
        k[1]=y[i]+(1/2)*h*calculate(x0+i*h , k[0] , f)
        k[2]=y[i]+(1/2)*h*calculate(x0+(i+1/2)*h, k[1] , f)
        k[3]= y[i] + h* calculate(x0+h*(i+1) , k[2], f)
        
        y[i+1] = y[i] + (1/6)* h *( calculate(x0+i*h , k[0] , f)  
                                   + 2* calculate(x0+(i+1/2)*h , k[1] , f) 
                                   + 2 * calculate(x0+(i+1/2)*h , k[2], f) 
                                   + calculate(x0+(i+1)*h , k[3] , f) )
        
        print('y %i = %f' % (i+1, y[i+1]))

    x=np.zeros(n+1)
    for i in range(0,n+1):
        x[i]=x0 + h * i

    plt.plot(x, y, 'r')
    plt.show()

f = str(input("If y'=f(x,y) , Please Enter f(x,y) : \n", ))
x = float(input("Please Enter x0 :\n"))
y = float(input("Please Enter y0 :\n"))
h = float(input("Please Enter Step Lenth (h) :\n"))
n = int(input("Please Enter Number Of Steps (n) : \n"))
rung_4(x, y, h, n, f)
input("Click Enter To Close.")

def adams_3(x0 , y0 , h , n, f):
    k=np.zeros(3)
    y=np.zeros(n+1)
    y1= np.zeros(n+3)
    y[0]=y0
    y1[0]=y0

    for i in range(0,n):
        k[0]= y[i]
        k[1]= y[i]+ (h/2)*calculate(x0+h*i,k[0],f)
        k[2]= y[i]+ (h)*((-1)*calculate(x0+h*i,k[0],f)+(2)*calculate(x0+h*i+h/2,k[1],f))
        y[i+1]=y[i]+ h*((1/6)*calculate(x0+h*i,k[0],f)+(2/3)*calculate(x0+h*i+h/2,k[1],f)+(1/6)*calculate(x0+(i+1)*h,k[2],f))    
    
    for i in range(0,n):
        y1[1]=y[1]
        y1[2]=y[2]
        y1[i+3]= y1[i+2]+ (h/12)*(23*calculate(x0+(i+2)*h,y1[i+2],f)-16*calculate(x0+(i+1)*h,y1[i+1],f)+5*calculate(x0+i*h,y1[i],f))

        print('y %i = %f' % (i+1, y1[i+1]))

    x=np.zeros(n+3)
    for i in range(0,n+3):
        x[i]=x0 + h * i   

    plt.plot(x, y1, 'r')
    plt.show()            

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

def moulton(x0, y0, h, n, f):
    y = np.zeros([n + 1])
    t = np.zeros([n + 1])
    a = np.zeros([n+2])
    b = np.zeros([n+2])
    y[0] = y0
    t[0] = y0
    a[0] = y0
    b[0]= y0

    for i in range(0, n):
        y[i + 1] = y[i] + h * calculate(x0 + h * i, y[i], f)

    for j in range(0, n):
        t[j + 1] = t[j] + (h / 2) * calculate(x0 + h * j, t[j], f) + (h / 2) * calculate(x0 + h * (j + 1), y[j + 1], f)
        
    for i in range(0,n):
        a[1] = t[1]
        a[i+2]=a[i+1] + (h/2)*(3*calculate( x0+h*(i+1), a[i+1], f) - calculate(x0+h*i , a[i],f))

    for i in range (0,n):
        b[1] = a [1]
        b[i+2] = b[i+1] + (h/12)*(5*calculate(x0+h*(i+2),a[i+2],f) + 8*calculate(x0+h*(i+1),b[i+1],f) - calculate(x0+h*i,b[i], f ))
        print( 'y %i = %f'% (i + 1, b[i + 1]))    



    x=np.zeros(n+2)
    for i in range(0,n+2):
        x[i]=x0 + h * i

    plt.plot(x, b, 'r')
    plt.show()   

def trapezoidal(x0, y0, h, n, f):
    y = np.zeros(n+1)
    t = np.zeros(n+1)
    y[0] = y0
    t[0] = y0

    for i in range(0, n):
        y[i + 1] = y[i] + h * calculate(x0 + h * i, y[i], f)

    for j in range(0, n):
        t[j + 1] = t[j] + (h / 2) * calculate(x0 + h * j, t[j], f) + (h / 2) * calculate(x0 + h * (j + 1), y[j + 1], f)
        print( 'y %i = %f'% (j + 1, t[j + 1]))
   
    x=np.zeros(n+1)
    for i in range(0,n+1):
        x[i]=x0 + h * i

    plt.plot(x, t, 'r')
    plt.show()


c = int(input(
"Please Choose Method From List.\n euler:1 \n euler richardson:2 \n  trapezoidal:3 \n adams bashfort 2nd Order :4 \n  adams bashfort 3rd Order :5 \n adams moulton 2nd Order : 6 \n adams moulton 3rd Order :7 \n runge kutta 2nd Order :8 \n runge kutta 3rd Order : 9 \n runge kutta 4th Order : 10 \n Implicit runge kutta 2nd Order:11 \n" ))
f = str(input("If y'=f(x,y) , Please Enter f(x,y) : \n", ))
x = float(input("Please Enter x0 :\n"))
y = float(input("Please Enter y0 :\n"))
h = float(input("Please Enter Step Lenth (h) :\n"))
n = int(input("Please Enter Number Of Steps (n) : \n"))

if c == 1 :
    euler(x,y,h,n,f)
    input("Click Enter To Close.")
elif c==2 :
    eu_rich(x,y,h,n,f)
    input("Click Enter To Close.")
elif c==3 :
    trapezoidal(x,y,h,n,f)
    input("Click Enter To Close.")
elif c== 4 :
    adams(x,y,h,n,f)
    input("Click Enter To Close.")
elif c== 5 :
    adams_3(x,y,h,n,f)
    input("Click Enter To Close.")
elif c==6 :
    moulton(x,y,h,n,f)
    input("Click Enter To Close.")
elif c==7 :
    moulton_3(x,y,h,n,f)
    input("Click Enter To Close.")      
elif c== 8 :
    rung_2(x,y,h,n,f) 
    input("Click Enter To Close.")
elif c== 9:
    runge_3(x,y,h,n,f)
    input("Click Enter To Close.")
elif c==10 :
    rung_4(x,y,h,n,f)
    input("Click Enter To Close.")
elif c==11:
    imp_rung_2(x,y,h,n,f)
    input("Click Enter To Close.")                            