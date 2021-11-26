height = int(input("Введіть висоту ялинки -> "))
array = []
for i in range(height):
    array.append(i)

s = '**'
parCentre = len(array) * 2
for i in array:
    print(s.center(parCentre))
    s += "**"
print("||".center(parCentre))