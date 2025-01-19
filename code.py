#кролик
n = int(input()) #стоимость одного пакетика
s = int(input()) #площадь огорода (м**2)
res = n*s
print(res)

#пятачок
n = input() #номер билета
n1 = n[0:3]
n2 = n[3:]
s1 = 0
s2 = 0
for i in n1:
    s1+=int(i)
for i in n2:
    s2+=int(i)
if s1 == s2:
    print('достался')

#винни пух
n1 = int(input()) #мед
n2 = int(input()) #сгущека
n3 = int(input()) #варенье
p = int(input()) #толстение
m = int(input()) #вес
m2 = int(input()) #набор веса
t0 = 0 #часы чая
t = 15 #часы
n = n1 + n2 + n3

while n > 0:
    if t0 < t:
        n-=0.5
        m+=m2
        t0+=0.25    
    else:
        print('нет')
if m < m+m*(p/100):
    print('да')
else:
    print('нет')

    


     
    