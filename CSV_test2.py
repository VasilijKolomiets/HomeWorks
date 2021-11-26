import csv

users_data = [
        ("user_name", "user_symma"),
        ["Anna",     "333"],
        ["Viktor",   "435"],
        ["Иванов",    "74"],
        ["Федоров", "4533"],
        ["Шнитке",   "483"],
        ["Элиткин",  "953"],
        ["Шняк",     "456"],
 ]

with open("data3.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(
        users_data
)