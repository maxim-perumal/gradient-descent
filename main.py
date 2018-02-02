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

f1 = polynomial_deg4(1,1,-13,-1,12)
print(f1.y(0))
print(f1.y(10))
print(f1.y(20))
