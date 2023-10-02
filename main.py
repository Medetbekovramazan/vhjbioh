a = int(input('число   '))
print(a)
print(a + 1)
print(a + 2)  # 2


a = int(input("Введите длину ребра куба: "))
volume = (a ** 3)
surface_area = 6 * (a ** 2)
print("Объем куба:", volume)
print("Площадь полной поверхности куба:", surface_area)


a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
print(3 * (a + b) * (a + b) * (a + b) + 275 * b * b - 127 * a - 41)


number = int(input("Введите целое число: "))
next_number = number + 1
prev_number = number - 1
print(f"Следующее число после {number} - {next_number}")
print(f"Предыдущее число перед {number} - {prev_number}")


monitor_cost = int(input("Введите стоимость монитора: "))
system_unit_cost = int(input("Введите стоимость системного блока: "))
keyboard_cost = int(input("Введите стоимость клавиатуры: "))
mouse_cost = int(input("Введите стоимость мыши: "))
one_computer_cost = monitor_cost + system_unit_cost + keyboard_cost + mouse_cost
total_cost = one_computer_cost * 3
print("Общая стоимость покупки трех компьютеров:", total_cost)


a_1 = int(input("Введите первый член прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите номер члена прогрессии: "))
a_n = a_1 + d * (n - 1)
print(f"n-й член арифметической прогрессии: {a_n}")











