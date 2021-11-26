import csv

file = r"D:\Les_Pyton\Data.txt"
list_data = []  
with open(file) as open_file:
    for row_file in csv.reader(open_file):
       list_data.append(row_file)

open_file.close()

sum_by_last_name = {}
for row_data in list_data:
    sum_by_last_name[row_data[0]] = sum_by_last_name.get(row_data[0], 0) + int(row_data[1])
print(sum_by_last_name)