class Viaggio:
    
    def __init__(self, nome, dataP, dataR, localita, resort, prezzo, partecipanti, responsabile):
        
        self.nome_viaggio = nome
        self.dataP = dataP
        self.dataR = dataR
        self.localita = localita
        self.resort = resort
        self.prezzo = prezzo
        self.partecipanti = partecipanti 
        self.responsabile = responsabile 

    def stampa(self):
        pass
    
    def periodo(self):
        pass

    def guadagno(self):
        pass

class VacanzaInvernale(Viaggio):
    pass

class VacanzaEstiva(Viaggio):
    pass


