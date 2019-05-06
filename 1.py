def pobierz_dane (liczba_cyfr):
    lista=[]
    for i in range (liczba_cyfr):
        dodaj = input()
        lista.append(dodaj)
    return lista
print("Podaj ile liczb ma się znaleźć w liśćie")

ile=int(input())


print(pobierz_dane(ile))
