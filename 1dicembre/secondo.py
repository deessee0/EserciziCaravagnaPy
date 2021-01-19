# Una classe persona con anagrafica
class Persona:
  def __init__(self, ruolo, nome, cognome):
    self.ruolo = ruolo 
    self.nome = nome 
    self.cognome = cognome

  def bonjour(self):
    print(self.ruolo, ":", self.nome, self.cognome)

# Una sotto-classe Studente con una lista di corsi.
# Memorizzo anche n, il numero dei corsi seguiti.
class Studente(Persona):
    
  def __init__(self, nome, cognome, lista_corsi):
    super().__init__("Studente UNITS", nome, cognome)
    self.lista_corsi = lista_corsi
    self.n = len(lista_corsi)
    
  def bonjour(self): 
    Persona.bonjour(self) 
    # Stampa con un for
    for i in range(0, self.n):
        print("> Frequento il corso:", self.lista_corsi[i])
        
# Una sotto-classe Docente con una lista di corsi.
# Memorizzo anche n, il numero dei corsi insegnati.
class Docente(Persona):
    
  def __init__(self, nome, cognome, lista_corsi):
    super().__init__("Docente UNITS", nome, cognome)
    self.lista_corsi = lista_corsi
    self.n = len(lista_corsi)
    
  def bonjour(self): 
    Persona.bonjour(self) 
    # Stampa con un for
    for i in range(0, self.n):
        print("> Insegno il corso:", self.lista_corsi[i])

# Creo un oggetto e chiamo la funzione bonjour()
obj_Giulio = Studente("Giulio", "Caravagna", ("Programmazione", "Laboratorio di Programmazione", "Analisi", "Geometria"))
obj_Giulio.bonjour()

obj_Mario = Studente("Mario", "Rossi", ("Programmazione", "Laboratorio di Programmazione"))
obj_Mario.bonjour()

obj_ProfRusso = Docente("Stefano Alberto", "Russo", ("Programmazione", "Laboratorio di Programmazione"))
obj_ProfRusso.bonjour()

def separatore():
    print("-~-~-o-~-~-o-~-~-")
    
# Restituisce True (come in C davamo un valore intero prestabilito, es 0)
# solo se il docente copre tutti i corsi di uno studente. Se uno studente
# ha dei corsi scoperti questi vengono restituiti
def docente_copre_studente(docente, studente):
    
    print("Docente che esamino")
    separatore()
    docente.bonjour()
    
    print("\nStudente che esamino")
    separatore()
    studente.bonjour()

    print("\nRicerca in corso ...")
    separatore()
    
     # Flag True sse tutti i corsi sono coperti.
    corsi_trovati = True
    
    # Lista di corsi scoperti, inzialmente vuota. In C questa sarebbe
    # una lista linkata come visto a lezione
    corsi_scoperti = []
    
    # Risolvo in stile C, poi vedremo come possiamo evitare tutto questo,
    # usando due ricerche iterative (annidate). La logica e' cercare per
    # ogni corso dello studente, se tra la lista dei corsi tenuti dal docente
    # quel corso compare. Se non compare, me lo memorizzo in una lista e 
    # mi ricordo anche che il docente non copre tutti i corsi. La ricerca
    # deve comunque guardare tutti i corsi dello studente perche voglio
    # resitutire la lista dei corsi scoperti.    
    
    # La prima iterazione usa un indice definito su 0, ..., n-1, come in C.
    # E' un for perche decido di guardare tutto visto che devo restituire
    # la lista di corsi che rimangono scoperti (altrimenti un while 
    # sarebbe stato la scelta giusta, ricerca lineare incerta).
    for i in range(0, studente.n):
        
        # Flag per la ricerca lineare incerta: per ogni corso di uno
        # studente, cerco se il docento lo copre o meno 
        corso_trovato = False 
        
        # Vedo tutti i docenti fino a che non trovo il corso
        j = 0
        while not corso_trovato and j < docente.n:
            if(studente.lista_corsi[i] == docente.lista_corsi[j]):
                corso_trovato = True
            j = j + 1
        
        # Qui sono fuori dal while, quindi corso_trovato mi dice se
        # ho trovato o meno il corso. Prima lo stampo
        print("Corso", studente.lista_corsi[i], " -> ", corso_trovato)
        
        # Poi gestisco il caso in cui non l'ho trovato
        if(not corso_trovato):
            
            # In particolare appendo in fondo alla lista il nome del
            # corso che non trovo. Questa operazione in C si sarebbe
            # fatta allocando memoria dinamica, usando addT o addC.
            #
            # Notate la sintassi diversa, il "+" qui indica appendere
            # un elemento in coda alla lista (come con addC). Ora siccome
            # la append (+) vuole due liste. Io costruisco al volo una
            # lista intrno a studente.lista_corsi[i] usando [..]. Cosi
            # a livello di tipi entrambi gli operandi del + sono liste
            corsi_scoperti = corsi_scoperti + [studente.lista_corsi[i]]
        
        # La formula logica che costruisco e' un and su ciascuno dei 
        # corsi dello studente. corso_trovato mi dice se ho trovato
        # o no il corso i-esimo, quindi lo uso per fare l'and. Notare 
        # che corsi_trovati viene inizializzata True altrimenti l'and
        # sarebbe sempre false
        corsi_trovati = corsi_trovati and corso_trovato
        
    # Qua sono fuori dal for - riporto solamente a schermo se ho trovato 
    # o meno tutto
    
    print("\nRicerca completata")
    separatore()
    
    if(corsi_trovati):
        print("Tutti i corsi sono coperti.")
    else:
        print("Qualche corso rimane scoperto.")
        for i in range(0, len(corsi_scoperti)):
            print("\t >", corsi_scoperti[i])
        
    return corsi_scoperti


# Testo i metodi
docente_copre_studente(obj_ProfRusso, obj_Mario)
docente_copre_studente(obj_ProfRusso, obj_Giulio)

# Commentate voi questo codice come io ho fatto con la funzione sopra
def copertura_totale(lista_di_docenti, studente):
    
    coperto = False
    
    
    # Inizialmente devo verificare tutti i corsi
    corsi_da_verificare = studente.lista_corsi
    
    i = 0
    
    print("Ricerca copertura")
    separatore()

    while not coperto and i < len(lista_di_docenti):
        # S asterisco (come nelle note)
        obj_S_ast = Studente(studente.nome, studente.cognome, corsi_da_verificare)
        
        copertura_docente = docente_copre_studente(lista_di_docenti[i], obj_S_ast)
        
        if(len(copertura_docente) == 0):
            coperto = True
        else:
            corsi_da_verificare = copertura_docente
        i = i + 1
    
    print("Ricerca con tutti i docenti completata")
    separatore()

    if not coperto:
        print("Lo studente rimane scoperto su alcuni corsi")
    else:
        print("Lo studente ha tutti i corsi coperti")
        
    return coperto

# Russo copre Mario (gia lo copriva da solo)
copertura_totale([obj_ProfRusso], obj_Mario)

# .. ma Russo da solo non copre Giulio 
copertura_totale([obj_ProfRusso], obj_Giulio)

# Per coprire Giulio mi serve un docente per Analisi e Geometria, il docente puo fare anche altri corsi (gia coperti da Russo, per esempio)
obj_ProfPippo = Docente("Pippo", "Goofy", ("Analisi", "Laboratorio di Programmazione", "Geometria"))
obj_ProfPippo.bonjour()

# Russo + Pippo coprono Giulio 
copertura_totale([obj_ProfRusso, obj_ProfPippo], obj_Giulio)