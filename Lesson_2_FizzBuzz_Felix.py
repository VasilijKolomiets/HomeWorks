number = int(input("Введіть число: "))

rest3, rest5 = number%3, number%5

if rest3 == 0:
    print("Fizz", sep="")
if rest5 == 0:
    print("Buzz")