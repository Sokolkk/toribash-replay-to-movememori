import os
import shutil
import time

# Путь к общей целевой папке 'keys' в 'DayZServer'
common_keys_path = os.path.join(os.getcwd(), "keys")

# Если целевая папка 'keys' не существует, создаем ее
if not os.path.exists(common_keys_path):
    os.makedirs(common_keys_path)


def copy_with_retries(src, dst, retries=5, delay=2):
    """Функция для копирования с несколькими попытками."""
    for i in range(retries):
        try:
            shutil.copy2(src, dst)
            print(f"Файл {src} успешно скопирован в {dst}")
            return True
        except PermissionError as e:
            print(f"Ошибка доступа к файлу {src}: {e}. Попытка {i + 1} из {retries}. Ожидание {delay} секунд...")
            time.sleep(delay)
        except Exception as e:
            print(f"Ошибка при копировании {src} в {dst}: {e}")
            break
    return False


# Получаем текущий каталог
current_directory = os.getcwd()

# Перебираем все элементы в текущем каталоге
for folder_name in os.listdir(current_directory):
    if os.path.isdir(folder_name) and folder_name.startswith("@"):
        at_folder_path = os.path.join(current_directory, folder_name)

        for root, dirs, files in os.walk(at_folder_path):
            for dir_name in dirs:
                if dir_name == "keys":
                    source_keys_path = os.path.join(root, dir_name)

                    # Копируем все содержимое из текущей папки 'keys' в общую папку
                    for item in os.listdir(source_keys_path):
                        s = os.path.join(source_keys_path, item)
                        d = os.path.join(common_keys_path, item)

                        if os.path.isdir(s):
                            try:
                                # Копируем папку, если она существует
                                shutil.copytree(s, d, dirs_exist_ok=True)
                                print(f"Папка {s} успешно скопирована в {d}")
                            except Exception as e:
                                print(f"Ошибка при копировании папки {s} в {d}: {e}")
                        else:
                            copy_with_retries(s, d)
