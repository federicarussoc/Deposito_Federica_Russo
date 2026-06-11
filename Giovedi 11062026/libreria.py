# Creo classe Libreria

class Libreria:

    def __init__(self):
        self.catalogo = []
    
    def aggiungi_libro(self, libro):
        if libro not in self.catalogo:
            self.catalogo.append(libro)
        else:
            print("Libro già presente in catalogo")
    
    def rimuovi_libro(self, isbn):
        trovato = False

        for libro in self.catalogo:
            if libro.isbn == isbn:
                self.catalogo.remove(libro)
                trovato = True
                break
        if not trovato:
            print("Libro non presente in catalogo")

    def cerca_per_titolo(self, titolo):
        lista = []
        for libro in self.catalogo:
            if libro.titolo == titolo:
                lista.append(libro)
        return lista
    
    def mostra_catalogo(self):
        for libro in self.catalogo:
            print(libro)
