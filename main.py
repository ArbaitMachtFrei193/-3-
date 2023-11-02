# Запросите у пользователя ввод двух значений (True или False)
value1 = input("Введите первое значение (True или False): ").strip().lower()
value2 = input("Введите второе значение (True или False): ").strip().lower()

# Преобразуйте введенные значения в логические переменные
try:
    value1 = bool(value1)
    value2 = bool(value2)
except ValueError:
    print("Пожалуйста, введите только True или False.")
    exit()

# Выведите результаты логического И, ИЛИ и отрицания
result_and = value1 and value2
result_or = value1 or value2
result_not1 = not value1
result_not2 = not value2

print(f"Результат логического И: {result_and}")
print(f"Результат логического ИЛИ: {result_or}")
print(f"Отрицание первого значения: {result_not1}")
print(f"Отрицание второго значения: {result_not2}")

