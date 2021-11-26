while True:
    num = int(input("Давайте нарисуем елочку (от 5 до 25): \n"))
    if num < 5:
        print("Не, ну так не пойдет давай елочку побольше нарисуем например 5")
    elif num > 25:
        print("Ну это уже перебор введи до 25")
    else:
        break
s = '**'
for i in range(num):
    print(s.center(100))
    s += "****"
print("||||".center(100))
print("||||".center(100))