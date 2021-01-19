import matplotlib.pyplot as plt
from math import e

# Classe generica per funzione
class Function:
    "Generic function R -> R"

    def printname(self):
        print("I am a generic function")
    
    def eval(self, x):
        pass

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

# Una funzione su intervalli
class IntervalFunction (Function):
    "Function defined over [a, b], 0 otherwise"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def printname(self):
        print("Interval Function defined in [", self.a, ';', self.b, "]")
    
    def myrealeval(self, x):
        pass

    def eval(self, x):
        if(x < self.a or x > self.b): 
            print("eval: x =", '{:2f}'.format(x), "out of [a,b] evaluation, forcing 0.")
            return(0)
        else:
            x = self.myrealeval(x)
            print("eval: x =", x, "in [a,b], standard evaluation gives", x)
            return(x)

    def integrate(self, x, y, dx = 0.01, plot = False):
        print("Calcolo integrale [", x, ", ", y, "] con dx =", dx)
        self.printname()
        
        # Range di calcolo da x ad y, con step delta_x
        x_start = x
        x_end = y
        i = 0
        
        # f_x memorizza f(x), x i punti discretizzati sull'asse x
        f_x = []
        x = []
        
        cumulative_f = 0
        
        while (x_start + i * dx) < x_end:
            this_x = x_start + i * dx + 0.5 * dx
            this_fx = self.eval(this_x)
            
            x = x + [this_x]
            f_x = f_x + [this_fx]
            
            cumulative_f += this_fx
            
            i = i + 1
            
        self.prettyprint("Dominio x", x)
        self.prettyprint("Funzione f(x)", f_x)
        self.prettyprint("Funzione f(x)", f_x)
            
        integral = dx * cumulative_f
            
        print("Integrale ", integral, "\n")
            
        # Plot con matplotlib
        if(plot):
            plt.plot(x, f_x)
            plt.show()
                
        return(integral)
        
# Una funzione su intervalli
class IntervalRetta (IntervalFunction):
    "Straight line defined over [a, b]"

    def __init__(self, a, b, m, q):
        super().__init__(a, b)
        self.m = m
        self.q = q

    def printname(self):
        print("Straight line defined in [", self.a, ';', self.b, "]; m = ", self.m, " q = ", self.q)
    
    def myrealeval(self, x):
        return self.m * x + self.q

obj_nonsense = IntervalFunction(1, 4)
obj_nonsense.printname()
print(obj_nonsense.eval(2))
print(obj_nonsense.eval(-3))

obj_Retta = IntervalRetta(1, 4, 1, 0)
obj_Retta.printname()
print(obj_Retta.eval(3))
print(obj_Retta.eval(-3))

print(obj_Retta.integrate(-10, 10, dx = .5, plot = False))

class Esponenziale(IntervalFunction):
    
    def __init__(self, a, b):
        super().__init__(a, b)  
        
    def printname(self):
        print("Exponential function in [", self.a, ';', self.b, "]")
        
    def eval(self, x):
        return (e ** (- 0.5 * (x ** 2)))
    
obj_normale = Esponenziale(-3, 3)
obj_normale.integrate(-5, 5, plot = True)
