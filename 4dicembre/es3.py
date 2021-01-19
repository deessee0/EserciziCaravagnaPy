class Function:
  def __init__(self, name, a, b):
    self.name = name
    self.a = a
    self.b = b

  def printname(self):
    print("Function: ", self.name, "tra [", self.a, ';', self.b, "]")
    
  def prettyprint(self, message, values):
    
    drop = False
    
    if(type(values) is list and len(values) > 10): 
        drop = True
        values = values[1:10]
        values = values + ["..."]
            
    if(not drop):
        print("~~~o~~~o~~~o~~~")
    else:
        print("~~~o~~~o~~~o~~~ (showing only the first 10 values)")
            
    print(message, "->", values)
    print("~~~o~~~o~~~o~~~\n")

  def min_value(self, delta_x = 0.5):
    print("Calcolo valore piu vicino 0")
    self.printname()
    
    # Range di calcolo da a a b, con step delta_x
    x_start = self.a
    x_end = self.b 
    i = 0
    
    # f_x memorizza f(x), mentra abs_f_x |f(x)|
    f_x = []
    abs_f_x = []
    x = []
    
    while (x_start + i*delta_x) < x_end:
        
        this_x = x_start + i*delta_x
        this_fx = self.eval(this_x)
        
        x = x + [this_x]
        f_x = f_x + [this_fx]
        abs_f_x = abs_f_x + [abs(this_fx)]
        
        i = i + 1
    
    self.prettyprint("Dominio x", x)
    self.prettyprint("Funzione f(x)", f_x)
    self.prettyprint("Valore assoluto |f(x)|", abs_f_x)
        
    # Per cercare il valore piu vicino a 0 posso guardare i valori 
    # assoluti. All'indice in cui trovo il minimo ho trovato il 
    # valore che e' piu vicino a 0; mi devo segnare quell'indice.
    # Posso assumere che la posizione 0 sia il minimo inizialmente
    x_min =  0
    for i in range(1, len(abs_f_x)):
        if abs_f_x[i] < abs_f_x[x_min]: x_min = i
        
    print("L'elemento piu vicino a 0 y = ", x[x_min], "con f(y) = ", self.eval(x[x_min]), "\n")

  def eval(self, x):
    pass
    
class Retta(Function):
  def __init__(self, a, b, m, q):
    super().__init__("Retta", a, b)
    self.m = m
    self.q = q
  
  def printname(self):
    Function.printname(self)
    print("Coeff angolare m = ", self.m, "e intercetta q = ", self.q, "\n")
  
  def eval(self, x):
    return self.m * x + self.q

bisettrice = Retta(-3, 3, 1, 0)
bisettrice.min_value(delta_x = 1)
input() 

non_bisettrice = Retta(-3, 3, 3, 1)
non_bisettrice.min_value(1/3)
input() 

class Parabola(Function):
  def __init__(self, a, b, c0, c1, c2 ):
    super().__init__("Retta", a, b)
    self.c0 = c0
    self.c1 = c1
    self.c2 = c2
  
  def printname(self):
    Function.printname(self)
    print("Parabola coefficent(s) a = ", self.c0, 'b =',  self.c1, 'c =', self.c2, "\n")
  
  def eval(self, x):
    return self.c0 + self.c1 * x + self.c2 * (x*x)

parabola_semplice = Parabola(-3, 3, 0, 0, 1)
parabola_semplice.min_value(delta_x = 1)
input() 


parabola_spostata = Parabola(-3, 3, 1, 1, 1)
parabola_spostata.min_value(delta_x = 1)
input() 

parabola_spostata.min_value(delta_x = 1/10)
input() 

parabola_spostata.min_value(delta_x = 1/100)