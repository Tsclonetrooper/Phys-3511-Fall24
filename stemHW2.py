import math
import cmath
#aloysia Black
print()


#1
print('#1')
print()
print('========EVEN==========')
for i in range(351):
    if i %2 == 0:
        print(i)


print('========ODD==========')
for i in range(351):
    if i %2 != 0:
        print(i)



print()
print()

#2
print('#2')


def roots(a, b, c):
    number = b**2 - 4*a*c

    if number > 0:
        root1 = (-b + cmath.sqrt(number)) / (2*a)
        root2 = (-b - cmath.sqrt(number)) / (2*a)
        nature = "real and distinct"
    elif number == 0:
        root1 = root2 = -b / (2*a)
        nature = "real and equal"
    else:
        root1 = (-b + cmath.sqrt(number)) / (2*a)
        root2 = (-b - cmath.sqrt(number)) / (2*a)
        nature = "complex"

    return nature, root1, root2

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))


nature, root1, root2 = roots(a, b, c)

print(f"These roots are: {nature}")
print(f"The roots are: {root1} and {root2}")

print()
print()

#3
print('#3')

def newton(m,a):
    return(m*a)

#m0 = input('Enter mass in Kg: ')
a = 9.8 #m/s^2

force_list = []
i = 1
while i < 201:
    force = newton(i,a)
    force_list.append(force)
    i += 1

print(force_list)