def is_right_angle_triangle(a, b, c):
    while True:
        result = {}
        error = False
        a = float(input('Введите сторону 1: '))
        b = float(input('Введите сторону 2: '))
        c = float(input('Введите сторону 3: '))
        
        if a + b > c and a + c > b and b + c > a:
            print("Треугольник существует")         
        else:
            result['success'] = False
            result['description'] = "No such triangle exists"
            error = True
            print(result)
    
        if a ** 2 + b ** 2 == c ** 2:
            result['success'] = True
            result['description'] = "The triangle is right-angled"
            error = True
            print(result)
        elif a ** 2 + c ** 2 == b ** 2:
            result['success'] = True
            result['description'] = "The triangle is right-angled"
            error = True
            print(result)
        else:
            if c ** 2 + b ** 2 == a ** 2:
                result['success'] = True
                result['description'] = "The triangle is right-angled"
                error = True
                print(result)
            else:
                result['success'] = False
                result['description'] = "The triangle is not right-angled"
                error = True
                print(result)


result = is_right_angle_triangle()
