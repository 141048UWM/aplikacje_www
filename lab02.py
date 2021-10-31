def funkcja(a_list, b_list):
    lista = a_list+b_list
    a_list=[]
    b_list=[]
    for i in lista:
        if i % 2 == 0:
            a_list.append(i)
        else:
            b_list.append(i)
    return a_list, b_list


print(funkcja((2,43,43,24,32,42,34,23,4,23,4),(3,4,3,34,23,4,234,2,34,23,4,23,4)))

def funkcja2(data_text):
    lista = []
    for i in data_text:
        lista.append(i)
    lista2 = []
    for i in data_text:
        if i == i.upper():
            lista2.append(i)
    lista3 = []
    for i in data_text:
        if i == i.lower():
            lista3.append(i)
    slownik = {
        'Length': len(data_text),
        'letters': lista,
        'big_letters': lista2,
        'small_letters': lista3,
    }
    return slownik
print(funkcja2("iofdsjoFDSFDFSDsjdoifdjoif"))

def funkcja3(text, letter):
    c = []
    h = []
    for g in text:
        if letter == g:
            c.append(letter)
        else:
            h.append(g)

    return c, h

print(funkcja3("apartment", 'a'))


def funkcja4(cel, **opcje):
    if opcje.get("far")=="far":
        print(cel,"stopni celsiusza to: ",2*cel + 32," stopni farenheita")
    if opcje.get("kel")=="kel":
        print(cel,"stopni celsiusza to: ",cel+273.15," stopni kelvina")
    if opcje.get("ran")=="ran":
        print(cel,"stopni celsiusza to: ",cel+273.15*9/5," stopni Rankina")

funkcja4(20, ran="ran")

class Calculator:
    def add(self, a,b):
        dodaj = a+b
        print(dodaj)
    def multiply(self, a,b):
        pomnoz = a*b
        print(dodaj)
    def odejmij(self, a,b):
        odejmij_ = a-b
        print(odejmij_)
    def divide(self, a,b):
        dziel = a/b
        print(dziel)

wynik = Calculator()
wynik.add(3,5)

class ScienceCalculator(Calculator):
    def potega(self, a, b):
        potega_ = a**b
        print(potega_)


wynik2 = ScienceCalculator()
wynik2.potega(2,3)


def Reverse(text):
    temp = text
    lista = []
    for i in text:
        lista.append(i)
    print(lista)
    lista.reverse()
    for i in lista:
        print(i.lower(), end="")

Reverse("Koteł")