# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# 1 Find the lenght of the set it_companies
print(len(it_companies))

# 2 Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3 Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Snapchat', 'TikTok'])
print(it_companies)

# 4 Remove one of the companies from the set it_companies
it_companies.remove('Snapchat')
print(it_companies)

# 5 What is the difference between remove and discard
# remove raises a KeyError if the element is not found
# discard does not raise an error if the element is not found

# example of remove
# it_companies.remove('Snapchat')  # This will raise a KeyError since 'Snapchat' has already been removed

#example of discard
it_companies.discard('Snapchat')  # This will not raise an error even though 'Snapchat' is not in the set   

# level 2
# 1 join A and B
print(A.union(B))

# 2 Find A intersection B
print(A.intersection(B))

# 3 Is A subset of B
print(A.issubset(B))

# 4 Are A and B disjoint sets
print(A.isdisjoint(B))

# 5 Join A with B and B with A
print(A.union(B))
print(B.union(A))

# 6 What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# 7 Delete the sets completely
del A
del B

# level 3
# 1 Convert the ages to a set and compare the length of the list and the set
age_set = set(age)
print(f"Length of the list: {len(age)}")
print(f"Length of the set: {len(age_set)}") #set removes duplicates, so the length of the set will be less than or equal to the length of the list

# 2 Explain the difference between the following data types: string, list, tuple and set
# String: A string is a sequence of characters enclosed in quotes. It is immutable, meaning that once created, it cannot be changed. Strings are used to represent text data.
# List: A list is an ordered collection of items that can be changed. Lists are mutable, meaning that you can modify the elements after the list is created. Lists are defined with square brackets.
# Tuple: A tuple is similar to a list, but it is immutable. Once a tuple is created, its elements cannot be changed. Tuples are defined with parentheses.
# Set: A set is an unordered collection of unique items. Sets are mutable, but they
# do not allow duplicate elements. Sets are defined with curly braces.

# 3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print(f"Number of unique words: {len(unique_words)}")