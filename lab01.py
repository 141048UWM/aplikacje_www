
#_1
napis = "Czym jest Lorem Ipsum?"
print(napis)
#_2
litera = 0

tabela = {}
for char in napis:
    char = char.lower()
    if char in tabela:
        tabela[char] += 1
    else:
        tabela[char] = 1

print(napis, "ilość:", tabela)

#_3
class Data(object):

    def __repr__(self):
        return 'räpr'
print('{0!r} {0!a}'.format(Data()))

print('{:>14}'.format('test'))

print('{:^10}'.format('test'))

print('{:_<10}'.format('test'))

#_4


zmienna_typu_string="Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w"

print(dir(zmienna_typu_string))
help(zmienna_typu_string.capitalize())

#_5

osoba = 'Jan Kowalski'[::-1]
osoba = osoba.lower() and osoba.capitalize()
osoba[:-1].upper()

print(osoba)


#_6

lista = list((range(1,11)))
print (lista,"lista przed podzialem")

lista2 = lista[5:]
lista = lista[:5]
print (lista, "lista po podziale")
print(lista2,"druga lista")

lista3=lista+lista2
#_7
lista3.insert(0, 0)

lista3_copy=lista3

print(lista3)

lista3_copy.sort(reverse=True)

print(lista3_copy)

#_8

krotka = ('1', ('Kazimierz', "Zawadzki"),
        '2', ('Przemysław', "Lewandowski"),
        '3', ('Damian', "Damian"),
        '4', ('Bolesław', "Jaworski"),
        '5', ('Alojzy', "Maxymus"),
        '6', ('Alex', "Dopałka"),
        '7', ('Mieszko', "Drugi"),
        '8', ('Dariusz', "Sznut"),
        '9', ('Lucjan', "Poprawny"),
        '10', ('Jędrzej', "Florian"),
        '11', ('Heronim', "Chrobry"),
        '12', ('Ireneusz', "Poniatowski"),)


#_10
lista4 = [432432423, 876567876, 367543456,787654345,986756454,876543245,367543456,324324293, 876567876]
print(lista4)

lista4 = set(lista4)

print(lista4)
#_11
lista5=list(range(1,10))
#_12
lista6=list(range(100,19,-5))
print(lista5)
print(lista6)
#_13
dict = {'id_1': 'napis1', 'id_2': 'napis2', 'id_3':'napis3'}
dict2 = {'id_4': 'napis4', 'id_5': 'napis5', 'id_6':'napis6'}
dict3 = {'id_7': 'napis7', 'id_8': 'napis8', 'id_9':'napis9'}
dict4 = {'id_10': 'napis10', 'id_11': 'napis11', 'id_12':'napis12'}
lista7 = [
    dict,dict2, dict3, dict4
]

for item in lista7:
    print("id:", item.keys(), "values: ", item.values())