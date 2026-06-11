## Esercizio 5

class Convertitore:

    @staticmethod
    def euro_in_dollari(importo):
        return importo * 1.08
    
    @staticmethod
    def km_in_miglia(distanza):
        return distanza * 0.621371
    
print(Convertitore.euro_in_dollari(100)) #essendo un metodo statico lo chiamo direttamente dalla classe, senza creare un oggetto Convertitore
print(Convertitore.km_in_miglia(10))

## Esercizio 6

class Animale:

    numero_animali = 0 #attributo di classe

    def __init__(self, nome, specie): #costruttore che definisce gli attributi delle istanze e incrementa il contatore ogni volta che creiamo un oggetto Animale
        self.nome = nome
        self.specie = specie
        Animale.numero_animali += 1

    @classmethod #metodo di classe
    def quanti_animali(cls):
        print(f"Numero di animali creati: {cls.numero_animali}")

pippo = Animale("cane", "mammifero")
pluto = Animale("cane", "mammifero")
paperino = Animale("papera", "anatide")

Animale.quanti_animali() #chiamo il metodo direttamente dalla classe


