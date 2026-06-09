##LISTE 

#Le liste sono collezioni di dati, caratterizzate da: modificabilità, ordine, eterogenità. 
#Sono indicizzate a partire da 0

#TUPLE
#Simili alle liste, ma con una differenza: sono immutabili
#Sono rappresentato dal tipo di dato tuple e sono racchiuse tra parentesi tonde ()
#Sono indicizzate come le liste

#INSIEMI
#Gli insiemi (set) sono una collezione di dati non ordinata e senza duplicati 

#Controllo del flusso
#Logica grazie alla quale possiamo ripetere o escludere parti del codice dalla lettura. 
#Si dividono in due famiglie: CICLI (while e for) e CONDIZIONI (if, match)

#IF
#La condizione if viene utilizzata per eseguire una parte di codice se una determinata condizione è vera
#L'istruzione else viene usata per definire un blocco di codice da eseguire se le condizioni precedenti risultano false.
#Si può utilizzare anche elif (deve essere più inclusivo dell'if)
#es. non posso fare un:
if numero > 0:
    print("numero maggiore di 0")
elif numero > 2: #la seconda condizione è inclusa nella prima
    print("numero maggiore di 2")

         

##esercizio 1

nome = input("Inserisci il nome: ")

if nome == "Federica":
    password = input("Inserisci la password: ")

    if password == "123":
        codice = input("Inserisci il codice di sicurezza: ")

        if codice == "ABC":
            print("Accesso consentito")
        else:
            print("Codice errato")
    else:
        print("Password errata")
else:
    print("Utente non riconosciuto")

##esercizio 2

scelta = int(input("Scegli un numero tra: 1-Aggiungi, 2-Modifica, 3-Elimina "))

if scelta == 1:
    print("Aggiungi")
elif scelta == 2:
    print("Modifica")
elif scelta == 3:
    print("Elimina")
else:
    print("Scelta non valida")

##esercizio 3

utente_presente = False
ultimo_id = 100

if utente_presente == False: #se l'utente non è presente creo l'account
    nome = input("Nome: ")
    password = input("Password: ")

    ultimo_id += 1  #incremento
    id_utente = ultimo_id

    print("Account creato")
    print("ID assegnato:", id_utente)

else: #se è presente
    print("Account già presente nel sistema")


#MATCH
#confronta un input con vari casi, eseguendo un blocco specifico di codice quando trova una corrispondenza
#serve a evitare di avere un if con tanti elif

comando = input("Inserisci un comando: ") #inserisco un comando in input

match comando: #verifico se il comando corrisponde a uno dei seguenti casi, python valuta il valore della variabile comando
    case "start":
        print("Avvio del programma")
    case "stop":
        print("Chiusura del programma")
    case "pausa":
        print("Programma in pausa")
    case _:  #default: se non trovo corrispondenze il codice associato a questo caso viene eseguito (è come l'else)
        print("Comando non riconosciuto")

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

##WHILE 
#i cicli controllano se e quando viene ripetuta una parte di codice. 
conteggio = 0
while conteggio < 5: #finchè il conteggio è inferiore a 5 ripeti il codice
    print(conteggio)
    conteggio += 1
#questo è detto ciclo matematico, è inutile
#il vero significato del while è ripetere in maniera indefinita
#il ciclo booleano è così, ed è uno dei più importanti. 

controllore: True 
while controllore: #finchè controllore è True ripeto il seguente codice
    print("ciao")  #cioè continuo a stampare ciao

    scelta = input("vuoi continuare?") #poi chiedo all'utente se vuole continuare
    if scelta == "no":  #se non vuole continuare:
        controllore = False #controllore diventa falso e quindi il ciclo si interrompe

#il while si usa quando non sai o non puoi o non vuoi definire quante volte si deve ripetere
#per tutti i contesti indefiniti
#il for, invece, si usa per tutti i contesti definiti o definibili
#il for si compone in due modi: un elemento, una sequenza. 
#può essere usato sia con elementi numerici sia per collezioni o su un oggetto iterabile

#for elemento in sequenza:
    #blocco di codice iterato

#eelemento è una variabile che rappresenta l'elemento corrente della sequenza in ogni iterazione.
#sequenza è una sequenza di elementi su cui si desidera iterare, come una lista, una stringa o l'output della funzione range().

numeri = [1,2,3,4,5] #creo una lista di numeri
for numero in numeri: #per ogni numero presente nella lista numeri
    print(numero) #stampa il numero corrente

#range() è una funzione incorporata di python che restituisce una sequenza di numeri interi che possono essere utilizzati in cicli for o 
# in altre situazioni in cui è necessario iterate su un insieme di valori.

#è composto da 3 parti: start (opzionale), stop, step (opzionale)
#start: il valore di partenza della sequenza. se omesso il valore di default è 0.
#stop: il valore di fine della sequenza, non è incluso nela sequenza generata.
#step: la differenza tra i valori successivi nella sequenza. se omesso, il valore predefinito è 1. sono i passi. 

for i in range(5): #questo ciclo stampa i numeri da 0 a 4, poichè range(5) genera una sequenza di valori da 0 a 4 (0 incluso, 5 escluso)
    print(i)

for i in range(2,8): #stampa i numeri da 2 a 7, 2 incluso 8 escluso
    print(i)

for i in range(1,10,2): #stampa i numeri dispari da 1 a 9, poichè range genera una sequenza di valori da 1 a 9 con passo 2 (1 incluso, 10 escluso)
    print(i)



