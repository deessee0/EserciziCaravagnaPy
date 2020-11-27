import math 
class Figura:
    '''
    classe cha rappresenta una generica figura geometrica, caratterizzata dal suo numero di lati 
    '''
    def __init__(self, n):
        self.nlati = n
    
    #per ogni figura voglio poter calcolare il perimetro
    def perimetro(self):
        pass
    
    #per ogni figura voglio poter calcolare l'area 
    def area(self):
        pass 
    
    def n_lati(self):
        return self.nlati 
    
    def stampa_caratteristiche(self):
        pass 
 
class Triangolo(Figura):
	'''
	classe che rappresenta un triangolo
	'''
	def __init__(self, a, b, c):
		#un triangolo è una figura con 3 lati 
		super().__init__(3)
		self.a = a
		self.b = b
		self.c = c
	
	def perimetro(self):
		#il perimetro è la somma dei lati 
		return self.a+self.b+self.c

	def area(self):
		#formula di Erone 
		p = (self.a+self.b+self.c)/2
		return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
	
	def tipo_triangolo(self):
		if(self.a!=self.b and self.b!=self.c and self.c!=self.a):
			return "Triangolo Scaleno"
		elif(self.a==self.b and self.b==self.c and self.c==self.a):
			return "Triangolo Equilatero"
		else:
			return "Triangolo isoscele"
	
	def stampa_caratteristiche(self):
		print("Triangolo:\nnumero lati: ", Figura.n_lati(self), 
        "\nTipo triangolo: ", Triangolo.tipo_triangolo(self), 
        "\nlunghezza lati: \n\ta = ",self.a, "\n\tb = ", self.b, "\n\tc = ", self.c,
		"\nPerimetro = ", Triangolo.perimetro(self), "\nArea = ", Triangolo.area(self), "\n")

class Rettangolo(Figura):
	'''
	classe che rappresenta un rettangolo 
	'''
	def __init__(self, b, h):
		#un rettangolo è una figura con 4 lati 
		super().__init__(4)
		self.base = b
		self.altezza = h 
	
	def perimetro(self):
		return 2*self.base + 2*self.altezza 

	def area(self):
		return self.base*self.altezza
	
	def quadrato(self):
		if(self.base == self.altezza):
			return True 
		else:
			return False 
	
	def stampa_caratteristiche(self):
		if(Rettangolo.quadrato(self) == True):
			print("Quadrato, \nnumero lati: ", Figura.n_lati(self),
			"\nlunghezza lati: ", self.base, 
            "\nPerimetro = ", Rettangolo.perimetro(self), "\nArea = ", Rettangolo.area(self), "\n")
		else: 
			print("Rettangolo: \nnumero lati: ", Figura.n_lati(self),
			"\nlunghezza lati: \n\tbase = ", self.base, "\n\taltezza = ", self.altezza, 
			"\nPerimetro = ", Rettangolo.perimetro(self), "\nArea = ", Rettangolo.area(self), "\n")

class Cerchio(Figura):
	'''
	classe che rappresenta un cerchio 
	'''
	def __init__(self, r):
		super().__init__(0)
		self.raggio = r
	
	def perimetro(self):
		return 2*math.pi*self.raggio 
	
	def area(self):
		return math.pi*(self.raggio**2)

	def stampa_caratteristiche(self):
		print("Cerchio: \nRaggio = ", self.raggio, "\nCirconferenza = ", Cerchio.perimetro(self), "\nArea = ", Cerchio.area(self), "\n")

#tests
#triangolo scaleno 
scaleno = Triangolo(11,25,30)
scaleno.stampa_caratteristiche()
#triangolo isoscele
isoscele = Triangolo(18, 18, 30)
isoscele.stampa_caratteristiche()
#triangolo equilatero
equilatero = Triangolo(22, 22, 22)
equilatero.stampa_caratteristiche()

#rettangolo
rettangolo = Rettangolo(10,20)
rettangolo.stampa_caratteristiche()
#quadrato
quadrato = Rettangolo(15, 15)
quadrato.stampa_caratteristiche()

#cerchio
cerchio = Cerchio(10)
cerchio.stampa_caratteristiche()

#opzionale 
figure = [scaleno, rettangolo, quadrato]

def area_totale(l):
    area = 0
    for fig in l:
        area += fig.area()
    return area 

area_tot = area_totale(figure)
print("Area totale = ", area_tot)

		

	







