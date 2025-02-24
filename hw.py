def a(n=0, s = 0, p = 1):
    for i in range(100, 1000):
        if i%17 == 0 and i%10 == 3:
            n+=1
            s+=i
            p*=i
    return {'a':s, 'б': n, 'в':p}
def b(n=0, s = 0, p = 1):
    for i in range(100, 1000):
        if ((i%10)+((i//10)%10)+(i//100)%10)%2 == 0:
            n+=1
            s+=i
            p*=i
    return {'a':s, 'б':n, 'в':p}
q = input('a/б:')
if q == 'a':
    print(f'result:{a()}')
else:
    print(f'result:{b()}')

