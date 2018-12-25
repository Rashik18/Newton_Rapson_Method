import sympy as sym
import matplotlib.pyplot as plt
a=[]
b=[]
c=[]

i=-20
def f(x):
    return x**2-5*x-6


for i in range (-20,21):
    x=i
    F = (x*2)-5
    if(F==0):
        print('No output for input: ',x)
        x=x+1
    f1=(x*2)-5
    tol=100 
    y = x - f(x)/(f1)
    count=0
    #print(i) 
    while(abs(tol)>10**(-5)):
        y = x - (f(x)/f1)
        #print(y) 
        tol = y - x
        x=y
        count+=1
        #print("y:",y)
        if(abs(y) > 10**10):
            print("y is too big for i=",i)
            count=0
            break
        if(count == 10000):
               print('no output or input',i)
               count=0
               break
        if(f1 == 0):
            i=i+1
            print('derivative error')
            count=0
            break
        #else:
         #   i = i + 1
    #print("y:",y)
    #print("i:",i)
    print("for i is ", i, " The Root is ", y , "Total iteration",count)
    a.append(i)
    b.append(y)
    c.append(count)


plt.plot(a,b)
plt.show()
plt.plot(a,c)
plt.show()
