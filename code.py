#квадратное уравниение
import math
from code2 import spl

#ввод уравнения
n = input('запишите уравнение в стандартном виде(ax^2+bx+c=0, если a, b или с равны 0 запишите их как 0):\n')

#присваивание значений коэфициэнтов
a,b,c = spl(n)

D = (b**2)-(4*a*c)
if D >= 0:
    #стандартный вид
    if [a, b, c] != [0, 0, 0]:
        #сумма к. равна 0
        if (a+b+c) == 0:
            x1 = 1
            x2 = c/a
            print(set((x1, x2)))
        #сумма крайних к. равна среднему к.
        elif (a+c) == b:
            x1 = -1
            x2 = (-1)*(c/a)
            print(set((x1, x2)))
        #D=0
        elif D == 0:
            x1 = (b*(-1))/(2*a)
            print({x1})
        #b четный
        elif b%2 == 0:
            D = ((b//2)**2) - (a*c)
            x1 = ((-1)*(b//2) + math.sqrt(D))/a
            x2 = ((-1)*(b//2) - math.sqrt(D))/a
            print(set((x1, x2)))
        #общий случай
        else:
            x1 = ((-1)*b + math.sqrt(D))/(2*a)
            x2 = ((-1)*b - math.sqrt(D))/(2*a)
            print(set((x1, x2)))
    #a,b,c = 0,0,0
    elif [a,b,c] == [0,0,0]:
        print('x ∈ R')
    #a,b,c = 0, not0, not 0
    elif a == 0 and b != 0 and c != 0:
        x = (-1*c)/b
        print({x})
    #a,b,c = not 0, 0, not 0
    elif a != 0 and b == 0 and c != 0:
        x1 = (math.sqrt((-1*c)/a))
        x2 = -1*(math.sqrt((-1*c)/a))
        print(set((x1, x2)))
    #a,b,c = not 0, not 0, 0
    elif a != 0 and b != 0 and c == 0:
        x1 = 0
        x2 = (-1*b)/a
        print(set((x1, x2)))
    #a,b,c = 0,0,not 0
    elif a == 0 and b == 0 and c != 0:
        print({})
    #a,b,c = not 0, 0, 0
    elif a != 0 and b == 0 and c == 0:
        print({0})
    #a,b,c = 0, not 0, 0
    elif a == 0 and b != 0 and c == 0:
        print({0})
else:
    print({})

    




