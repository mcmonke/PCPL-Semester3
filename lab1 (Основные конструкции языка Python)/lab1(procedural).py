#решение задачи с применением процедурной парадигмы (lab1(procedural).py)
import sys
import math

def get_coefficient(name):
    while True:
        try:
            value = float(input(f"Введите коэффициент {name}: "))
            return value
        except ValueError:
            print(f"Коэффициент {name} должен быть числом. Попробуйте снова.")

def solve_biquadratic_equation(a, b, c):
    if a == 0:
        print("Коэффициент A не должен быть равен 0.")
        return

    print(f"Решаем уравнение {a}x^4 + {b}x^2 + {c} = 0")

    # Приведем его к квадратному уравнению относительно z = x^2
    # Получаем a*z^2 + b*z + c = 0

    discriminant = b**2 - 4 * a * c
    print(f"Дискриминант: {discriminant}")

    if discriminant > 0:
        z1 = (-b + math.sqrt(discriminant)) / (2 * a)
        z2 = (-b - math.sqrt(discriminant)) / (2 * a)
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
        z = -b / (2 * a)
        if z >= 0:
            print(f"Действительные корни: {math.sqrt(z)}, {-math.sqrt(z)}")
        else:
            print("Нет действительных корней.")
    
    else:
        print("Нет действительных корней.")


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

solve_biquadratic_equation(a, b, c)