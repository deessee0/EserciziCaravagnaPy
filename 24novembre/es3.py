class Function:
  "Generic function R -> R"

  def printname(self):
    print("sono una funzione generica")

  def eval(self, x):
    pass


class IntervalFunction(Function):

  def __init__(self, a, b):
    self.a = a
    self.b = b

  def printname(self):
    print("sono una funzione con intervallo")

  def myrealeval(self, x):
    pass

  def eval(self, x):
    if(x < self.a or x > self.b): 
      print("eval: x fuori intervallo [a, b], restituisco 0")
      return(0)
    else:
      v = self.myrealeval(x)
      print("eval: x = ", '{:2f}'.format(x), '->', v)
      return(v)

  def integrate(self, x, y, dx):
    x_start = x
    x_end = y
    i = 0

    f_x = []
    x = []

    cumulative_f = 0

    while(x_start + i * dx < x_end):
      this_x = x_start + i * dx + 0.5 * dx
      this_fx = self.eval(this_x)
      cumulative_f += this_fx

      x = x + [this_x]
      f_x = f_x + [this_fx]

      i += 1

    print("Calcolo integrale completo:", cumulative_f * dx)
    return(cumulative_f * dx)

class IntervalRetta(IntervalFunction):
  "Linea retta etc"

  def __init__(self, a, b, m , q):
    super().__init__(a, b)
    self.m = m
    self.q = q

  def myrealeval(self, x):
    return(self.m * x + self.q)
