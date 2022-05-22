import sympy as smp
# create a "symbol" called x
x = smp.symbols('x')

# Given the average cost function AC(x) is
AC = 2*x - 11 +50/x

#Find derivative of AC
derivative_AC = AC.diff(x)

#Solving derivative gives required values of x
y=smp.solve(derivative_AC>0)

print("the average cost increases when output is",y)
