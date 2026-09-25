print('Thirty', 'Days', 'Of', 'Python', sep='')
print('Coding', 'For', 'All', sep=' ')
company = 'Coding For All'
print(company)
print('Length of company string:', len(company))

print('Company in uppercase:', company.upper())
print('Company in lowercase:', company.lower())
print('Company title:', company.title())
print('Company swapcase:', company.swapcase())
print('Company capitalized:', company.capitalize())
print(company[7:])
print(company.find('Coding'))
print(company.replace('Coding', 'Python'))
print('Python for Everyone'.replace('Everyone', 'All'))
print(company.split())
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(','))
print(company[0])
print(company[-1])
print(company[10])

#18
com = 'Python For Everyone'
com1 = 'Coding For All'
sp1 = com.split()
sp2 = com1.split()
print(''.join([i[0] for i in sp1]))
print(''.join([i[0] for i in sp2]))

sent ='You cannot end a sentence with because because because is a conjunction'
print('Index of "because":', sent.index('because'))
print('Last index of "because":', sent.rindex('because'))
print(sent.find('because'))
print(sent[31:54])
print(sent[:31] + sent[55:])

#28,29,30
print(com1.startswith('Coding'))
print(com1.endswith('coding'))
print('   Coding For All      '.strip())

#31 valid string variable or not? using isidentifier()
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

plib= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(plib))

# \n \t
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2

print(f"The area of a circle with radius {radius} is {area:.0f} meters square.")

a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")