def bisestile(anno):
    if(anno%400==0 or (anno%4==0 and (anno%100!=0))):
        return True 
    else:
        return False

class Data:
    '''
    classe per rappresentare una data 
    '''
    def __init__(self, g, m, a):
        #una data è caratterizzata da giorno, mese e anno 
        self.giorno = g
        self.mese = m
        self.anno = a 
    
    def __iter__(self):
        return self 

    def __next__(self):
        #giorni di ciascun mese per anno non bisestile 
        giorni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        #controllo se l'attributo anno rappresenta un anno bisestile 
        if(bisestile(self.anno)):
            #cambio l'entrata relativa a febbraio
            giorni[1] = 29
        #indice per ottenere i giorni del mese corrente
        indice_mese = self.mese - 1  
        gg = giorni[indice_mese]
        #se non sono all'ultimo giorno del mese 
        if(self.giorno<gg):
            #aggiungo 1 al giorno attuale 
            x = self.giorno 
            self.giorno +=1
            return Data(x, self.mese, self.anno) 
        #sono all'ultimo giorno del mese 
        else: 
            #se non sono a dicembre 
            if(self.mese!=12):
                x = self.giorno
                y = self.mese 
                self.giorno = 1
                self.mese += 1
                return Data(x, y, self.anno)
            #sono al 31 dicembre 
            else:
                x = self.giorno
                y = self.mese 
                z = self.anno 
                self.giorno = 1
                self.mese = 1
                self.anno += 1
                return Data(x, y, z)
    
    #stampare la data nel formato gg/mm/aa
    def __str__(self):
        return '{} / {} / {}'.format(self.giorno, self.mese, self.anno)


#data ordinaria 
d1 = Data(7, 1, 2000)
myiter1 = iter(d1)
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))

print("\n")

#fine febbraio anno bisestile 
d2 = Data(27, 2, 2020)
myiter2 = iter(d2)
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))

print("\n")

#fine febbraio anno non bisestile 
d3 = Data(27, 2, 2019)
myiter3 = iter(d3)
print(next(myiter3))
print(next(myiter3))
print(next(myiter3))
print(next(myiter3))

print("\n")

#fine dicembre 
d4 = Data(30, 12, 2020)
myiter4 = iter(d4)
print(next(myiter4))
print(next(myiter4))
print(next(myiter4))
print(next(myiter4))


