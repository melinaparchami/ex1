import  math
import Swap


def Area(a, b, c, d):
    if d == 0:
        p = (a + b + c)/2
        return (p * (p-a) * (p-b) * (p-c))**(0.5)

def AreaX(a, b, c, d):
    sides = [a, b, c, d]
    for i in range(len(sides)):
        if sides[i] == 0:
            sides.remove(sides[i])
            return Area(sides[0], sides[1], sides[2], 0)


print(Area(8, 5, 7, 2))

print(AreaX(8, 5, 0, 2))
