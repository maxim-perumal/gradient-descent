class polynomial_deg4:
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    def __init__(self, a , b , c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def y(self, x):
        return self.a*x**4 + self.b*x**3 + self.c*x**2 + self.d*x + self.e

    def derivative(self, x1):
        return 4*self.a*x1**3 + 3*self.b*x1**2 + 2*self.c*x1 + self.d
