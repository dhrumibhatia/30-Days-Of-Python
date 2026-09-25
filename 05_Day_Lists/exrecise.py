# 1. Declare an empty list
empty_list = []
print(empty_list)

# 2. Declare a list with more than 5 items
fruits = ['apple', 'banana', 'orange', 'mango', 'grape', 'lemon']
print(fruits)

# 3. Find the length of the list
print(len(fruits))

# 4. Get the first item, the middle item and the last item of the list
first_item = fruits[0]
middle_item = fruits[len(fruits) // 2]
last_item = fruits[-1]
print('First item:', first_item)
print('Middle item:', middle_item)
print('Last item:', last_item)

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['John Doe', 30, 5.9, 'Single', '123 Main St, City, Country']
print(mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print('Number of companies:', len(it_companies))

# 9. Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print('First company:', first_company)
print('Middle company:', middle_company)
print('Last company:', last_company)

# 10. Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print('Modified list:', it_companies)

#11. Add an IT company to it_companies
it_companies.append('Tesla')
print('List after adding a company:', it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'Intel')
print('List after inserting a company in the middle:', it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()   
print('List after changing a company name to uppercase:', it_companies)

# 14. Join the it_companies with a string '#;  '
joined_companies = '#;  '.join(it_companies)
print('Joined companies:', joined_companies)

# 15. Check if a certain company exists in the it_companies list.
company_to_check = 'Google'
if company_to_check in it_companies:
    print(f'{company_to_check} exists in the list.')
else:
    print(f'{company_to_check} does not exist in the list.')

# 16. Sort the list using sort() method
it_companies.sort()
print('Sorted list:', it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print('Reversed list:', it_companies)

# 18. Slice out the first 3 companies from the list
sliced_companies = it_companies[:3]
print('First 3 companies:', sliced_companies)

# 19. Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print('Last 3 companies:', last_three_companies)

# 20. Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[middle_index - 1:middle_index + 1]
else:
    middle_companies = it_companies[middle_index:middle_index + 1]
print('Middle company or companies:', middle_companies)

# 21. Remove the first IT company from the list
it_companies.pop(0)
print('List after removing the first company:', it_companies)

# 22. Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    it_companies.pop(middle_index - 1)  
else:
    it_companies.pop(middle_index)    

print('List after removing the middle company or companies:', it_companies)

# 23. Remove the last IT company from the list
it_companies.pop(-1)
print('List after removing the last company:', it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print('List after removing all companies:', it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print('Full stack:', full_stack)

# 27. Copy the full_stack list to a new list called new_full_stack
new_full_stack = full_stack.copy()
new_full_stack.extend(['Python','SQL'])  #append require two and only take one input, so I used extend to add both Python and SQL
print('New full stack:', new_full_stack)

# 1 the following list of 10 students ages, find the min, max, median, average, range and std deviation of the ages.

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

min_age = min(ages)
max_age = max(ages)
average_age = sum(ages) / len(ages)
range_age = max_age - min_age

min_difference = abs(min_age - average_age)
max_difference = abs(max_age - average_age)

print('Minimum age:', min_age)
print('Maximum age:', max_age)
print('Average age:', average_age)
print('Range of ages:', range_age)
print('Minimum difference:', min_difference)
print('Maximum difference:', max_difference)
print('Comparison:', min_difference > max_difference)

from country import countries
#imported from country.py file, which contains a list of countries

#middle country
middle_index = len(countries) // 2
print('Middle country:', countries[middle_index])

first_half = countries[:middle_index]
second_half = countries[middle_index:]

print('First half:', first_half)
print('Second half:', second_half)
print('First half length:', len(first_half))
print('Second half length:', len(second_half))

# Unpaking the first three countries and the last three countries
countries = [
    'China',
    'Russia',
    'USA',
    'Finland',
    'Sweden',
    'Norway',
    'Denmark'
]

country_one, country_two, country_three, *scandic_countries = countries

print(country_one)
print(country_two)
print(country_three)
print(scandic_countries)
