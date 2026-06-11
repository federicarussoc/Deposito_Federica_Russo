from libro import Libro
from libreria import Libreria

#creo oggetti della classe Libro
libro1 = Libro("1984", "George Orwell")
libro2 = Libro("Divina Commedia", "Dante Alighieri")
libro3 = Libro("Il nome della rosa", "Umberto Eco")

#creo oggetto della classe LIbreria
libreria = Libreria()

#aggiungo i libri al catalogo libreria
libreria.aggiungi_libro(libro1)
libreria.aggiungi_libro(libro2)
libreria.aggiungi_libro(libro3)

#stampa catalogo
libreria.mostra_catalogo()

print("\nRicerca per titolo:")
risultati = libreria.cerca_per_titolo("1984")

for libro in risultati:
    print(libro)

print("\nRimozione libro con isbn 2:")
libreria.rimuovi_libro(2)

libreria.mostra_catalogo()