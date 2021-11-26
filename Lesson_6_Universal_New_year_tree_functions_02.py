# from typing import Tuple

def heights_input() -> list[int]:

    heights_in = input(
        """
        Введіть висоту кожної з трьох частин ялинки.
        Три цілих числа через пробіл починаючи з верхньоъ частини.
        Увага! числа мають бути більше за 2. Наприклад:  -> 4 3 7
        -> """
        ).split()

    heights = [int(el) for el in heights_in]
    return heights


def all_bloks_widths(heights: list[int]) -> tuple[list, int]:
    """Обчислити максимальну ширину ялинки.

    Args:
        heights (list): [description]

    Returns:
        [type]: [description]
    """
    #
    #       Аналіз даних з метою вирахувати ширину ялинки
    #  Кожний рядок додає 2 до довжини попереднього рядка.
    #  Тобто ширина першого низу буде: 
    #         2 + 2 * "кількість_рядків_1"    
    # для першої частини.
    # Зменшуємо цю шрину на 2 з кожного краю для краси. Маємо: 
    #         2 + 2 * "кількість_рядків_1" - 4
    # Другий крок починається з цієї ширини і додає ще 
    #         2 * "кількість_рядків_2" 
    # рядків. Знову віднімаємо 4 зірочки (по 2 з краю). 
    # Тоді початкова ширина третьої частини буде: 
    #         2 + 2 * "кількість_рядків_1" - 4  +  2 * "кількість_рядків_2" - 4
    # а "низ" третьої частинии буде дорівнювати: 
    #         2 + 2 * "кількість_рядків_1" - 4   \
    #           + 2 * "кількість_рядків_2" - 4   \
    #           + 2 * "кількість_рядків_3"  
    #         
    par_bottom, i = 2, 0 
    bottom_widths = [ ] 
    for height in heights: 
        bottom_width = par_bottom + 2 * height 
        bottom_widths.append(bottom_width) 
        par_centre = bottom_width - 4
    par_bottom += 4    
    return bottom_widths, par_bottom


def print_tree (heights: list[int], bottom_widths: list[int], par_centre: int) -> None: 
    s = '**'   # ширина першого верху - 2
    for i, height in enumerate(heights):
    # Друк наступної частини ялинки
        for _ in range(height):
            print(s.center(par_centre))
            s += "**"
        s = (bottom_widths[i] - 4) * '*' 

    
def print_tree_base(max_bottom: int) -> None: 
    """Print New Year tree base."""  
    print(((1 + max_bottom // 20  )) * "||".center(max_bottom))
 
 
heights = heights_input()                                 # Отримання висоти кожної з частин ялинки
bottom_widths, low_bottom = all_bloks_widths(heights)     # Обчислення довжин низів "частин" ялинки
print_tree(heights, bottom_widths, low_bottom)            # Друк "частин" ялинки
print_tree_base(low_bottom)                               # Друк ніжки ялинки