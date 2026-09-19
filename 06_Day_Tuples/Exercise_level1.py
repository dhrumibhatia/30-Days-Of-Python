# empty tuple
#1
emt_tuple = tuple()
print(emt_tuple)
#2
family = ('ram','sita','joe','jonny','jenney')
#3
brothers = ('joe','jonney')
sister = ('jenney',)

siblings = (*brothers,*sister)
print(siblings)

#4
print(len(siblings))

#5
#conversions
lis = list(siblings)
lis[0] = 'zack'
siblings= tuple(lis)
print(siblings)

father = ('shailesh',)
mother = ('roshni',)
family = siblings+father+mother
print(family)