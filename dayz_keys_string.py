import os

# Получаем текущий каталог
current_directory = os.getcwd()

# Список для хранения имен папок
folder_names = []

print(f"Поиск папок с '@' в каталоге: {current_directory}\n")

# Обход всех файлов и папок в текущем каталоге и его подкаталогах
for root, dirs, files in os.walk(current_directory):
    for dir in dirs:
        # Если имя папки содержит "@", добавляем его в список
        if "@" in dir:
            folder_names.append(dir)
            print(f"Найдена папка: {dir} в каталоге {root}")

# Объединяем имена папок в одну строку, разделяя их "; "
result = "; ".join(folder_names)

# Проверяем, найдены ли папки
if result:
    print(f"\nВсе найденные папки: {result}")
else:
    print("Папки с '@' не найдены.")