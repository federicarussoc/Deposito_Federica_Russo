# Scrivere un programma che permetta all'utente di gestire i propri esami universitari. 
# in particolare il programma deve permettere di: 
# registrare esame superato, 
# visualizzare esami sostenuti, 
# cercare un esame, 
# calcolare media voti, 
# uscire dal programma. 

##################################################################################################################

## PRIMO STEP: SCRIVERE LE SINGOLE FUNZIONI

# registrare un esame superato
# per farlo uso le liste
# matricola = []
# esami = []
# voti = []
# in cui ogni posizione rappresenta una registrazione

matricole = []
esami = []
voti = []

def registerExam():
    #chiedo all'utente di inserire le informazioni necessarie alla registrazione
    m = input("Inserire codice matricola: ") 
    e = input("Inserire nome esame: ")
    v = int(input("Inserire voto: "))
    #le inserisco nelle rispettive liste
    matricole.append(m)
    esami.append(e)
    voti.append(v)
    #stampo messaggio di conferma
    print("Esame registrato con successo!")

# visualizzare esami sostenuti
# devo cercare le corrispondenze tra matricola e esami usando la posizione
# per prima cosa creo una funzione che registra la posizione di una determinata matricola e restituisce l'esame e il voto corrispondenti 
# uso yield per creare un generatore che scorre le liste e restituisce esame e voto associati alla matricola

def generateExams(m):
    for i in range(len(matricole)):
        if matricole[i] == m:
            yield esami[i], voti[i]

# la funzione showExams() prende in input la matricola digitata dall'utente e chiede alla funzione generateExams di restituire uno ad uno gli esami e voti corrispondenti
# e li stampa uno a uno, se non ha trovato corrispondenze con la matricola stampa un messaggio di errore

def showExams():
    m = input("Inserire codice matricola: ")
    trovato = False
    for esame, voto in generateExams(m):
        print("Esame:", esame, "- Voto:", voto)
        trovato = True
    if not trovato:
        print("Matricola non trovata")

# cercare un esame
# l'utente inserisce matricola e nome esame, la funzione verifica se estste una registrazione corrispondente

# la funzione searchExams() prende in input matricola e nome esame digitati dall'utente e verifica se sono presenti nelle rispettive liste
# e se le posizioni corrispondono

def searchExam():
    m = input("Inserire codice matricola: ")
    e = input("Inserire nome esame: ")
    trovato = False
    for i in range(len(matricole)):
        if matricole[i] == m and esami[i] == e: 
            print("Esame presente nella lista")
            trovato = True
            break #se la corrispondenza viene trovata interrompiamo il ciclo for perchè non ha senso continuare a scorrere le liste
    if not trovato:
        print("Esame non presente nella lista")

# calcolare media voti
# la funzione prende in input la matricola, crea una lista vuota dove conservare i voti di quell'utente
# scorrendo la lista matricole cerca per ogni posizione della matricola inserita, un corrispondente in voti
# ogni volta che lo trova lo inserisce nella lista vuota con append()

from statistics import mean
def meanExam():
    m = input("Inserire codice matricola: ")
    trovato = False
    votiUtente = []
    for i in range(len(matricole)):
        if matricole[i] == m:
            votiUtente.append(voti[i])
            trovato = True
    if not trovato: #se non ci sono corrispondenze con la matricola allora stampa un messaggio di errore
        print("Matricola non trovata")
    else:           # altrimenti calcola la media dei valori contenuti nella lista 
        media = mean(votiUtente)
        print("La media dei voti è: ", media)

## SECONDO STEP: MENU

# creare un menu che permette all'utente di scegliere tra le varie operazioni che può fare

while True:

    print("\n--- GESTIONE ESAMI ---")
    print("1) Registra esame")
    print("2) Visualizza esami")
    print("3) Cerca esame")
    print("4) Calcola media")
    print("5) Esci")

    scelta = input("Scegli un'opzione: ")

    match scelta:
        case "1":
            registerExam()
        case "2":
            showExams()
        case "3":
            searchExam()
        case "4":
            meanExam()
        case "5":
            print("Programma terminato")
            break
        case _:
            print("Scelta non valida")