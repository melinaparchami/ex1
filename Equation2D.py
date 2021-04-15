import math


def Equation2D(a, b, c):
    delta = b*b - 4*a*c
    if delta == 0:
        return 'The equation has one root. Root = {}'.format(-b/(2*a))
    if delta > 0:
        root_1 =  (-b+(delta**0.5))/(2*a)
        root_2 = (-b-(delta**0.5))/(2*a)
        return 'The equation has two roots. Root_1 = {} , Root_2 = {}'.format(root_1, root_2)


print(Equation2D(2, 5, 3))

