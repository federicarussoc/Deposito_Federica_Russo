# creo classe Clienti

class Cliente:

    contatore = 0 #contatore parte da zero

    def __init__(self, nome):
        self.nome = nome

        Cliente.contatore += 1 #incremento il contatore ogni volta che un utente si registra

        self.id = Cliente.contatore #assegno i singoli id tramite contatore all'utente

        self.acquisti = [] #lista acquisti

    def descrizione(self): #restituisce descrizione cliente
        return (f"Il cliente si chiama {self.nome}, "
                f"e il corrispondente codice utente è {self.id} ")

    def __str__(self): #permette di stampare direttamente l'oggetto cliente
        return self.descrizione()
    
    def visualizza(self, inventario): #mostra tutti gli articoli presenti nell'inventario usando un metodo della classe inventario
        inventario.mostra_magazzino()

    def acquista(self, inventario, id_articolo):
        # vedo se l'articolo è presente nell'inventario
        if id_articolo in inventario.magazzino:

            articolo = inventario.magazzino[id_articolo]

            # vedo se c'è almeno un'unità dell'articolo 
            if articolo.quantita > 0:
                articolo.quantita -= 1 #sottraggo l'unità acquistata
                self.acquisti.append(articolo) #se sì salvo l'articolo tra gli acquisti
                
                inventario.registra_vendita(self, articolo) #aggiorno vendite e guadagni

                print("Articolo acquistato con successo")
            else:
                print("Articolo esaurito") # se non sono presenti unità: errore

        else:
            print("Articolo non presente nell'inventario") #se articolo non presente in magazzino: errore
        
    @classmethod
    def mostra_numero_clienti(cls):
        print(f"Numero di clienti registrati: {cls.contatore}")
        
