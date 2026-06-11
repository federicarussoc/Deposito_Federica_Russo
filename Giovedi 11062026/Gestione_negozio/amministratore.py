# Classe amministratore

class Amministratore:

    contatore = 0

    def __init__(self, nome): #anche amministratore, come cliente, ha un codice univoco creato tramite contatore
        self.nome = nome

        Amministratore.contatore += 1
        self.id = Amministratore.contatore

    def descrizione(self):
        return f"L'amministratore si chiama {self.nome}, codice amministratore: {self.id}"

    def __str__(self):
        return self.descrizione()

    def visualizza_inventario(self, inventario):
        inventario.mostra_magazzino()

    def visualizza_rapporto_vendite(self, inventario):
        inventario.mostra_rapporto_vendite()