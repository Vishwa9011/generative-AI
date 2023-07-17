def isPallindrome(num):
    temp = str(num)
    for i in range(int(len(temp) / 2)):
        if temp[i] != temp[len(temp)-1-i]:
            return False
    return True

res = isPallindrome(11211)
print(res)


company = {
    'employees': {
        'John': {'age': 35, 'job_title': 'Manager'},
        'Emma': {'age': 28, 'job_title': 'Software Engineer'},
        'Kelly': {'age': 41, 'job_title': 'Senior Developer'},
        'Sam': {'age': 30, 'job_title': 'Software Engineer'},
        'Mark': {'age': 37, 'job_title': 'Senior Manager'},
        'Sara': {'age': 32, 'job_title': 'Software Engineer'},
    }
}

def average_age_of_employees_with_s_job_title(company):
    total_age = 0;
    count = 0
    for i,val in enumerate(company["employees"]):
        if company['employees'][val]['job_title'][0] == 'S':
            count+=1
            total_age += company['employees'][val]['age']            
    return total_age/count


print(average_age_of_employees_with_s_job_title(company))  # 31.0
