# walkthrough the study of best possible way of learning lambda function such that

# lambda function : a lambda function is a small, anonymous (unnamed function ) defined using the lambda keyword
# why and when to use lambda function
# when we need a temporary function for
# sorting
# mapping
# filtering
# reducing

# basic syntax
# lambda arguments: expression
# lambda is the keyword
# argument: one or more than one parameter to be used as input parameter
# expressions: expresssion is a single return value no keyword value (no return keyword used)
 # for example
# Simple
square = lambda x: x*x
print(square(5))

# Vareint and Uses
# lambda with multiple inputs 
add = lambda x, y : x+y
print(add(2, 4))
# here in above example input will be x some element and y some element after : the operation getting started
# lambda with no arguments
greet = lambda: "Hello!"
print(greet())
# lambda with conditional expressions
max_val = lambda x, y : x if x> y else y
print(max_val(2, 3))
# map with lambda
nums = [1,2,3, 4]
squares = list(map(lambda x:x**2, nums))
print(squares)

# In this Example the input is num it is automatically iterated over the list 
## and like it take the in this way also the input part is iterated over in another after comma that's a simple way of exploring and identifying there operations
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x : x%2 == 0, nums))
print(evens)

# here the lambda function is works like the nums is iterated automatically over them 
# and filter use to filter the particular sense of data with some given condition with the lambda expression


# we can combine lambda functions inside list comprehension is several powerful ways also that does it handles all possiblity
# 1- to write compact, expressive code for filtering, mapping, or even dynamic function generatin

# Using lambda with list Comprehension
square = lambda x : x*x
newone = [square(x) for x in range(5)]
print(newone)

# using lambda with builted and iterating in that list
split = [2, 5, 6,3 , 9]
squar = lambda x: x*x
lip = [square(x) for x in split]
print(lip)

# lambda with if condition inside list comprehension
nums = [1,2,3, 4, 5,6]
ans = lambda x : x**2
preans = [ans(x) for x in nums if x%2 == 0]
print(preans)

# lambda wit if else condition expression
nums = [1, 2, 3, 4, 5, 6]
results = [(lambda x : x*2 if x%2 == 0 else x*3) (x) for x in nums]
print(results)

# cerating a list of lambda functions
funcs=[lambda x, i = i: x+i for i in range(3)]
print([f(10) for f in funcs])

# storing lambda outputs in tuples
nums = [1,2 , 3]
result = [(x, (lambda x: x**2) (x)) for x in nums]
print(result)
# in the above input part it creates a list of tuples(original, square)

# filtering and applying together
nums = [1,2, 3, 4, 5, 6]
results = [(lambda x:x*100)(x) for x in nums if x > 3]
print(results)

# apllying multiple lambdas
nums = [1,2,3]
results = [[f(x) for f in [lambda x : x+1, lambda x: x*2]] for x in nums]
print(results)