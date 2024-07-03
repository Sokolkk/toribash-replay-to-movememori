#торибащ сохранение движений из реплеев
import re
import os

def extract_data(input_file, output_file, move_name, joint):
    try:
        # Ищем текст с расширением ".tbm" в файле
        mod_name = "mushu"
        with open(input_file, 'r') as infile:
            for line in infile:
                tbm_match = re.search(r'\b(\w+)\.tbm\b', line)
                if tbm_match:
                    mod_name = tbm_match.group(1)
                    break

        # Считываем входной файл и записываем данные в выходной файл
        with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:
            # Записываем строки NAME и MOD
            outfile.write(f"NAME {mod_name} {move_name}\n")
            outfile.write(f"MOD /{mod_name}\n")

            turn_number = 1
            for line in infile:
                match = re.match(rf'{joint}\s*(.*)', line)
                if match:
                    data = match.group(1).strip()
                    outfile.write(f"TURN {turn_number}; {data}\n")
                    turn_number += 1
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found in the current directory.")

# Запрашиваем имя входного файла, название приема и игрока у пользователя
input_filename = input("Введите имя файла в текущей папке: ")
move_name = input("Введите название приема: ")
output_filename = r"C:\Program Files (x86)\Steam\steamapps\common\Toribash\data\script\system\movememory.mm"
player = input("игрок 1 или 0 (по умолчанию 0): ")
if not player:
    player = '0'
joint = 'JOINT ' + player + ';'

# Вызываем функцию
extract_data(input_filename, output_filename, move_name, joint)





