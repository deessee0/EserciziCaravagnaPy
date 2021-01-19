class MyFibo:

    def __init__(self, max):
        self.max = max
    
    def __iter__(self):
        self.n = 0
        self.n_0 = 0
        self.n_1 = 1 
        return self
    
    def __next__(self):
        if self.n <= self.max:
            if self.n == 0:
                result = self.n_0
            if self.n == 1:
                result = self.n_1
            if self.n > 1:
                result = self.n_0 + self.n_1
                self.n_0 = self.n_1
                self.n_1 = result
            self.n += 1
            return result
        else:
            raise StopIteration
            

serf_fibonacci = MyFibo(20)

for i in serf_fibonacci
    print(i)