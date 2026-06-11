# creo classe Articolo

class Articolo:
    
    def __init__(self, id_articolo, nome, prezzo, quantita):
        self.id = id_articolo 
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Nome: {self.nome}\n"
            f"Prezzo: {self.prezzo}€\n"
            f"Quantità: {self.quantita}"
        )