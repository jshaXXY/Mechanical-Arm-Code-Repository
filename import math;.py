import math;
pi=3.1415
r=float(input("r="));
h1=6.7;
h2=9;
l2=7.7;
l3=9.8;
l4=9.8;
from scipy.optimize import fsolve
 
def solve_function(unsolved_value):
    x,y,p,q=unsolved_value[0],unsolved_value[1],unsolved_value[2],unsolved_value[3]
    return [
        x*l4+q*l3-r-l2,
        p*l3-y*l4+h2-h1,
        x**2+y**2-1,
        p**2+q**2-1,
    ]
 
solved=fsolve(solve_function,[0, 0, 0, 0])
print(solved)
print(math.acos(solved[0])*180/pi)
print(math.acos(solved[2])*180/pi) 
 
print("Program done!")