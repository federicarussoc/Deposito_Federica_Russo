#CIAO UTENTE, QUALE ESERCIZIO VUOI USARE? 1/2/3? dentro un while
#QUANTO NUMERI VUOI INSERIRE? X RANGE(X)

#esercizio 1
n1 = int(input("Inserisci un numero intero: ")) #chiedo di inserire un numero intero in input
if n1 % 2 == 0: #se il numero è divisibile per 2 è pari
    print("Pari") #quindi stampo se è pari
else: #in tutti gli altri casi il numero è dispari 
    print("Dispari") #quindi stampo che è dispari

#esercizio 2
n2 = int(input("Inserisci un numero intero positivo: ")) #chiedo di inserire un numero intero positivo in input
while n2 >= 0: #finchè il numero rimane maggiore o uguale a zero
    print(n2)  #stampo il numero
    n2 -= 1    #decremento il numero di una unità e ripeto finchè la condizione del while è falsa

#esercizio 3
lunghezza = int(input("Quanti numeri vuoi inserire? ")) #chiedo la lunghezza della lista di numeri
lista = [] #creo una lista vuota

for i in range(lunghezza): #per ogni posizione vuota della lista 
    n3 = int(input("Inserisci un numero intero: ")) 
    lista.append(n3) #la popolo con un numero dato in input dall'utente
for j in lista: #per ogni elemento della lista appena popolata
    print(j**2) #stampo il quadrato


#unire i tre esercizi precedenti

flag = True #inizializzo la flag a True

while flag: #finchè la flag rimane True
    es = input("Quale esercizio vuoi usare? (x per uscire)") #chiedo quale esercizio l'utente vuole svolgere
    match es: #cerco la corrispondenza tra la risposta e l'esercizio
        case "1":
            n1 = int(input("Inserisci un numero intero: "))
            if n1 % 2 == 0:
                print("Pari")
            else:
                print("Dispari")

        case "2":
            n2 = int(input("Inserisci un numero intero positivo: "))
            while n2 >= 0:
                print(n2)
                n2 -= 1


        case "3":
            lunghezza = int(input("Quanti numeri vuoi inserire? "))
            lista = []
            for i in range(lunghezza):
                n3 = int(input("Inserisci un numero intero: "))
                lista.append(n3)
            for j in lista:
                print(j**2)
        
        case "x": #se l'utente vuole uscire la flag diventa False e il ciclo while si ferma
            flag = False

#esercizio 4
#punto 1
lunghezza = int(input("Quanti numeri vuoi inserire? "))
lista = []
for i in range(lunghezza):
    n = int(input("Inserisci un numero intero: "))
    lista.append(n)

massimo = lista[0]
for i in lista:
    if i > massimo:
        massimo = i
print("Il numero massimo è: ", massimo)

#punto 2

contatore = 0
indice = 0

while indice <=








