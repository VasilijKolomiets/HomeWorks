import csv
with open(r"C:\Users\Alisa\ДЗ_УРОК_4\dima.txt") as r_file:
   
    file_reader = csv.reader(r_file, delimiter = ",")  # Создаем объект reader, указываем символ-разделитель ","
    
    count = 0 # Счетчик для подсчета количества строк и вывода заголовков столбцов
    
    for row in file_reader:    # Считывание данных из CSV файла
        if count == 0:
            print(f'Файл содержит столбцы: {": ".join(row)}')  # Вывод строки, содержащей заголовки для столбцов
        else:
            print(f'    {row[0]} : {row[1]}') # Вывод строк
        count += 1
    print(f'Всего в файле {count} строк.')