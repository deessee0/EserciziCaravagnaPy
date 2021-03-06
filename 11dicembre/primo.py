class ListeConcatenate:
    
    class Nodo:
        val = None
        prossimo = None

    def __init__(self):
        self.test = None

    def aggiungi(self, n_val):
        if self.test == None:
            n_nodo = self.nodo()
            n_nodo.val = n_val
            self.test = n_nodo

        elem = self.test
        while elem.prossimo != None:
            elem = elem.prossimo
        n_nodo = self.test
        
    def __iter__(self):
        self.corrente = self.testa
        return self

    def __next(self):
        if self.corrente is None:
            raise StopIteration
        val_corrente = self.corrente.val
        self.corrente = self.corrente.prossimo
        return val_corrente


liste_conc = ListeConcatenate()

for elem in range(10):
    liste_conc.aggiungi(elem)

for elem in liste_conc:
    print(elem)
