def fun1(mot):
    newMot = ''
    for i in range(len(mot)):
        newMot += 'a'
    newListMot = list(newMot)
    for i in reversed(list(range(len(newMot)))):
        newListMot[i] = mot[len(mot) - 1 - i]
    return ''.join(newListMot)

def fun2(mot):
    newListMot = []
    for i in mot:
        newListMot.append(ord(i) + 13)
    return newListMot

def fun3(liste):
    xorWord = 42
    newListMot = []
    for i in liste:
        newListMot.append(i ^ xorWord)
    return ' '.join(map(str, newListMot))
    
#flag = input('Flag : ')
#print(fun1(flag))
#print(fun2(fun1(flag)))
#print(fun3(fun2(fun1(flag))))


a="160 172 104 107 106 70 104 20 70 126 81 20 85 106 106 81 20 126 81 106 70 106 104 85 106 169 106 117 162 122 113 113 120 119 118"

la = a.split(" ")
print(la)
lb = []
for i in la:
    lb.append(int(i))
b = fun3(lb)
print(type(b))

def fun4(la):
    newListMot = []
    for i in la.split(" "):
        print(i)
        newListMot.append(chr(int(i)-13))
    return newListMot

print(fun1(fun4(b)))
