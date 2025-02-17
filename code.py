import math
#ticket
n = input('ticket')
lst1 = [int(i) for i in n[0:3]]
lst2 = [int(i) for i in n[3:]]
print(sum(lst1)==sum(lst2))

#point a

print(float(input('y'))<1)

#point б
x = float(input('x'))
y = float(input('y'))
if x < 0 and y < 0:
    print(True)
elif x < 0 and y > 0:
    print(y<x*-1)
elif x > 0 and y < 0:
    print(y*-1>x)
else:
    print(False)


#point в
x = float(input('x'))
y = float(input('y'))
print(x<1 and x>-1 and y<1 and y>-1)

#point д
x = float(input('x'))
y = float(input('y'))
if x > 0 and y > 0:
    if (x**2 + y**2) > 4:
        if y < x and x < 2:
            print(True)
        else:
            print(False)
    else:
        print(False)
else:
    print(False)


#point г
x = float(input('x'))
y = float(input('y'))
print((x**2)+(y**2)>4 and x<2 and x > 0 and y<2 and y>0)

#point ж
x = float(input('x'))
y = float(input('y'))
n = math.sqrt(2)
if x < 0 and y > 0:
    if y < 2-x**2:
        print(True)
elif y < 0 and x < 0:
    if y > x and y < 2-x**2:
        print(True)

if x <= 0 and x > n*-1:
    if y < 2-x**2 and y > x:
        print(True)
elif x > 0 and x < n:
    if y < 2-x**2 and y > 0:
        print(True)
else:
    print(False)

#point e
x = float(input('x'))
y = float(input('y'))
print(y>0 and x>0 and y<0.5 and y<math.sin((x*math.pi)/180))



