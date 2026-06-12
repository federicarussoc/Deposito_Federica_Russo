# importo le classi

from articolo import Articolo
from inventario import Inventario
from clienti import Cliente
from amministratore import Amministratore


# creo una funzione per gestire il menù cliente

def menu_cliente(cliente, inventario):
    
    while True:

        print("\nScegliere un'opzione:")
        print("1. Visualizza articoli")
        print("2. Acquista articolo")
        print("3. Mostra acquisti effettuati")
        print("4. Esci")

        scelta = input("Scegli un'opzione: ")

        match scelta:

            case "1":
                inventario.mostra_magazzino()
            
            case "2":

                id_articolo = input("Inserire ID articolo che si vuole acquistare: ")

                cliente.acquista(inventario, id_articolo)
                
            case "3":
                if len(cliente.acquisti) == 0:
                    print("Nessun acquisto effettuato")
                else:
                    print("\nArticoli acquistati:")

                    for articolo in cliente.acquisti:
                        print(f"Nome: {articolo.nome} - Prezzo: {articolo.prezzo}€")

            case "4":
                break

            case _:
                print("Opzione non corretta, fare un'altra scelta: ")

# creo funzione per gestire menù amministratore

def menu_admin(amministratore, inventario):
    
    while True:
            
        print("\nScegliere un'opzione:")
        print("1. Visualizza inventario")
        print("2. Aggiungi articolo")
        print("3. Rimuovi articolo")
        print("4. Visualizza rapporto vendite")
        print("5. Visualizza guadagni totali")
        print("6. Esci")

        scelta = input("Scegli un'opzione: ")

        match scelta:

            case "1":
                inventario.mostra_magazzino()
            
            case "2":
                id_articolo = input("Inserire ID articolo che si vuole aggiungere: ")
                nome_articolo = input("Inserire nome articolo che si vuole aggiungere: ")
                prezzo_articolo = float(input("Inserire prezzo articolo che si vuole aggiungere: "))
                quantita_articolo = int(input("Inserire quantità articolo che si vuole aggiungere: "))

                nuovo_articolo = Articolo(id_articolo, nome_articolo, prezzo_articolo, quantita_articolo)

                inventario.aggiungi_articolo(nuovo_articolo)
                
            case "3":
                id_articolo_rimuovere = input("Inserire ID articolo da rimuovere: ")

                inventario.rimuovi_articolo(id_articolo_rimuovere)

            case "4":
                inventario.mostra_rapporto_vendite()

            case "5":
                print(f"Guadagni totali: {inventario.guadagni_totali}€")

            case "6":
                break

            case _:
                print("Opzione non corretta, fare un'altra scelta: ")

## Inizzializzo il sistema

inventario = Inventario() 

admin1 = Amministratore("Federica", "123") 

a1 = Articolo("1", "libro", 20.00, 10)
a2 = Articolo("2", "penna", 3.00, 5)
a3 = Articolo("3", "gomma", 0.80, 20)

inventario.aggiungi_articolo(a1)
inventario.aggiungi_articolo(a2)
inventario.aggiungi_articolo(a3)

clienti = []

amministratori = []

amministratori.append(admin1)

# Creo il menù principale che dovrà permettere di scegliere l'operazione da svolgere

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

            trovato = False

            for i in clienti:
                if id_cliente == i.id:
                    trovato = True
                    cliente_trovato = i
                    break
            
            if trovato: 
                print(cliente_trovato.descrizione()) 
                menu_cliente(cliente_trovato, inventario)
            else: 
                print("Utente non trovato")
            
        case "3":
            id_admin = input("Inserisci il tuo ID Amministratore: ")

            trovato = False

            for i in amministratori:
                if id_admin == i.id:
                    trovato = True
                    admin_trovato = i
                    break
            
            if trovato: 
                print(admin_trovato.descrizione())
                menu_admin(admin_trovato, inventario)
            else: 
                print("Amministratore non trovato")

        case "4":
            break

        case _:
            print("Opzione non corretta, fare un'altra scelta: ")
