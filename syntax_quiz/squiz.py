#!/usr/bin/env python

# -------------------------------------------------------
print('**** List slices')

boys = ['Leon', 'Fred', 'Jeff', 'Juan', 'Alfonso', 'Sanjeet',]

print('   ', boys[1])

print('   ', boys[-1])

print('   ', boys[2:4])

print('   ', boys[3:])

# -------------------------------------------------------
print('**** Iterating')

for name in boys[4:]:
    print('  ', name)


print('**** Iterating 2')
for index, name in enumerate(boys[4:]):
    print('  ', index, name)


print('**** Iterating 3')
for x in range(3, 6):
    print('  ', boys[x])


print('**** Iterating 4')
for x in range(0, len(boys), 3):
    print('  ', boys[x])


# -------------------------------------------------------
print('**** List comprehension')

letters = [name[0] for name in boys]
print('   ', letters)

print('**** List comprehension 2')
names = [name for name in boys if ord(name[0]) > 72]
print('   ', names)


print('**** List comprehension 3')
names = [name[0] if ord(name[0]) > 72 else '!' for name in boys]
print('   ', names)

# -------------------------------------------------------
print('**** Dictionary comprehension')

letter_map = {chr(large):chr(large + 32) for large in range(65, 92)}  
print('   ', letter_map['L'], letter_map['O'], letter_map['L'])

print('**** Dictionary comprehension 2')
letter_map = {
    chr(x):(chr(x + 13) if index < 13 else chr(65 + index - 13)) \
    for index, x in enumerate(range(65, 91))}
print('   ', letter_map)
