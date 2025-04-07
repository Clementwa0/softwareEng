#lists
a = [1, 2, 3, 4, 5];
print(a);

#accessing elements
print(a[0]);
print(a[-1]);


#changing elements
a[0] = 10;
print(a);

#adding elements
a.append(6);

#removing elements
a.remove(3);
print(a);

#popping elements
a.pop(0);
print(a);



#looping through lists
for x in a:
    print(x);

#looping through lists with index
for i in range(len(a)):
    print(a[i]);
#while loop
i = 0;
while i < len(a):
    print(a[i]);
    i += 1;

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


#sorting lists
a.sort();
print(a);

#sorting lists in reverse order
a.sort(reverse=True);
print(a);

#copying lists
b = a.copy();
print(b);

#joining lists
c = a + b;
print(c);

#list methods
a.append(6);
print(a);

a.insert(0, 0);
print(a);

a.remove(6);
print(a);

a.pop();
print(a);   

a.clear();
print(a);

a.count(6);
print(a);   

a.extend(b);
print(a);

a.index(6);
print(a);   

a.reverse();
print(a);

a.sort();
print(a);   



