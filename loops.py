# for loop

# print("Counting from 1 to 5:")

# for i in range(1,6):
#     print(i)

# print("\nReversed condition from 5 to 1:")
# for i in range(5,0 -1):
#     print(i)

# # while loop
# count = 1

# while count <= 20 :
#     print(count)
#     count += 1

# count = 10
# print("\nReversed While loop")
# while count >= 1 :
#     print(count)
#     count -= 1

# #  looping thru a list 
# fruits = ["apple", "bananna","cherry"]
# print("My fruits")
# for fruit in fruits:
#     print(fruit)

# print("My fruits")
# for fruit in reversed (fruits):
#     print(fruit)

# # loop with enumerate
print("Fruits with indicies")
for index, fruit in enumerate(fruits):
    print(f"{index}:{fruit}")

# looping with dictionaries
person = {
    "name":"Clement",
    "age":30,
    "city":"NYC",
    "pno": 72020202
}

print("\nPerson Details")
for key,value in person.items():
    print(f"{key}:{value}")

# list compehesion

squares = [x**2 for x in range (1,6)]
print("Square of 1 to 5 ", squares)

# for loop with zip()

colors = [1,2,3 4 , 5]

print()