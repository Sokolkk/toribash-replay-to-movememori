import os

def remove_spaces_from_at_folders(directory):
    """
    Удаляет пробелы из имен папок, начинающихся с '@' в указанном каталоге.

    Args:
        directory: Путь к каталогу для обработки.
    """

    for name in os.listdir(directory):
        if name.startswith('@') and ' ' in name:
            src = os.path.join(directory, name)
            dst = os.path.join(directory, name.replace(' ', ''))
            try:
                os.rename(src, dst)
                print(f"Переименовано: {src} -> {dst}")
            except OSError as e:
                print(f"Ошибка при переименовании {src}: {e}")

# Получаем путь к текущему каталогу
current_directory = os.getcwd()

# Вызываем функцию для текущего каталога
remove_spaces_from_at_folders(current_directory)