import math

x = int(input("dividers of "))
z = 1
nombre = 0
numerals = [1]
numerals.pop(0)
s_x = math.sqrt(x)

while True:
    if z <= s_x:
        if x % z == 0:
            numerals.append(int(x / z))
            numerals.append(z)
            z += 1
            nombre += 2
            if (100 * z) / s_x < 101:
                print("{} %".format(int((100 * z) / s_x)))
            else:
                continue
        else:
            z += 1
            if (100 * z) / s_x < 101:
                print("{} %".format(int((100 * z) / s_x)))
            else:
                continue
    else:
        numerals.sort()
        num = str(numerals)[1:-1]
        print("There are {} dividers".format(nombre))
        print("The factors of {1} are {0} ".format(num, x))
        quit()
