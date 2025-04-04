from names import get_random_name

persons = [
    {
        "name": get_random_name(),
        "hobbies": [
            "tennis",
            "Warcraft 3"
        ]
    },
    {
        "name": get_random_name(),
        "hobbies": [
            "reading",
            "collecting diecast cars"
        ]
    }
]

# Make a persons list with at least 2 dictionaries representing a person with hobbies - DONE

# create a function to print out the name of the persons
for person in persons:
    print(person["name"])

# create a function to print out all hobbies of the persons eg. print(all_hobbies()) => ['tennis', 'working out', 'maths']
hobbies = []
for person in persons:
    for hobby in person["hobbies"]:
        hobbies.append(hobby)

print(hobbies)