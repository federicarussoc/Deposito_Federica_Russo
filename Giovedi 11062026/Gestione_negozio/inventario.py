## creo una classe inventario


class Inventario:

    def __init__(self):
        self.magazzino = {} #dizionario che contiene tutti gli articoli dove chiave è l'id e il valore è l'oggetto articolo

        self.vendite = [] #lista di tuple che contiene le vendite

        self.guadagni_totali = 0

    def aggiungi_articolo(self, articolo):
        if articolo.id not in self.magazzino: #se l'id non è presente in magazzino
            self.magazzino[articolo.id] = articolo #lo aggiungo 
        else:
            print("Articolo già presente in magazzino") #altrimenti errore
    
    def rimuovi_articolo(self, id_articolo):

        if id_articolo in self.magazzino: #se l'articolo è presente 
            self.magazzino.pop(id_articolo) #lo elimino con pop()
        else:
            print("Articolo non presente")

    def mostra_magazzino(self): #stampo tutti gli articoli presenti in magazzino

        for articolo in self.magazzino.values():
            print(articolo)

    def registra_vendita(self, cliente, articolo):

        self.vendite.append(
            (cliente.nome, articolo.nome, articolo.prezzo) #informazioni della vendita conservate in una tupla
        )

        self.guadagni_totali += articolo.prezzo #aggiorno i guadagni totali

    def mostra_rapporto_vendite(self):

        print("rapporto vendite")

        for vendita in self.vendite:
            print(vendita)

        print(f"\nGuadagni totali: {self.guadagni_totali}€")