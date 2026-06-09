#lezione 09/06/2026
#clausole di controllo del flusso, diamo maggiori informazioni al flusso

#PASS
#Non fa niente: serve a evitare l'errore mentre costruiamo i software.
#Serve a costruire l'architettura senza doverla popolare subito

for i in range(5):
    
    print(i)

#es
for i in range(5):
    if i == 3:
        pass
    print(i)

#BREAK 
#utilizzata per interrompere il ciclo in anticipo se si verifica una condizione specifica
for i in range(5):
    if i == 3:
        break
    print(i)

#CONTINUE
#L'istruzione continue viene utilizzata per saltare il resto del blocco di codice 
#all'interno di un ciclo e passare alla prossima iterazione.

for i in range(5):
    if i == 3:
        continue
    print(i)

#OPERATORE SPLAT (*)
#allungamento/spalmaggio
#viene utilizzato per espandere un iterabile in elementi separati (come una lista, una tupla o un range)

#es

numeri = [*range(1,11)]
print(numeri)

#funzioni
#esempio massimo dell'astrazione 
#dichiarando una funzione possiamo definire un blocco di codice che poi viene richiamato in un altro punto
#la funzione viene scritta in un punto
#i parametri possono essere posizionali, keyword e di default 

def esempio(parametri):
    #corpo della funzione

    pass

esempio(argomenti)

#servono a organizzare il codice di unità modulari che possono essere richiamate e riutilizzate in diverse parti di un programma
#ogni funzione deve essere atomica, cioè rispettare un solo obiettivo
#anche se vuol dire creare più funzioni
#rende il codice manutenibile, leggibile, comprensibile 

def saluta(nome):
    print("Ciao, ", nome)

def somma(a,b):
    risultato = a+b
    print("La somma è: ", risultato)

#tipi di parametri 
#i parametri possono essere posizionali 
#print(f"{messaggio} {nome}!") un altro modo di stampare una stringa

#esistono 2 tipi di funzioni: quelle con return e quelle senza

def quadrato(numero): #funzione con return
    return numero * numero

risultato = quadrato(4)
print(risultato)

