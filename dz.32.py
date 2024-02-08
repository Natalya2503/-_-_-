# задача
# напиши тестовые сценарии для данной функции и протестируйте ее 

# def is_even(number: int) -> bool:
"""
Проверяет, является ли число четным.
:param number: Проверяемое число
:return: True, если число четное, иначе False
"""
    # return number % 2 == 0

def is_even(number: int) -> bool:
    return number % 2 == 0

#-------test case 1------#
# expected result: is_even(8) -> True
# actual result: is_even(8) -> True
number = 8
print(f'is_even({number}) -> {is_even(number)}')

#-------test case 2------#
# expected result: is_even(4.2) -> False
# actual result: is_even(4.2) -> False
number = 4.2
print(f'is_even({number}) -> {is_even(number)}')

#-------test case 3------#
# expected result: is_even(-3) -> False
# actual result: is_even(-3) -> False
number = -3
print(f'is_even({number}) -> {is_even(number)}')

#-------test case 4------#
# expected result: is_even(5) -> False
# actual result: is_even(5) -> False
number = 5
print(f'is_even({number}) -> {is_even(number)}')

print('---------------------------------------')
# задача
# напиши тестовые сценарии для данной функции и протестируйте ее 

# def calculate_average(numbers: list[float]) -> float:
"""
Вычисляет среднее значение списка чисел.
:param numbers: Список чисел
:return: Среднее значение
"""
# if not numbers:
#    raise ValueError("Список чисел не должен быть пустым")
# return sum(numbers) / len(numbers)

def calculate_average(numbers: list[float]) -> float:
    if not numbers:
     raise ValueError("Список чисел не должен быть пустым")
    return sum(numbers) / len(numbers)

#--------test case 1--------#
# expected result: calculate_average([1.2, 3.4, 5.0]) -> float
# actual result: calculate_average([1.2, 3.4, 5.0]) -> float
numbers = [1.2, 3.4, 5.0]
print(f'calculate_average({numbers}) -> {calculate_average(numbers)}')

#--------test case 2--------#
# expected result: calculate_average([1, 3, 5]) -> float
# actual result: calculate_average([1, 3, 5]) -> float
numbers = [1, 3, 5]
print(f'calculate_average({numbers}) -> {calculate_average(numbers)}')

#--------test case 3--------#
# expected result: calculate_average([]) 
# actual result: calculate_average([]) 
numbers = []
print(f'calculate_average({numbers}) -> {calculate_average(numbers)}')
