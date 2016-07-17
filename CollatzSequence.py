# The simplest impossible maths problem
def collatz(number):
    number2 = number % 2
    if number2 == 0:
        number3 = (number // 2)
        print(number3)
        return number3
    if number2 == 1:
        number3 = (3 * number + 1)
        print(number3)
        return number3

print('Please enter a whole number')
try:
    number = int(input())
    while number != 1:
        number = collatz(number)
except ValueError:
    print('That was not a whole number')




