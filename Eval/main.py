def reverse_string(str):
    new_str = ''
    for val in str:
        new_str = val + new_str

    return new_str


print(reverse_string("Python is fun"))


employees = [
    {"name": "John", "salary": 3000, "designation": 'developer'},
    {"name": "Emma", "salary": 4000, "designation": 'manager'},
    {"name": "Kelly", "salary": 3500, "designation": 'tester'},
]


def find_maxsalary(employees):
    max = 0
    index = None
    for i, employee in enumerate(employees):
        if max < employee['salary']:
            max = employee['salary']
            index = i
    return employees[index]


print(find_maxsalary(employees))
