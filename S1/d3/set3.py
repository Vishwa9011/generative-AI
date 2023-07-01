# Tuple Unpacking: Create a list of tuples, each containing a name and an age.
# Then, use tuple unpacking to iterate through the list and print each name and age.


list = [("John", 25), ("Jane", 30)]
str = ''
for data in list:
    str += (f"{data[0]} is {data[1]} years old. ")

print(str)


# Dictionary Manipulation: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
