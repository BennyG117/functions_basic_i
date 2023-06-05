#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#?just prints 5 since no arguments are passed into the parameters

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#? error since first function isn't defined? or error + 5?


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#? prints 5, and doesn't print 10 since it returns 5 then stops

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#?returns just 5, then stops before 10 is printed

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#? prints 5 since x is assigned to be the answer of the above function which is 5
#! was wrong, prints 5 first, then x is assigned as the function with no areguments giving us "none"

#6
def add(b,c):
    print(b+c)
    # return b + c   (would allow it to print 3 5 8)
print(add(1,2) + add(2,3))
#?prints 3+5  = prints 8
#! prints 3, then prints 5, then error since you can't add "non types"

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#? It would print 25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#? print 100 , print 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#? 7, 14, 7 + 14 = 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#? return 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#? 500, 500, 300, 500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#? 500, 500, 300, 300, 500
#! actually 500, 500, 300, 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#? 500, 500, 300 or 500, 500, def foobar(): 
#! actually 500, 500, 300, 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#? 1, none, 2
#! forgot that bar() is a call to the function
#! actual answer 1, 3, 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#? 1, 3, 5, 10, 1, 3, 5, 10
#! reminder that L141 is just an assignment so L 142 calls the function once so the actual answer: 1, 3, 5, 10

