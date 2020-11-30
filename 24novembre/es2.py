##############################################################
#
#                   COMPAGNIA DI VIAGGIO
#
# @FILENAME f_01_es_02.py
# @AUTHOR(S) Giulio Caravagna, Gaia Saveri, Pietro Morichetti
# @BRIEF gestione di viaggi tramite programmazione ad ogetti
# 
# @DATE 24/11/2020
# @LASTUPDATE 25/11/2020
# @VERSION 1.2
#
# Il programma implementa una generica classe "Viaggio" con
# dati di base e metodi per determinare info sul viaggio, sui
# guadagni dell'agenzia e sul periodo di giorni e mesi del
# viaggio. Questa classe viene ereditata da "Estiva" e
# "Invernale" che aggiungono un paio di attributi e modificano
# alcuni metodi della superclasse. Infine è presente una
# funzione esterna per determinare l'elenco dei viaggi e
# l'ammontare di denaro speso da un preciso cliente.
#
##############################################################


####################### CLASSE VIAGGIO #######################

class Viaggio:
    """
    Questa classe rappresenta un generico viaggio offerto da una compagnia di viaggi.

    La classe è fornita degli attributi: 
    -- [String] nome_viaggio, titolo del viaggio
    -- [lista di 3 Integer] data_partenza, data prevista per la partenza
    -- [lista di 3 Integer] data_ritorno, data prevista del rientro
    -- [String] localita, luogo in cui è stata pianificata la vacanza
    -- [String] resort, stabilimento che ospiterà i partecipanti al viaggio
    -- [Integer] prezzo, ammontare (standard) previsto per ogni partecipante
    -- [lista di String] partecipanti, elenco le persone che si sono prenotati il viaggio
    -- [String] responsabile, figura di riferimento per il viaggio
    
    E dei seguenti metodi:
    -- [void] stampa, stampa a schermo le informazioni base di un viaggio
    -- [Float] guadagno, restituisce il guadagno netto dell'agenzia per questo viaggio
    -- [lista di 2 Integer] periodo, restituisce il numero di giorni e di mesi del viaggio
    """

    def __init__(self, nome_viaggio, data_partenza, data_ritorno, localita, resort, prezzo, partecipanti, responsabile):
        self.nome_viaggio = nome_viaggio
        self.data_partenza = data_partenza
        self.data_ritorno = data_ritorno
        self.localita = localita
        self.resort = resort
        self.prezzo = prezzo
        self.partecipanti = partecipanti
        self.responsabile = responsabile

    def stampa(self):
        """Inizializza una istanza della classe."""
        stampa = "--- dati viaggio ---\n"
        stampa += "nome_viaggio: " + str(self.nome_viaggio) + "\n"
        stampa += "data_partenza: " + str(self.data_partenza) + "\n"
        stampa += "resort: " + str(self.resort) + "\n"
        stampa += "prezzo: " + str(self.prezzo) + "\n"
        stampa += "partecipanti: " + str(self.partecipanti) + "\n"
        stampa += "responsabile: " + str(self.responsabile) + "\n"
        stampa += "----------------------"

        print(stampa)
    
    def guadagno(self):
        """Restituisce il 47% dell'ammontare di denaro speso dai clienti."""
        return (len(self.partecipanti) * self.prezzo) * 47 / 100

    def periodo(self):
        """ 
        Dato che dobbiamo considerare solo l'anno corrente, facciamo uso di
        una lista che riporta il numero di giorni per ogni mese da cui poi
        andremo a determinare il numero di giorni di vacanza (e di mesi).
        Ci sono due casi da considerare:
        1. partenza e ritorno sono in due mesi diversi. In tal caso il numero
        di giorni di vacanza + determinato come: 
        giorni rimanenti del mese di partenza + giorni di ogni mese che non sia 
        quello di ritorno + giorni del mese di ritorno (ossia la data di ritorno)
        2. partenza e ritorno nello stesso mese. In tal caso è sufficiente fare:
        data di ritorno - data di partenza per avere i giorni di vacanza
        In entrambi i casi sommiamo 1 per considerare anche il giorno di partenza
        come giorno di vacanza.
        """
        # lista dei mesi, ogni item corrisponde ai giorni per quel mese
        anno_2020 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        giorni_vacanza = 0 # giorni risultanti
        mesi_vacanza = 0 # mesi risultanti
        
        # sottragliamo perché la lista si conta da 0!
        mese_partenza = self.data_partenza[1] - 1 # quando si parte...
        mese_ritorno = self.data_ritorno[1] - 1 # quando si torna...
        mese = self.data_partenza[1] - 1 # indice sui mesi (da partenza)
        
        trovato_mese = True # variabile di "check"
        while(trovato_mese == True): # verifichiamo alla "larga" sui mesi
            if(mese == mese_partenza and mese != mese_ritorno):
                # prendiamo tutti i giorni rimanenti del mese di partenza
                giorni_vacanza += (anno_2020[mese] - self.data_partenza[0])
            elif(mese != mese_ritorno):
                # prendiamo tutto il mese
                giorni_vacanza += anno_2020[mese]
            else:
                # si parte e si torna nello stesso mese
                trovato_mese = False
            mesi_vacanza += 1
            mese += 1 # prossimo mese
        
        # verifichiamo sui giorni
        if(mese_partenza != mese_ritorno): 
            giorni_vacanza += self.data_ritorno[0]  
            # ci basta sommare i giorni corrispondenti alla data di rientro
        else:
            giorni_vacanza = self.data_ritorno[0] - self.data_partenza[0]
            # stesso mese: semplice differenza e abbiamo i giorni di vacanza
        
        giorni_vacanza += 1 # necessario perché per noi la partenza è di vacanza
        return [giorni_vacanza, mesi_vacanza]


####################### CLASSE INVERNALE #######################


class Invernale(Viaggio):
    """
    Questa classe rappresenta un generico viaggio Invernale offerto da una compagnia di viaggi.
    Sottoclasse della classe Viaggio.

    La classe è fornita degli attributi: 
    -- [String] nome_viaggio, titolo del viaggio
    -- [lista di 3 Integer] data_partenza, data prevista per la partenza
    -- [lista di 3 Integer] data_ritorno, data prevista del rientro
    -- [String] localita, luogo in cui è stata pianificata la vacanza
    -- [String] resort, stabilimento che ospiterà i partecipanti al viaggio
    -- [Integer] prezzo, ammontare (standard) previsto per ogni partecipante
    -- [lista di String] partecipanti, elenco le persone che si sono prenotati il viaggio
    -- [String] responsabile, figura di riferimento per il viaggio
    -- [Integer] skipass, prezzo giornaliero delo skipass
    -- [lista di String] impianti_sciistici, elenco degli impianti sciistici accedibili
    
    E dei seguenti metodi:
    -- [void] stampa, stampa a schermo le informazioni base di un viaggio
    -- [Float] guadagno, restituisce il guadagno netto dell'agenzia per questo viaggio
    -- [lista di 2 Integer] periodo, restituisce il numero di giorni e di mesi del viaggio
    """
    
    def __init__(self, nome_viaggio, data_partenza, data_ritorno, localita, resort, prezzo, partecipanti, responsabile, skipass, impianti_sciistici):
        """Inizializza un'istanza della classe"""
        super().__init__(nome_viaggio, data_partenza, data_ritorno, localita, resort, prezzo, partecipanti, responsabile)
        self.skipass = skipass
        self.impianti_sciistici = impianti_sciistici

    def guadagno(self):
        """
        Sulla base della località del viaggio, il guadagno dell'agenzia subisce
        delle variazioni.
        """
        guadagno_standard = super().guadagno()
        if(self.localita == "Cortina"):
            guadagno_standard -= (len(self.partecipanti) * self.prezzo) * 15 / 100
        elif(self.localita == "San Mortiz"):
            guadagno_standard -= (len(self.partecipanti) * self.prezzo) * 10 / 100
        else:
            guadagno_standard -= (len(self.partecipanti) * self.prezzo) * 5 / 100

        return guadagno_standard


####################### CLASSE ESTIVA #######################


class Estiva(Viaggio):
    """
    Questa classe rappresenta un generico viaggio Invernale offerto da una compagnia di viaggi.
    Sottoclasse della classe Viaggio.

    La classe è fornita degli attributi: 
    -- [String] nome_viaggio, titolo del viaggio
    -- [lista di 3 Integer] data_partenza, data prevista per la partenza
    -- [lista di 3 Integer] data_ritorno, data prevista del rientro
    -- [String] localita, luogo in cui è stata pianificata la vacanza
    -- [String] resort, stabilimento che ospiterà i partecipanti al viaggio
    -- [Integer] prezzo, ammontare (standard) previsto per ogni partecipante
    -- [lista di String] partecipanti, elenco le persone che si sono prenotati il viaggio
    -- [String] responsabile, figura di riferimento per il viaggio
    -- [Integer] distanza, distanza in metri tra il resort e la spiaggia
    -- [lista di String] escursioni_marine, elenco delle attività "marittime"
    
    E dei seguenti metodi:
    -- [void] stampa, stampa a schermo le informazioni base di un viaggio
    -- [Float] guadagno, restituisce il guadagno netto dell'agenzia per questo viaggio
    -- [lista di 2 Integer] periodo, restituisce il numero di giorni e di mesi del viaggio
    """

    def __init__(self, nome_viaggio, data_partenza, data_ritorno, localita, resort, prezzo, partecipanti, responsabile, distanza, escursioni_marine):
        """Inizializza un'istanza della classe."""
        super().__init__(nome_viaggio, data_partenza, data_ritorno, localita, resort, prezzo, partecipanti, responsabile)
        self.distanza = distanza
        self.escursioni_marine = escursioni_marine

    def guadagno(self):
        """
        L'insieme delle attività marittime flettono il guadagno dell'agenzia di un altro 10%.
        """
        guadagno_standard = super().guadagno()
        guadagno_standard -= (len(self.partecipanti)/2 * self.prezzo) * 10 / 100
        return guadagno_standard


####################### FUNZIONI ESTERNE #######################


def bilancio_cliente(cliente, viaggi):
    """
    La funzione esterna determina l'elenco dei viaggi a cui un preciso cliente ha
    partecipato e l'ammontare di denaro speso per tutte queste.

    Si cerca il cliente in ogni viaggio organizzato e se viene trovato, si registra
    la località della vacanza ed il prezzo (standard) speso.

    Essa riceve in ingreso le seguenti variabili:
    -- [String] cliente, cognome del cliente da esaminare
    -- [lista di String] viaggi, elenco dei viaggi dell'agenzia di viaggio
    """

    spesa = 0
    prenotazioni = []
    for viaggio in viaggi: # cerchiamo in tutto l'elenco dei viaggi organizzati
        cerca = True
        candidato = 0
        # cerchiamo tra i partecipanti il nostro cliente per un preciso viaggio
        while(candidato < len(viaggio.partecipanti) and cerca == True):
            if(viaggio.partecipanti[candidato] == cliente): # trovato!
                prenotazioni.append(viaggio.localita) # registriamo la località
                spesa += viaggio.prezzo # somma delle spese
                cerca = False
            else:
                candidato += 1 # prossimo partencipante

    print(cliente, "ha speso:", spesa)
    print("luoghi in cui è stato", cliente, ":", prenotazioni)


####################### "MAIN" #######################


## vacanze (generiche) ##
v0 = Viaggio("Mille ed una Notte", [1, 1, 2000], [7, 1, 2000], "sharm el sheikh", "Emirati Palace", 20000, ["Fontana", "Sanchez", "King", "Pirandello"], "DiGregorio")

v1 = Viaggio("Ritorno al Futuro", [1, 1, 2000], [25, 3, 2000], "Los Angeles", "Ghost Buster Hotel", 1400, ["Fontana", "Petrarca", "Boccaccio", "Seneca"], "Girasole")

v2 = Viaggio("Sabbia e Mare", [1, 1, 2000], [7, 1, 2000], "sharm el sheikh", "Emirati Palace", 300, ["Fontana", "Sanchez", "King", "Pirandello"], "DiGregorio")
        
v0.stampa()
vacanza = v1.periodo()
print(v1.nome_viaggio, "- giorni:", vacanza[0], "mesi:", vacanza[1])
print(v2.nome_viaggio, "- guadagno:", v2.guadagno())

## vacanze estive ##
v3 = Estiva("Sapori D'oriente", [1, 1, 2000], [7, 1, 2000], "Nuova Deli", "Essenza Palace", 20000, ["Darth Maul", "Olivieri", "Pirandello"], "Cesare", 200, ["acquagym", "snorkeling"])

v4 = Estiva("Palma d'oro", [1, 1, 2000], [7, 1, 2000], "Mykonos", "Greece Hotel", 1400, ["King", "Boccaccio", "Petronio"], "Girasole", 100, ["poolparty", "snorkeling"])

print(v4.nome_viaggio, "- guadagno:", v4.guadagno())

## vacanze invernali ##
v5 = Invernale("Alle Spalle del Monte", [1, 1, 2000], [7, 1, 2000], "Cortina", "Cortina Palace", 300, ["Fontana", "Virgilio", "Seneca"], "DiGregorio", 30, ["impianto1", "impianto2", "impianto3"])

v6 = Invernale("Fiocco di Neve", [1, 1, 2000], [7, 1, 2000], "San Mortiz", "Mortiz Palace", 300, ["King", "Petrarca", "Pirandello"], "Cesare", 50, ["impianto4", "impianto5"])

print(v6.nome_viaggio, "- guadagno:", v6.guadagno())


# funzione esterna
bilancio_cliente("Fontana", [v0, v1, v2, v3, v4, v5, v6])
