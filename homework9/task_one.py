class Triangle:
    def __init__(self, a, b, c):
        if self._check_if_exist(a, b, c):
            self.a = a
            self.b = b
            self.c = c

    def _check_if_exist(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True
        raise ValueError('Треугольник не существует')

    def perimetr(self):
        return self.a + self.b + self.c

    def __eq__(self, other):
        perimetr1 = self.perimetr()
        perimetr3 = other.perimetr()
        return perimetr1 == perimetr3

    def __ne__(self, other):
        perimetr1 = self.perimetr()
        perimetr3 = other.perimetr()
        return perimetr1 != perimetr3

    def is_right_angled(self):
        if self.a**2 + self.b**2 == self.c**2:
            return True
        else:
            return False


try:
    t2 = Triangle(10, 10, 20)
except ValueError as e:
    print(e)


t1 = Triangle(3, 4, 5)
t3 = Triangle(6, 8, 10)

print(t1.is_right_angled())
print(t1 == t3)
print(t1 != t3)
