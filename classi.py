### LE CLASSI ###

# una classe è un modello logico che serve a definire un tipo non basilare
# è un concetto astratto
# gli oggetti sono le istanze reali della classe
# le classi devono essere singolari per ogni codice (una sola classe penna, infiniti oggetti che ne derivano)
# la classe definisce: tipo (la classe definisce un nuovo tipo di oggetto), metodi (le funzioni definite nella classe che descrivono i comportamenti degli oggetti.), 
# attributi. 
# ogni oggetto avrà in comune con gli oggetti della stessa classe queste tre cose
# non avranno in comune il nome proprio, il valore degli attributi, il modo in cui utilizzano i metodi

# le classi sono un'astrazione dei concetti del mondo reale, riprodotto come tipo all'interno della prorammazione
# le classi sono definite udanso la parola chiave class, seguita dal nome della classe.
# le classe possono contenere metodi e attributi

# Gli attributi sono variabili associate ad una classe, rappresentano le proprietà di un oggetto e sono condivisi tra tutte le istanze di una classe
# I metodi sono funzioni associate a una classe, rappresentano il comportamento di un oggetto

class Automobile:                                                # dichiaro la classe
    numero_di_ruote = 4                                          # attributo di classe

    def __init__ (self, marca, modello):                         # metodo costruttore
        self.marca = marca                                       # attributo di istanza
        self.modello = modello                                   # attributo di istanza
    
    def stampa_info(self):                                       # metodo di istanza

        print("Lautomobile è una", self.marca, self.modello)

# Il costruttore è rappresentato dal metodo init che deve definire gli attributi obbligatori relativi a quell'oggetto, 
# è implicito esiste anche se non si sovrascrive
# Self serve a riferirsi all'oggetto che sta usando il metodo
# Tutti i metodi con __ si chiamano "dunder method", i dunder method sono metodi speciali
# init accetta almeno un parametro

# Creazione di oggetti da una classe

auto1 = Automobile("Fiat", "500")
auto2 = Automobile("BMW", "X3")

auto1.stampa_info()
auto2.stampa_info()

# Esempio costruttore

class Persona:
    def __init__(self, nome, eta):
        self.nome = nome # Attributo per memorizzare il nome
        self.eta = eta # Attributo per memorizzare l'età

# Creazione di un oggetto persona

p = Persona("Pippo", 30)

print(p.nome) 
print(p.eta)

# I metodi possono essere:

# Di istanza: Lavorano sull'oggetto, quelli che hanno il self, sono definiti dentro la classe, possono volere altri parametri oltre il self
# Di classe: Lavorano sulla classe, sono definiti usando il decoratore @classmethod e ricevono come parametro la classe
# Statici: Non sono legati nè alla classe nè all'oggetto, sono definiti dal decoratore @staticmethod

# Esempio metodo statico

class Calcolatrice:

    @staticmethod
    def somma(a,b):
        return a+b

risultato = Calcolatrice.somma(5,3)
print(risultato)

# Esempio di metodo della classe 

class Contatore:
    numero_istanze = 0 # Attributo di classe

    def __init__(self):
        Contatore.numero_istanze += 1
    
    @classmethod 
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")

c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze() 