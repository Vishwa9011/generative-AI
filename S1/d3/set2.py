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
    if (i > 150):
        continue
    elif i > 500:
        break
    elif (i % 5 == 0):
        print(i)
