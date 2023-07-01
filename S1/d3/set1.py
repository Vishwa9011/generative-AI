import math

print("Hello world!")


# Data Type Play: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.

a = 5
b = 1.2
c = "karan"
d = True
e = [1, 2, 3, 4]
f = (1, 2, 3, 4)
g = {
    "value": "pair"
}

h = set()
h.add(1)
h.update([5])
print("set", h)


# List Operations: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list

list = []
for i in range(1, 11):
    list.append(i)

print(list)

# Sum and Average: Write a Python program that calculates and prints the sum and average of a list of numbers.
list = [1, 2, 3, 4, 5]
sum = 0
for i in range(len(list)):
    sum += list[i]

print('average', sum / len(list))

# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.

str = "karan"
print("reverrsed", str[::-1])

# Count Vowels: Write a Python program that counts the number of vowels in a given string.
str = 'karan'
vowel = 'aeiou'
count = 0
for i in range(len(str)):
    if (str[i] in vowel):
        count += 1

print(f'vowel count in {str}', count)


# Prime number
def is_prime(number):
    if (number < 2):
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i == 0):
            return False
    return True


print("Prime number" if is_prime(11) else "Not Prime")


# Factorial Calculation: Write a Python function that calculates the factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))


# Fibonacci
def fibonacci_sequence(n):
    sequence = []

    # First two numbers in the sequence
    if n >= 1:
        sequence.append(0)
    if n >= 2:
        sequence.append(1)

    # Generate the remaining numbers
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)

    return sequence


n = 10
fib_numbers = fibonacci_sequence(n)
print(fib_numbers)


# 10 square
squares = [x**2 for x in range(1, 11)]
print(squares)
