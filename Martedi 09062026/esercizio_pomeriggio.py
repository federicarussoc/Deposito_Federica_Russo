##ESERCITAZIONE

#1: Chiedere un numero intero positivo
import random

def chiedi_numero():
    n = int(input("Inserisci un numero intero positivo: "))

    while n <= 0:
        n = int(input("Errore. Inserisci un numero intero positivo: "))

    return n


#2: Generare numeri casuali con un generatore
def genera_numeri(n):
    for i in range(n):
        yield random.randint(1, n)


def lista_numeri_casuali(lunghezza):
    lista = list(genera_numeri(lunghezza))
    return lista


#3: Somma dei numeri pari
def somma_pari(lista):
    somma = 0

    for numero in lista:
        if numero % 2 == 0:
            somma += numero

    print("Somma dei numeri pari:", somma)


#4: Stampare i numeri dispari
def stampa_dispari(lista):
    print("Numeri dispari:")

    for numero in lista:
        if numero % 2 != 0:
            print(numero)


#5: Controllare se un numero è primo
def isPrimo(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


#6: Stampare tutti i numeri primi nella lista
def stampa_primi(lista):
    print("Numeri primi:")

    for numero in lista:
        if isPrimo(numero):
            print(numero)


#7: Controllare se la somma totale è un numero primo
def somma_totale_prima(lista):
    somma = 0

    for numero in lista:
        somma += numero

    if isPrimo(somma):
        print("La somma totale", somma, "è un numero primo")
    else:
        print("La somma totale", somma, "non è un numero primo")


#8: Menu
def menu(lista):
    scelta = "" #inizzializzo scelta come stringa vuota, mi serve a memorizzare la scelta dell'utente

    while scelta != "0": #finchè l'utente non sceglie di uscire:
        print("\n--- MENU ---") #stampo il menu delle opzioni
        print("1 - Somma dei numeri pari")
        print("2 - Stampa numeri dispari")
        print("3 - Stampa numeri primi")
        print("4 - Controlla se la somma totale è prima")
        print("0 - Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            somma_pari(lista)
        elif scelta == "2":
            stampa_dispari(lista)
        elif scelta == "3":
            stampa_primi(lista)
        elif scelta == "4":
            somma_totale_prima(lista)
        elif scelta == "0":
            print("Programma terminato.")
        else:
            print("Scelta non valida.")


#programma principale
n = chiedi_numero()
lista = lista_numeri_casuali(n)

print("Lista generata:", lista)

menu(lista)

