#  print the pattern

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

str = ''
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


'''
Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

- The number must be divisible by five
- If the number is greater than 150, then skip it and move to the next number
- If the number is greater than 500, then stop the loop
'''

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break
    elif (i > 150):
        continue
    elif (i % 5 == 0):
        print(i)


# Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"

half = int(len(s1) / 2)
print(half)

start_half = s1[:half]
end_half = s1[half:]

str = start_half + s2 + end_half
print("ans", str)

# Given string contains a combination of the lower and upper case letters.
#  Write a program to arrange the characters of a string so that all lowercase letters should come first.

str = "PyNaTive"
lower = ''
upper = ''
for letter in str:
    if letter.lower() == letter:
        lower += letter
    else:
        upper += letter

print(lower + upper)


# Write a program to add two lists index-wise. Create a new list that contains the 0th index
# item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

newList = []
for i in range(len(list1)):
    newList.append(list1[i] + list2[i])

print(newList)


# Given a two Python list. Write a program to iterate both lists simultaneously and display
# items from list1 in original order and items from list2 in reverse order.
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i in range(len(list1)):
    print(list1[i], list2[len(list2)-1-i])


# In Python, we can initialize the keys with the same values.
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dict = {}

for employee in employees:
    dict[employee] = defaults

print(dict)

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

new_dict = {}

for key in keys:
    new_dict[key] = sample_dict[key]

print(new_dict)


# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)
