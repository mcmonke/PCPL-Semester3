#решение задачи с применением объектно-ориентированной парадигмы (lab1(oop).py)
import sys
import math

class BiquadraticEquation:
    def __init__(self, a, b, c): #конструктор класса
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        if self.a == 0:
            raise ValueError("Коэффициент A не должен быть равен 0.")
        
        print(f"Решаем уравнение {self.a}x^4 + {self.b}x^2 + {self.c} = 0")

        discriminant = self.b ** 2 - 4 * self.a * self.c
        print(f"Дискриминант: {discriminant}")
        
        if discriminant > 0:
            z1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            z2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            roots = []
            
            if z1 >= 0:
                roots.append(math.sqrt(z1))
                roots.append(-math.sqrt(z1))
            if z2 >= 0:
                roots.append(math.sqrt(z2))
                roots.append(-math.sqrt(z2))

            if roots:
                print(f"Действительные корни: {sorted(set(roots))}")
            else:
                print("Нет действительных корней.")
        
        elif discriminant == 0:
            z = -self.b / (2 * self.a)
            if z >= 0:
                print(f"Действительные корни: {math.sqrt(z)}, {-math.sqrt(z)}")
            else:
                print("Нет действительных корней.")
        
        else:
            print("Нет действительных корней.")

def get_coefficient(name):
    while True:
        try:
            value = float(input(f"Введите коэффициент {name}: "))
            return value
        except ValueError:
            print(f"Коэффициент {name} должен быть числом. Попробуйте снова.")

if len(sys.argv) == 4:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except ValueError:
        print("Один или несколько параметров командной строки некорректны.")
        a = get_coefficient('A')
        b = get_coefficient('B')
        c = get_coefficient('C')
else:
    a = get_coefficient('A')
    b = get_coefficient('B')
    c = get_coefficient('C')

equation = BiquadraticEquation(a, b, c)
equation.solve()