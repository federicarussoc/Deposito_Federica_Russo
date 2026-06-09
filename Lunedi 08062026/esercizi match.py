#esercizi match

##esercizio 1

eta = int(input("Inserire la propria età: ")) #inserisco l'età come input

match eta: #verifico se l'età corrisponde ad uno dei due casi possibili
    case x if x >= 18: #per fare confronti logici devo: prendere il valore di eta, chiamarlo x, usare questo caso solo se x >= 18
        print("Puoi vedere questo film")
    case _: #se non corrisponde al primo caso, allora questo codice viene eseguito
        print("Mi dispiace, non puoi vedere questo film")

##esercizio 2

num1 = float(input("Inserisci il primo numero: ")) #primo numero
num2 = float(input("Inserisci il secondo numero: ")) #secondo numero
operazione = input("Inserisci l'operazione (+, -, *, /): ") #operazione (come stringa)

match operazione: #faccio il match su operazione, perchè da questa dipende cosa printo
    case "+": #se è +, -, * non ci sono problemi, printo il risultato dell'operazione corrispondente (che ha trovato il match)
        print("Risultato:", num1 + num2)
    case "-":
        print("Risultato:", num1 - num2)
    case "*":
        print("Risultato:", num1 * num2)
    case "/": #se l'operazione è /, devo fare attenzione al secondo numero (il denominatore)
        if num2 == 0: #se il denominatore è uguale a 0, non posso restituire una soluzione e printo errore
            print("Errore: Divisione per zero")
        else:
            print("Risultato", num1 / num2)
    case _: #se viene inserito un valore errato per l'operazione allora printo errore
        print("Operazione non valida")