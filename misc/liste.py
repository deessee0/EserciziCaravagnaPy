class ListaConcatenata:

    class Nodo:
        val = None
        prossimo = None

    def __init__(self):
        self.test = None

    def aggiungi(self, n_val):
        if self.test == None:
            n_nodo = self.nodo
            n_nodo.val = n_val
            self.test = n_nodo

        elem = self.test
        while elem.prossimo is not None:
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


lista_conc = ListeConcatenate()

for elem in range(10):
    lista_conc.aggiungi(elem)

for elem in lista_conc:
    print(elem)
