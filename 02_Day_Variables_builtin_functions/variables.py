
# Variables in Python

first_name = 'dhrumil'
last_name = 'bhatia'
country = 'india'
city = 'bharuch'
age = 25
is_married = False
skills = ['HTML', 'CSS', 'ml', 'django', 'Python','sql']
person_info = {
    'firstname': 'dhrumil',
    'lastname': 'bhatia',
    'country': 'india',
    'city': 'bharuch'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'dhrumil', 'bhatia', 'india', 25, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
