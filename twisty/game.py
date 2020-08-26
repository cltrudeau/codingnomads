#!/usr/bin/env python

rooms = {
    'centre':{
        'description': 'You are in the middle',
        'east':'left',
        'west':'right',
    },
    'left': {
        'description': 'You can see the sun through the window',
        'west':'centre',
    },
    'right': {
        'description': 'You smell bagels',
        'east':'centre',
    },

}

current = 'centre'
print('What is your name?')
response = input('> ')

while True:
    print(rooms[current]['description'])
    choices = list(rooms[current].keys())
    choices.remove('description')
    directions = ','.join(choices)

    print(f'\nWhere would you like to go ({directions})?')
    response = input('> ')
    reponse = response.lower()

    if response == 'quit':
        exit()

    if response in choices:
        current = rooms[current][response]
        print('You are travelling', response)
        print()
        continue

    # bad choice
    print(f'You chose "{response}", which was not a choice')
