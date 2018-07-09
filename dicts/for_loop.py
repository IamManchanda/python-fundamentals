instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

"""
# Keys
for key in instructor.keys():
    print(key)

for value in instructor.values():
    print(value)
"""

# Items
for (key, value) in instructor.items():
    print(f"{key}: {value}")
