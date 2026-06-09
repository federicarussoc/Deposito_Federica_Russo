#esercitazione 
#macro while
#faccio inserire un valore positivo (secondo while) se non inserisce un valor epositivo non lo faccio uscire
# a quel punto faccio gli esercizi su n
#poi gli chiedo se vuole ripetere di nuovo

ripeti = "s"
while ripeti == "s":
    n = int(input("Inserire un numero intero positivo: "))
    while n <= 0:
        n = int(input("Sbagliato, inserire un numero intero positivo: "))
    
    #es 1
    somma = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            somma += i
    print("Somma dei numeri pari: ", somma)

    #es 2
    for i in range(1,n+1):
        if i % 2 != 0:
            print(i)
    
    #es 3
    if n == 1: #caso particolare, 1 non è numero primo
        print("Non è primo")
    else:
        #imposto flag a True e cerco l'eccezione
        flag = True
        #per ogni numero che precede n (da 2 a n-1 perchè già sapiamo che n si può dividere per 1 e se stesso, qualunque sia n)
        for i in range(2, n): #si potrebbe anche fare: range(2, int(n**0.5) + 1)
            if n % i == 0: #se n è divisibile per i allora vuol dire che non è primo e la flag diventa false
                flag = False
        #terminato il ciclo stampo il risultato rispetto allo stato della flag (se è True o False)
        if flag:
            print("È primo")
        else:
            print("Non è primo")
    
    #chiedo se si vuole ricominciare

    ripeti = input("Vuoi ripetere di nuovo? (s/n) ").lower()
    


##extra rifarlo con una lista

ripeti = "s"

while ripeti == "s":

    #creo la lista
    lunghezza = int(input("Quanti numeri vuoi inserire? "))
    lista = []

    for i in range(lunghezza):
        n = int(input("Inserisci un numero intero: "))
        lista.append(n)

    #per ogni elemento della lista ripeto gli esercizi
    for n in lista:

        print("Analizzo il numero:", n)

        if n <= 0:
            print("Numero non valido")
            continue

        #es1
        somma = 0

        for i in range(1, n + 1):
            if i % 2 == 0:
                somma += i

        print("Somma dei numeri pari:", somma)

        #es2
        print("Numeri dispari:")

        for i in range(1, n + 1):
            if i % 2 != 0:
                print(i)

        #es3
        if n == 1:
            print("Non è primo")

        else:
            flag = True

            for i in range(2, n):
                if n % i == 0:
                    flag = False

            if flag:
                print("È primo")
            else:
                print("Non è primo")

    #chiedo se si vuole ricominciare
    ripeti = input("Vuoi ripetere di nuovo? (s/n) ").lower()