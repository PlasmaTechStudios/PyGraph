import matplotlib.pyplot as plt
import math
import numpy
x = []
y = []
x2 = []
y2 = []
def graph():
    coefficient = float(input("input the coefficient "))
    constant = float(input("input the constant "))
    exponent = float(input("input the exponent "))
    for i in range(50):
        x.append(i)
    for xval in range(50):
        y.append(coefficient*(xval**exponent)+constant)
    ##########################
    coefficient2 = float(input("input the second coefficient "))
    constant2 = float(input("input the second constant "))
    exponent2 = float(input("input the second exponent "))
    for d in range(50):
        x2.append(d)
    for xval2 in range(50):
        y2.append(coefficient2*(xval2**exponent2)+constant2)       
    if(exponent == exponent2):
       new_coefficient = max(coefficient, coefficient2) - min(coefficient, coefficient2)
       new_constant = max(constant, constant2) - min(constant, constant2)
       if(exponent == exponent2):
          xintval =(-new_constant/new_coefficient)**(1./exponent)
          yintval = new_coefficient * (xintval ** exponent) + new_constant
          print("One intersection is at point", xintval, " , ", yintval)
       else:
           print("No intersection in this range or the polynomials are different")
graph()
print("The blue polynomial is the first set of numbers entered.")
print("The orange polynomial is the second set of numbers entered.")
fig = plt.figure(frameon=False)
fig.canvas.toolbar.pack_forget()
plt.plot(x,y)
plt.plot(x2,y2)
plt.show()
