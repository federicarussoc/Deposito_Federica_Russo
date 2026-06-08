#esercizi cicli

#1
ripetere = "s" #imposto ripetere su "sì"
while ripetere == "s": #finchè l'utente vuole ripetere
    num = int(input("Inserisci un numero intero: ")) #chiedo all'utente di inserire un numero
    while num >= 0: #finchè il numero è maggiore o uguale a zero:
        print(num) #stampo il numero
        num -= 1   #il numero si riduce di 1
    ripetere = input("Vuoi ripetere? (s/n): ") #chiudo all'utente se vuole continuare

#2

pari_trovati = 0 #il contatore dei nuperi pari è uguale a 0
while pari_trovati < 5: #finchè il contatore dei pari è inferiore a 5
    n = int(input("Inserire un numero intero: ")) #chiedo all'utente di inserire un numero
    if n % 2 == 0: #se il numero è pari
        print("Il numero è pari") #stampo che è pari
        pari_trovati += 1 #il contatore dei pari aumenta di 1
    else:
        print("Il numero non è pari") #se il numero non è pari stampo che non lo è
    