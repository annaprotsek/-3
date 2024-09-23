def average_of_digits(number):
    digits = [int(digit) for digit in str(number)]
    return sum(digits) / len(digits)
number = int(input("Введіть тризначне число: "))
average = average_of_digits(number)
print(f"Середнє арифметичне цифр числа: {average}")