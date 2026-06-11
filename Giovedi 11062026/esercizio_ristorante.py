## Esercizio 7

#creo la classe Piatto

class Piatto:
    def __init__(self, nome, categoria, prezzo): #costruttore
        self.nome = nome
        self.categoria = categoria
        self.prezzo = prezzo
    
    def descrivi_piatto(self): #metodo di istanza
        print(f"{self.nome} ({self.categoria}) - {self.prezzo}€")

#creo la classe Ristorante

class Ristorante:
    def __init__(self, nome, tipo_cucina): #costruttore
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False #chiuso di default
        self.menu = [] #lista di oggetti Piatto

    # da qui sono tutti metodi di istanza

    def descrivi_ristorante(self): 
        print(f"Il ristorante si chiama {self.nome} e propone un tipo di cucina {self.tipo_cucina}")

    def stato_apertura(self):
        if self.aperto:
            print("Il ristorante è aperto")
        else:
            print("Il ristorante è chiuso")

    def apri_ristorante(self):
        if not self.aperto:
            self.aperto = True
            print("Il ristorante è ora aperto")
        else:
            print("Il ristorante è già aperto")

    def chiudi_ristorante(self):
        if self.aperto:
            self.aperto = False
            print("Il ristorante è ora chiuso")
        else:
            print("Il ristorante è già chiuso")
    
    def aggiungi_al_menu(self, piatto): #aggiungo l'oggetto Piatto
        if piatto not in self.menu: #se il piatto non è presente in menù
            self.menu.append(piatto) #lo aggiungo
        else:
            print("Piatto già inserito") #altrimenti errore

    def togli_dal_menu(self, piatto): 
        if piatto in self.menu: #se il piatto è nel menù
            self.menu.remove(piatto) #lo tolgo
        else:
            print("Piatto non presente") #altrimenti errore

    def stampa_menu(self):
        for piatto in self.menu: #per ogni elemento nella lista menù
            piatto.descrivi_piatto() #sto chiamanto un metodo dell'oggetto Piatto      

r = Ristorante("kfc", "fast food")

r.descrivi_ristorante()

r.stato_apertura()

r.apri_ristorante()

p1 = Piatto("insalata", "contorni", 5.99)
p2 = Piatto("pollo fritto", "secondi", 9.99)
p3 = Piatto("coca-cola", "bibite", 4.49)

r.aggiungi_al_menu(p1)
r.aggiungi_al_menu(p2)
r.aggiungi_al_menu(p3)

r.stampa_menu()

r.togli_dal_menu(p1)
r.stampa_menu()

r.chiudi_ristorante()
    
