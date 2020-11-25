class Persona:
    def __init__(self, ruolo, nome, cognome, eta):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def buongiorno(self):
        print(self.ruolo, ":", self.nome, self.cognome, self.eta)

class Studente(Persona):
    def __init__(self, nome, cognome, eta, lista_corsi):
        super().__init__("Studente UNITS", nome, cognome, eta, lista_corsi)
        self.lista_corsi = lista_corsi

    def buongiorno(self):
        for i in range(0, self.n):
            print("> Frequento il corso: ", self.lista_corsi[i])

class Docente(Persona):
    def __init__(self, nome, cognome, eta, corso):
        super().__init__("Docente UNITS", nome, cognome, eta, corso)
        self.corso = corso
    

    def buongiorno(self):
        if self.eta > 40:
            super().buongiorno("Docente UNITS", self.nome, self.cognome, "<40")
            Persona.buongiorno(self)
            print("> Docente del corso: ", self.corso) 

