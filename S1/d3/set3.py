# Tuple Unpacking: Create a list of tuples, each containing a name and an age.
# Then, use tuple unpacking to iterate through the list and print each name and age.


from queue import Queue
list = [("John", 25), ("Jane", 30)]
str = ''
for data in list:
    str += (f"{data[0]} is {data[1]} years old. ")

print(str)


# Dictionary Manipulation: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
# Create an empty dictionary
name_age_dict = {}

# Function to add a new name-age pair


def add_name_age(name, age):
    name_age_dict[name] = age
    print(f"Added {name} with age {age} to the dictionary.")

# Function to update the age of a name


def update_age(name, age):
    if name in name_age_dict:
        name_age_dict[name] = age
        print(f"Updated age of {name} to {age} in the dictionary.")
    else:
        print(f"{name} is not found in the dictionary.")

# Function to delete a name from the dictionary


def delete_name(name):
    if name in name_age_dict:
        del name_age_dict[name]
        print(f"Deleted {name} from the dictionary.")
    else:
        print(f"{name} is not found in the dictionary.")


add_name_age("John", 25)
add_name_age("Alice", 30)
add_name_age("Bob", 40)

print(name_age_dict)  # Output: {'John': 25, 'Alice': 30, 'Bob': 40}

update_age("John", 26)
delete_name("Alice")

print(name_age_dict)  # Output: {'John': 26, 'Bob': 40}

# Two Sum Problem: Given an array of integers and a target integer, find the two integers in the array that sum to the target.

arr = [2, 11, 7, 3]
target = 9

arr.sort()

i = 0
j = len(arr) - 1
while (i < j):
    sum = arr[i] + arr[j]
    if sum == target:
        print(f"{i},{j}")
        break
    elif sum < target:
        i += 1
    else:
        j -= 1


# Palindrome Check: Write a Python function that checks whether a given word or phrase is a palindrome.

str = "racecar"

new_str = str[::-1]

print("Pallindrome") if str == new_str else print("not a Pallindrome")


# Selection sort
def selection_sort(arr):
    n = len(arr)

    # Traverse the entire list
    for i in range(n):
        # Find the minimum element in the unsorted portion
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the minimum element with the current element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Example usage
my_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(my_list)
print(sorted_list)  # Output: [11, 12, 22, 25, 64]


# implemenation of stack using queue


class Stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, value):
        # Add the new element to queue1
        self.queue1.put(value)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"

        # Transfer elements from queue1 to queue2, leaving the last element in queue1
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())

        # Remove and return the last element from queue1 (simulating stack's behavior)
        value = self.queue1.get()

        # Swap the names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

        return value

    def is_empty(self):
        return self.queue1.empty()


# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1
print(stack.pop())  # Output: Stack is empty


# Exception Handling: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."


# Example usage
num1 = 10
num2 = 0

division_result = divide_numbers(num1, num2)
print(division_result)  # Output: Error: Division by zero is not allowed.
