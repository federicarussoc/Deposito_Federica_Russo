#esercizi ifelse

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
