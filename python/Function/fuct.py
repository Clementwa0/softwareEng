def greet_everyone():
    print("Hello everyone")

greet_everyone()

def family(fname, lname):
    print(fname+" "+lname)

family("Clement", "Muli")

# Arbitrary Arguments *args

def kids(*kids):
    print("The youngest kid is " + kids[2])

kids("Tobius", "matthew","Linus")

# defualt value
def my_function(country = "Norway"):
    print("I am from " + country)

my_function()

# passing a list into fucntion

def my_fuction(food):
    for  x in food:
        print(x)
fruits = ["Apple","Banana","Cherry"]

my_fuction(fruits)

# return values

def operators(x):
    return 5 * x

print(operators(3))
print(operators(5))
print(operators(6))

# Combine Positional-Only and Keyword-Only
# any args b4 the / are positional and any agrs after * are keyword only

def positional(a,b,c,/,*,d,e):
    print(a+b+c+d+e)
positional(2,3,4, d = 8,e = 10)

# recursion
def tri_al(k):
    if(k > 0):
      result = k + tri_al (k - 1)
      print(result)
    else:
        result = 0
    return result
print("Recursion Example:")
tri_al(6)
 
# lambda 
# lambda arguments : expression
x = lambda a,b: a + b
print(x(5, 6))


def myfunc(n):
    return lambda a:a*n
mydoubler = myfunc(2)

print(mydoubler(11))

mytripler = myfunc(3)

print(mytripler(11))