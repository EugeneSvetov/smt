e = float(input('Вставьте разницу '))
a = int(input('Вставьте начало интервала '))
b = int(input('Вставьте конец интервала '))
n = 0


def function(x):
    return x ** 3 + x ** 2 - 1


while (b - a) >= e:
    xc = (a + b) / 2
    if function(xc) * function(a) < 0:
        b = xc
        n += 1
        print(f'Действие {n} : [{a};{b}]')

    if function(xc) * function(b) < 0:
        a = xc
        n += 1
        print(f'Действие {n} : [{a};{b}]')
