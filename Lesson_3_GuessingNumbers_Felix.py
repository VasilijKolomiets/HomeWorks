left, check_number, right = 1, 8, 16

while right - left > 1: 
    num = int(input(f'Ваше число більше за {check_number}? \n 0 - No  1 - Yes: \n -> '))
    if num == 1: 
        left = check_number
        check_number += (right - check_number) // 2
    else: 
        right = check_number
        check_number += (left - check_number) // 2

#когда массив (1,2)        
    if left == 1 and right == 2:
        num = int(input(f'Ваше число більше за {check_number}? \n 0 - No  1 - Yes: \n -> '))
        if num == 0: 
            right = left
    
    print(left, check_number, right)

print(f"Ви загадали число: {right}")