# 📘 Python Project: List Comprehension & Lambda Functions

Welcome to this Python project where we explore the power of **List Comprehension** and **Lambda Functions** — two powerful tools in Python that help write **cleaner**, **more readable**, and **more concise** code.

---

## 🔍 What This Project Covers

- ✅ List Comprehension (Basics to Advanced)
- ✅ Nested List Comprehension
- ✅ Conditional List Comprehension
- ✅ Lambda (Anonymous) Functions
- ✅ Using Lambda with `map()`, `filter()`, and `reduce()`
- ✅ Real-world examples and utility scripts

---

## 🧠 Why These Concepts Matter

- **List Comprehension** simplifies loops and makes data transformations elegant.
- **Lambda Functions** let you write functions in a single line — especially useful for quick operations.

These techniques are **crucial for Pythonic coding**, especially in:
- Data Science
- Functional Programming
- One-liners in real-world code

---

## 🧪 Example Snippets

### ✅ List Comprehension
```python
# Squares of even numbers
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

### ✅ Lambda with `map()`
```python
# Convert a list of strings to uppercase
words = ["hello", "world"]
upper_words = list(map(lambda w: w.upper(), words))
```

### ✅ Lambda with `filter()`
```python
# Filter out only odd numbers
numbers = [1, 2, 3, 4, 5]
odds = list(filter(lambda x: x % 2 != 0, numbers))
```

### ✅ Lambda with `reduce()`
```python
from functools import reduce

# Calculate product of all elements
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
```

---

## 📂 Project Structure

```
├── list_comprehension_examples.py
├── lambda_examples.py
├── README.md
└── requirements.txt
```

---

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-list-lambda.git
   cd python-list-lambda
   ```

2. Run examples:
   ```bash
   python list_comprehension_examples.py
   python lambda_examples.py
   ```

---

## 📚 Recommended Prerequisites

- Python 3.6+
- Basic understanding of loops and functions

---

## 📖 References

- [Python Docs - List Comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Python Docs - Lambda Functions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

---

## 👨‍💻 Author

**Mannu Chaurasiya**  
Python Enthusiast | Final Year CSE (Data Science)
