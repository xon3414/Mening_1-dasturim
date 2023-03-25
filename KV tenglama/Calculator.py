import math

#Kvadrat tenglama xisoblovchi dastur
print("ax^2+bx+c=0")
def dis():
    a = int(input("'a' ga raqam kiriting: "))
    b = int(input("'b' ga raqam kiriting: "))
    c = int(input("'c' ga raqam kiriting: "))

    D = b**2-4*a*c
    print("D =", D)
    X1 = (-b + pow(D, 0.5))/(2*a)
    print("X1 =", X1)
    X2 = (-b - pow(D, 0.5))/(2*a)
    print("X2 =", X2)
dis()
while True:
    flag = input("repeat [Y/n]")

    if flag == 'Y':
        dis()
    elif flag == 'n':
        break

