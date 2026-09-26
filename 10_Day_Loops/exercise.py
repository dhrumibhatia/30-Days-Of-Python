# level 1 
# 1
# for i in range(0, 11):
#     print(i)

# a=0
# while a<10:
#     print(a)
#     a+=1

#2
# for i in range(10, 0,-1):
#     print(i)

# a=10
# while a>0:
#     print(a)
#     a-=1

#3
# for i in range(0,8):
#     print('#'*i)

# a=0
# while a<8:
#     print('#'*a)
#     a+=1

#4
'''
learnings, how "for" and "while" can be using nested.
'''
# for row in range(8):
#     for column in range(8):
#         print("#", end=" ")
#     print()

# row = 0
# while row <8:
#     col = 0
#     while col<8:
#         print('#',end=' ')
#         col+=1
#     print()
#     row+=1

#5 table
# for num in range(11):
#     print(f"{num} x {num} = {num*num}")


#6
# li =['Python', 'Numpy','Pandas','Django', 'Flask']
# for item in li:
#     print(item)

#7
# for num in range(101):
#     if num%2==0:
#         print(num)

#8
# for num in range(101):
#     if num%2!=0:
#         print(num)

# level 2
#1
# sm = 0
# for num in range(101):
#     sm+=num
# print('The sum of all numbers is',sm)

#2
# sodd=0
# seven=0
# for num in range(101):
#     if num%2!=0:
#         sodd+=num
#     else:
#         seven+=num
# print(f"Sum of all evens: {seven}\nSum of all odds: {sodd}")

# level 3
#1
'''
I need to import countries from the data/countries.py file. 
I will use the import statement to do that.
but 
'''
from pathlib import Path
import sys

project_folder = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_folder))
from data.countries import countries
for i in countries:
    if 'land' in i:
        print(i)

#2
# fruits = ['banana', 'orange', 'mango', 'lemon']
# print(fruits[-1: :-1])
# print(fruits[::-1])



# understanding the pathlib lib to navigate the file system
from pathlib import Path

current_file = Path(__file__).resolve()

print("Current file:", current_file)
print("All parents:", current_file.parents)
print("parents[0]:", current_file.parents[0])
print("parents[1]:", current_file.parents[1])
print("parents[2]:", current_file.parents[2])

#3
import json
from pathlib import Path

data_file = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "countries-data.py"
)

with open(data_file, "r", encoding="utf-8") as file:
    countries_data = json.load(file)
#1.1
langsum = 0
for country in countries_data:
    langsum += len(country.get("languages", []))
print("Total number of languages:", langsum)

# dictionary.get(key, default_value)

print(countries_data[0])

print(countries_data[0].get('languages',[]))
print(len(countries_data[0].get('languages',[])))
print(type(countries_data[0]))
print(type(countries_data))

#1.2 ten most spoken languages
from collections import Counter
language_counter = Counter()

for country in countries_data:
    for language in country.get('languages', []):
        language_counter[language] += 1

print("Ten most spoken languages:")
for language, count in language_counter.most_common(10):
    print(f"{language}: {count}")
# print(language_counter)
#1.3 10 most populated countries
from collections import Counter
population_counter = Counter()

for country in countries_data:
    population_counter[country.get('name', 'Unknown')] += country.get('population', 0)

print("Ten most populated countries:")
for country, population in population_counter.most_common(10):
    print(f"{country}: {population}")
print(population_counter)