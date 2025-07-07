# PYTHON LIST COMPREHENSIONS & LAMBDA FUNCTIONS CHEAT SHEET
### The Ultimate Guide to Writing Concise, Badass Python Code

## 🔥 WHAT THIS COVERS:
- List comprehensions (basic to advanced)
- Lambda functions (when to use and when to say fuck no)
- Combining both for maximum Python-fu
- Performance shit you should know
- Common mistakes that'll make you look dumb

## 🚀 LIST COMPREHENSIONS

### Basic Syntax (The Bread and Butter)
```python
[do_this for each_thing in all_the_things]
# Square numbers like a boss
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16...]

# Filter even numbers while flipping off odds
evens = [x for x in range(100) if x % 2 == 0]

# Nested list? Flatten that bitch
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]  # [1, 2, 3, 4]
# If-else in one line because you're lazy
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
# ['Even', 'Odd', 'Even', 'Odd', 'Even']

# Dictionary comprehension for maximum efficiency
square_dict = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4...}
lambda arguments: do_something_with(arguments)
# Sorting with style
pairs = [(1, 'z'), (2, 'a')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])  # [(2, 'a'), (1, 'z')]

# Quick math without def-ing a whole function
add = lambda x, y: x + y
add(2, 3)  # 5 (no shit)

# Double whammy - lambda inside comprehension
operation = lambda x: x * 3
tripled = [operation(x) for x in range(4)]  # [0, 3, 6, 9]

# Filter and map like a Python gangster
result = [(lambda x: x**2)(x) for x in range(5) if x % 2 == 0]  # [0, 4, 16]
result = [
    x**2 
    for x in range(100) 
    if x % 2 == 0 
    and x > 10
]
