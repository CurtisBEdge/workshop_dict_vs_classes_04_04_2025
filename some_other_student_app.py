from toy import Toy

toys = [
    {
        "name": "Ball",
        "colour": "red"
    },
    {
        "name": "Teddy",
        "colour": "brown"
    }
]

# Make a toys list with at least 2 dictionaries representing a toy with name and colour DONE

# create a function to print out the name of all toys

# create a function to print out all colours of toys. print(print_colours()) => ['red', 'green']

# Now do this with classes

def all_toys(toys):
    for toy in toys:
        print(toy['name'])
        
def all_toy_colours(toys):
    for toy in toys:
        print(toy['colour'])

all_toys(toys)
all_toy_colours(toys)

more_toys = []

more_toys.append()