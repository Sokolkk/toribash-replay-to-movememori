import os

# Получаем текущий каталог
current_directory = os.getcwd()

# Проходимся по всем элементам в текущем каталоге
for root, dirs, files in os.walk(current_directory):
    # Проверяем, если папка начинается с '@'
    if os.path.basename(root).startswith('@'):
        for dir_name in dirs:
            # Преобразуем имя папки в строчные буквы
            lower_case_name = dir_name.lower()
            if dir_name != lower_case_name:
                # Определяем полные пути для исходной и новой папки
                original_path = os.path.join(root, dir_name)
                new_path = os.path.join(root, lower_case_name)
                # Переименовываем папку
                os.rename(original_path, new_path)
                print(f"Переименовано: '{original_path}' -> '{new_path}'")

        # Обновляем список папок, так как они могли быть переименованы
        dirs[:] = [d.lower() for d in dirs]
