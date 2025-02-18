#разбиение выражения на коэфициэнты
def spl(n):
    n = n[0:-2].split('+')
    a, b, c = int(n[0].split('x')[0]), int(n[1].split('x')[0]), int(n[2])
    return (a,b,c)