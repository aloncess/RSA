import random
#Нахождение НОДа чисел по алгоритму Евклида
def nodEvklid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

#Функции нахождения обратного числа по модулю с помощью расширенного алгоритма Евклида
def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def invEl(module, a):
    gcd, x, y = gcdExtended(a, module)
    return (x % module + module) % module


#Проверка числа на простоту
def prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a

#Функция Эйлера
def FuncEyler(p, q):
    return (p-1)*(q-1)

#Нахождения числа N
def resN(p, q):
    return p*q

#Нахождение экспоненты шифрования
def e(p, q):
    z = 2
    while 1:
        if nodEvklid(z, FuncEyler(p, q)) == 1 and nodEvklid(z, resN(p, q)) == 1:
            return z
        z+=1

#Нахождение экспоненты дешифрования
def d(Eyler, e):
    return invEl(Eyler, e)

#Генерация публичного и приватного ключей
def keys(p, q):
    EncrExp = e(p, q)
    Eyler = FuncEyler(p, q)
    Decr = d(Eyler, EncrExp)
    N = resN(p, q)
    public = [EncrExp, N]
    private = [Decr, N]
    return public, private

#Шифрование
def enc(info, public):
    e = public[0]
    N = public[1]
    unichars = [ord(i) for i in info]
    newchars = []
    unicodelen = 1114111
    for i in unichars:
        newchars.append( ((i ** e) % N) % unicodelen )
    output = ''
    for i in newchars:
        output += chr(i)
    return output

#Дешифрование
def dec(info, private):
    d = private[0]
    N = private[1]
    unichars = [ord(i) for i in info]
    newchars = []
    unicodelen = 1114111
    for i in unichars:
        newchars.append(((i ** d) % N) % unicodelen)
    output = ''
    for i in newchars:
        output += chr(i)
    return output

# Интерфейс
act = input('1 - Шифрование; 2 - Дешифрование\n')
if act == '1':
    todo = input('1 - Сгенерировать p и q; 2 - Ввести вручную\n')
    if todo == '1':
        while 1:
            p = random.randint(1, 1000000)
            if prime(p) == 1:
                break
        while 1:
            q = random.randint(1, 1000000)
            if prime(q) == 1:
                break
    else:
        p = int(input('p: '))
        q = int(input('q: '))
    KeySchedule = keys(p, q)
    public = KeySchedule[0]
    private = KeySchedule[1]
    print('Public: ' + str(public[0]) + '; ' + str(public[1]))
    print('Private: ' + str(private[0]) + '; ' + str(private[1]))
    info = input('Введите информацию для шифрования: ')
    encr = enc(info, public)
    print('Результат шифрования: ' + encr)
    file = open('RSA', 'w', encoding='utf-8')
    file.write(encr)
    file.close()
elif act == '2':
    private = list(map(int, input('Введите private-key: ').split()))
    filename = input('Введите название файла с заширфованным сообщением: ')
    file = open(filename, 'r', encoding='utf-8')
    info = file.readline()
    file.close()
    decr = dec(info, private)
    print('Результат дешифрования: ' + decr)
    file = open('RSA', 'w', encoding='utf-8')
    file.write(decr)
    file.close()