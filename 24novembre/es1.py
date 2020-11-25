import math

class FiguraGeometrica:
    def __init__(self, n):
        self.nLati = n

    def CalcolaPerimetro(self):
        pass

    def CalcolaArea(self):
        pass

    def n_lati(self):
        return self.nlati

    def stampa_caratteristiche(self):
        pass

class Triangolo(FiguraGeometrica):
    def __init__(self, a, b, c):
        super().__init__(3)
        self.lato1 = a
        self.lato2 = b
        self.lato3 = c
        
    def perimetro(self):
        return self.a + self.b + self.c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p *(p-self.a)*(p-self.b)*(p-self.c))
    
    def who(self):
        if self.lato1 == self.lato2 == self.lato3:
            print("Il triangolo è equilatero")
        elif self.lato1 != self.lato2 != self.lato2:
            print("Il triangolo è scaleno")
        else: print("Il triangolo è isoscele")

class Rettangolo(FiguraGeometrica):
    def __init__(self, b, h):
        super().__init__(4)
        self.base = b
        self.altezza = h
        
    def perimetro(self):
        return 2*self.base + 2*self.altezza

    def area(self):
        return self.base * self.altezza

class Cerchio(FiguraGeometrica):
    def __init__(self, r):
        super().__init__(0)
        self.raggio = r
        
    def area(self):
        return 2*math.pi(self.raggio**2)

    def perimetro(self):
        return 2*math.pi*self.raggio
       -------- 
    
    

