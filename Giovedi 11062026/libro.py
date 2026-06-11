# Creo classe Libro

class Libro:

    contatore = 0 #contatore parte da zero

    def __init__(self, titolo, autore): #costruttore
        self.titolo = titolo
        self.autore = autore

        Libro.contatore += 1 #incremento il contatore ogni volta che creo un libro

        self.isbn = Libro.contatore #simulo isbn tramite contatore, assegno il valore del contatore come codice univoco per identificare il libro

    def descrizione(self):
        return (f"Il titolo del libro è {self.titolo}, "
                f"è stato scritto da {self.autore} "
                f"e ha codice {self.isbn}")

    def __str__(self):
        return self.descrizione()


