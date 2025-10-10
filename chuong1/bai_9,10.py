import math

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def is_valid(self):
        return (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a)

    def chuvi(self):
        return self.a + self.b + self.c

    def dientich(self):
        s = self.chuvi() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
t = Triangle(3, 4, 5)
if t.is_valid():
    print("Chu vi:", t.chuvi())
    print("Diện tích:", t.dientich())
else:
    print("Tam giác không hợp lệ!")



#bài 10
class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)

t2 = EquilateralTriangle(4)
print("Chu vi:", t2.chuvi())
print("Diện tích:", t2.dientich())