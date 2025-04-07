#string
#string is a sequence of characters
#string is immutable
#string is ordered
#string is indexed
#string is iterable
#string is mutable
#string is immutable

#string are arrays
a = "hello";
print(a[1]);

#looping through a string
for x in "banana":
    print(x);

#string length
print(len(a));

#check string
txt = "The best things in life are free!";
print("free" in txt);

#check if not
print("expensive" not in txt);

#string slicing
b = "Hello, World!";
print(b[:5]);
print(b[2:5]);

#string slicing
print(b[-5:-2]);

#string slicing
print(b[2:]);

#Modify Strings
a = "Hello, World!";
print(a.upper());
print(a.lower());

#Remove Whitespace
a = " Hello, World! ";
print(a.strip());

#Replace String
a = "Hello, World!";
print(a.replace("H", "J"));

#Split String
a = "Hello, World!";
print(a.split(","));

#String Concatenation
a = "Hello";
b = "World";
print(a + b);

