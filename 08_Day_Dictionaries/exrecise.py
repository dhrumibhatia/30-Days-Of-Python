# 1 create an empty dictionary called dog
dog = {}

#2 Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 3

# 3 Create a student dictionary and add first_name, last_name, gender, age, marital_status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript', 'SQL'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

# 4 Get the length of the student dictionary
print('Length of student dictionary:', len(student))

# 5 Get the value of skills and check the data type, it should be a list
print('Skills:', student['skills'])
print('Data type of skills:', type(student['skills']))

# 6 Modify the skills values by adding one or two skills
student['skills'].append('HTML')
student['skills'].append('CSS')

# 7 Get the dictionary keys as a list
keys_list = list(student.keys())

# 8 Get the dictionary values as a list
values_list = list(student.values())
print('Keys:', keys_list)
print('Values:', values_list)

# 9 Create a dictionary to a list of tuples using the items() method
items_list = list(student.items())
print('Items:', items_list)

# 10 Delete one of the items in the dictionary
del student['marital_status']

#11 Clear the dictionary
student.clear()


