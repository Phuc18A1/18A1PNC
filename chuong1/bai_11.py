import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self):
        """Kiểm tra tam giác hợp lệ"""
        return (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a)

    def perimeter(self):
        """Tính chu vi"""
        return self.a + self.b + self.c

    def area(self):
        """Tính diện tích theo công thức Heron"""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def display(self):
        print(f"Ba cạnh: a={self.a}, b={self.b}, c={self.c}")
        if self.is_valid():
            print(f"→ Chu vi: {self.perimeter():.2f}")
            print(f"→ Diện tích: {self.area():.2f}")
        else:
            print(" Tam giác không hợp lệ.")



class RightTriangle(Triangle):
    def __init__(self, a, b):
        """Tam giác vuông với 2 cạnh góc vuông a, b"""
        c = math.sqrt(a**2 + b**2)
        super().__init__(a, b, c)

    def display(self):
        print(" Tam giác vuông:")
        super().display()


class IsoscelesTriangle(Triangle):
    def __init__(self, a, b):
        """Tam giác cân với hai cạnh bên bằng a và cạnh đáy b"""
        super().__init__(a, a, b)

    def display(self):
        print(" Tam giác cân:")
        super().display()



class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, a):
        """Tam giác đều có 3 cạnh bằng nhau"""
        super().__init__(a, a)

    def display(self):
        print(" Tam giác đều:")
        super().display()



if __name__ == "__main__":
    print("=== Tam giác chung ===")
    tg = Triangle(3, 4, 5)
    tg.display()

    print("\n=== Tam giác vuông ===")
    rt = RightTriangle(3, 4)
    rt.display()

    print("\n=== Tam giác cân ===")
    it = IsoscelesTriangle(5, 6)
    it.display()

    print("\n=== Tam giác đều ===")
    et = EquilateralTriangle(4)
    et.display()