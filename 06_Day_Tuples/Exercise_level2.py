#1
family = ('zack', 'jonney', 'jenney', 'shailesh', 'roshni')
siblings = family[0:3]
parents = family[3:]
print(siblings,parents)

#2
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'potato', 'spinach')
animal_products = ('milk', 'cheese', 'eggs')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#3
food_stuff_lt = food_stuff_tp

#4
print(food_stuff_tp[(len(food_stuff_tp)//2)-1])

#5
print(food_stuff_tp[0:3]+food_stuff_tp[-3:])

#6
del food_stuff_tp
# print(food_stuff_tp) this will give erro as dilited tuple

# 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)