import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(
        ("user_name",  "user_symma")
    )

    users_data = [
        ["Anna",     "333"],
        ["Viktor",   "435"],
        ["Иванов",    "74"],
        ["Федоров", "4533"],
        ["Шнитке",   "483"],
        ["Элиткин",  "953"],
        ["Шняк",     "455"],
        ["Шняк2",    "435"],
 ]

for user in users_data:
    with open ("data.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(
            user
        )
