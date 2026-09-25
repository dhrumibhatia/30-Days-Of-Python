# level 1
'''
1
Get user input using input(“Enter your age: ”).
If user is 18 or older, give feedback:
You are old enough to drive.
If below 18 give feedback to wait for the missing amount of years.
Output:
'''

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    years_left = 18 - age
    print(f"You need to wait {years_left} more years to drive.")

'''
2
Get user input using input("Enter your age: ").
If user is 18 or older, give feedback:
You are old enough to drive.
If below 18 give feedback to wait for the missing amount of years.
Output:
'''

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    years_left = 18 - age
    print(f"You need to wait {years_left} more years to drive.")

'''
3
Get two numbers from the user using input prompt.
If a is greater than b return a is greater than b, if a is less b 
return a is smaller than b, else a is equal to b. Output:
'''

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is smaller than {b}.")
else:
    print(f"{a} is equal to {b}.")

# level 2
'''
4
Write a code which gives grade to students according to theirs scores:
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
'''
score = int(input("Enter the student's score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

'''
5
Get the month from user input then check if the season is 
Autumn, Winter, Spring or Summer. If the user input is:
September, October or November, the season is Autumn.
December, January or February, the season is Winter. 
March, April or May, the season is Spring 
June, July or August, the season is Summer
'''
month = input("Enter the month: ")

if month in ["September", "October", "November"]:
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid month.")

'''
6
Check if a fruit is in a list of fruits.
If the fruit is in the list, print "The fruit is in the list."
If the fruit is not in the list, print "The fruit is not in the list."
'''
fruits = ["apple", "banana", "orange", "grape"]
fruit = input("Enter a fruit: ")
if fruit in fruits:
    print("The fruit is in the list.")
else:
    print("The fruit is not in the list.")

'''
7
* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
'''
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']

    print("Middle skill:", skills[len(skills) // 2])

    if 'Python' in skills:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.")

    if skills == ['JavaScript', 'React']:
        print("He is a front end developer.")
    elif skills == ['Node', 'Python', 'MongoDB']:
        print("He is a backend developer.")
    elif skills == ['React', 'Node', 'MongoDB']:
        print("He is a fullstack developer.")
    else:
        print("unknown title")

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} is married and lives in Finland.")

