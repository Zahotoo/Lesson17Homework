# Homework
# Write a program that asks for the a, b and c of a Quadratic Equation
# it should say how many roots there are and give the roots.
# But only if the roots are real of course.
# You DO NOT need to use DEF but it would be really cool if you did.
print("The Quadratic Equation is ax^2+bx+c=0")
a = int(input("Please give me the 'a' of a Quadratic Equation: "))
b = int(input("Please give me the 'b' of a Quadratic Equation: "))
c = int(input("Please give me the 'c' of a Quadratic Equation: "))
#Gain the value of a, b and c.

delta = (b**2) - (4*a*c) # Calculate the value of delta.
def QuadraticEquation1(a,b,c):
    rootsformula1 = ((-b)+(((b**2)-(4*a*c))**0.5))/(2*a)
    rootsformula2 = ((-b)-(((b**2)-(4*a*c))**0.5))/(2*a)
    print("The first real root is: ",rootsformula1)
    print("The second real root is: ",rootsformula2)
def QudraticEquation2(a,b,c):
    rootsformula = (-b)/(2*a)
    print("The two equal real roots is: ",rootsformula)

# Define two solutions to solve 2 situation.

if delta > 0:
    print("The Quadratic Equation has two unequal real roots.")
    QuadraticEquation1(a,b,c)
elif delta < 0:
    print("The Quadratic Equation do not have real roots.")
else:
    print("The Quadratic Equation has two equal real roots.")
    QudraticEquation2(a, b, c)

#Different situation use different method and use the functions I have defined to calculate and print.

quit()
