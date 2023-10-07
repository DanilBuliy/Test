import sys


print(sys.argv)
sys.stdout.write("Hello, World!\n")

try:
    # Какой-то код, который может вызвать исключение
    x = 1 / 0
except Exception as e:
    # Вывод сообщения об ошибке в стандартный поток ошибок
    print(f"An error occurred: {e}", file=sys.stderr)

# Вывести все аргументы командной строки
print("Список аргументов командной строки:", sys.argv)

# Вывести имя скрипта (первый элемент)
print("Имя скрипта:", sys.argv[0])
def recursive_search(data, target):
    # Проверяем базовый случай: если data - это не словарь, возвращаем None
    if not isinstance(data, dict):
        return None

    # Итерируем по элементам словаря
    for key, value in data.items():
        # Если значение - это словарь, делаем рекурсивный вызов для него
        if isinstance(value, dict):
            result = recursive_search(value, target)
            if result is not None:
                return result  # Если найден результат во вложенном словаре, возвращаем его
        elif value == target:
            return key, value  # Если значение не словарь и равно цели, возвращаем ключ и значение

    # Если цель не найдена в текущем словаре, возвращаем None
    return None



# Пример данных (глубоко вложенный словарь)
my_data = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3,
            'f': 4
        }
    },
    'g': 5
}

# Ищем значение 3 в данных
result = recursive_search(my_data, 3)

# Выводим результат
if result:
    print(f"Значение найдено: {result}")
else:
    print("Значение не найдено.")
