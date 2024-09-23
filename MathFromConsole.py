def triangle_area(a, b):
    return 0.5 * a * b
a = float(input("Введіть довжину першого катета: "))
b = float(input("Введіть довжину другого катета: "))
area = triangle_area(a, b)
print(f"Площа прямокутного трикутника: {area}")