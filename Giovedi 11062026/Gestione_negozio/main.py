# importo le classi

from articolo import Articolo
from inventario import Inventario
from clienti import Cliente
from amministratore import Amministratore

## Inizzializzo il sistema

inventario = Inventario() 

admin1 = Amministratore("Federica") 

a1 = Articolo(1, "libro", 20.00, 10)
a2 = Articolo(2, "penna", 3.00, 5)
a3 = Articolo(3, "gomma", 0.80, 20)

inventario.aggiungi_articolo(a1)
inventario.aggiungi_articolo(a2)
inventario.aggiungi_articolo(a3)

clienti = []

# Creo il menù principale che dovrà permettere di scegliere l'operazione da svolgere
# per adesso ho completato solamente la registrazione clienti

while True:

    print("\nScegliere un'opzione:")
    print("1. Registrazione cliente")
    print("2. Login cliente")
    print("3. Login amministratore")
    print("4. Esci")

    scelta = input("Scegli un'opzione: ")

    match scelta:

        case "1":
            nome = input("Inserisci il nome: ")

            nuovo_cliente = Cliente(nome)

            clienti.append(nuovo_cliente)

            print("Registrazione completata.")
            print(nuovo_cliente)
        
        case "2":
            id_cliente = int(input("Inserisci il tuo ID cliente: "))

            trovato =

