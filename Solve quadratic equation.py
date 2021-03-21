import math

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

d = (b**2) - (4*a*b)

sol1 = (-b-math.sqrt(d))/(2*a)
sol2 = (-b+math.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))

