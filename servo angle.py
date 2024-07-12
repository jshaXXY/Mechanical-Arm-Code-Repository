import math
from scipy.optimize import fsolve

x1=float(input("x1="))
y1=float(input("y1="))
r=math.sqrt(x1*x1+y1*y1)
h1=float(input("h1="))
h2=float(input("h2="))
l3=float(input("l3="))
l4=float(input("l4="))

 
def solve_function(unsolved_value):
    x,y,p,q=unsolved_value[0],unsolved_value[1],unsolved_value[2],unsolved_value[3]
    return [
        x*l4+q*l3-r,
        p*l3-y*l4+h2-h1,
        x**2+y**2-1,
        p**2+q**2-1,
    ]
 
solved=fsolve(solve_function,[0, 0, 0, 0])
print(solved)
print(math.acos(solved[0]))
print(math.acos(solved[2])) 
 
print("Program done!")
