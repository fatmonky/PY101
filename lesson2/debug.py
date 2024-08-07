# debug.py

import pdb #remove after debugging

"""
counter = 1
breakpoint()

while counter <= 5:
    print(counter)
    pdb.set_trace()  # Add breakpoint
    counter += 1
    """
cats = []

for name in ('Powder', 'Sky', 'Cheddar', 'Cocoa'):
    cats.append(name)

print(cats) #Expected: ['Powder', 'Sky', 'Cheddar', 'Cocoa']
