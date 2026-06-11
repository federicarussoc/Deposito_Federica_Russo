## MODULI
# In python un modulo è un file
# questo ci permette di importarli e usarli all'interno di altri contesti
# I moduli permettono di organizzare il codice in unità logiche e riutilizzabili, migliorando la
# modularità, la manutenibilità e la leggibilità del codice.
# Un modulo Python può contenere una combinazione di definizioni di funzioni, classi e variabili. 
# È possibile importare un modulo in un programma Python utilizzando l'istruzione import. 
# Una volta importato un modulo, è possibile accedere alle sue definizioni utilizzando il nome del modulo seguito da un punto.

# DEVE ESSERE LO STESSO IDENTICO NOME


## TUPLE

punto = (3,4)

colore_rgb = (255, 128, 0)
informazioni_persona = ("Alice", 25, "Femmina")

punto = (3,4)
print(punto[0])
print(punto[1])

punto = 3,4
x,y = punto
print(x,y)

## INSIEMI
# unione, intersezione, differenza, differenza simmetrica

set1 = set([1,2,3,4,5])
set2 = {4,5,6,7,8}
set3 = {1,2,3,3,4,4,5}
print(set3)


## DIZIONARI

studente = {
    "nome": "Alice",
    "età" : 20,
    "sesso" : "Femmina"
}

for chiave, valore in studente.items():
    print(chiave, "->", valore)