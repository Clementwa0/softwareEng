# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "electric": False,
#     "colors": ["red", "white", "blue"],
# }
# thisdict.update({'year':2020})
# x = thisdict.items()

# print(x)
# print(len(thisdict))
# print(thisdict)

student = {
    "name":"Emma",
    "age":23,
    "courses":["Math","Computer Science"]
}

print(student["name"])
student["grade"] = "A"
student["age"]  += 24
print(student)
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(f"\nloops:{key}:{value}")

# sets

color = {"red","blue","white"}
print(color)

# Tuples
coord 