
# PYTHON FUNCTIONS — A Beginner-Friendly Guide with Examples


# A function is a reusable block of code that performs a specific task.
# You define it once and call it as many times as needed.


# 1. BASIC FUNCTION — No parameters, no return value


def greet():
    """This is a docstring — it describes what the function does."""
    print("Hello! Welcome to Python Functions.")

greet()  # Calling the function



# 2. FUNCTION WITH PARAMETERS — Accepts input values


def greet_user(name):
    """Greets a specific user by name."""
    print(f"Hello, {name}! Nice to meet you.")

greet_user("Alice")
greet_user("Bob")



# 3. FUNCTION WITH RETURN VALUE — Gives back a result


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add(10, 5)
print(f"10 + 5 = {result}")



# 4. DEFAULT PARAMETERS — Used when no argument is passed


def power(base, exponent=2):
    """Returns base raised to exponent. Default exponent is 2 (square)."""
    return base ** exponent

print(power(4))      # Uses default exponent → 4² = 16
print(power(3, 3))   # Custom exponent      → 3³ = 27



# 5. MULTIPLE RETURN VALUES — Functions can return more than one value


def min_max(numbers):
    """Returns both the minimum and maximum from a list."""
    return min(numbers), max(numbers)

low, high = min_max([3, 7, 1, 9, 4])
print(f"Min: {low}, Max: {high}")


# 6. *ARGS — Accepts any number of positional arguments


def total(*args):
    """Adds up any number of values passed to it."""
    return sum(args)

print(total(1, 2, 3))           # 3 arguments
print(total(10, 20, 30, 40))    # 4 arguments



# 7. **KWARGS — Accepts any number of keyword arguments


def show_profile(**kwargs):
    """Displays key-value pairs passed as keyword arguments."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

show_profile(name="Alice", age=25, city="Mumbai")



# 8. LAMBDA FUNCTION — A short, one-line anonymous function


square = lambda x: x * x
print(f"Square of 6: {square(6)}")

# Lambda used with built-in sorted()
students = [("Alice", 85), ("Bob", 72), ("Charlie", 91)]
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print("Ranked students:", sorted_students)



# 9. NESTED FUNCTION — A function defined inside another function


def outer():
    """Outer function that contains an inner function."""
    def inner():
        print("  I am the inner function!")
    print("Outer function called.")
    inner()  # Call the inner function from within outer

outer()



# 10. RECURSIVE FUNCTION — A function that calls itself


def factorial(n):
    """Calculates factorial of n using recursion. Example: 5! = 120"""
    if n == 0 or n == 1:   # Base case — stops the recursion
        return 1
    return n * factorial(n - 1)  # Recursive call

print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 6: {factorial(6)}")



# PUTTING IT ALL TOGETHER — A small practical example


def describe_list(label, *items, separator=", "):
    """
    Prints a labeled list of items joined by a separator.
    Uses: regular param + *args + keyword-only param
    """
    print(f"{label}: {separator.join(str(i) for i in items)}")

describe_list("Fruits", "Apple", "Mango", "Banana")
describe_list("Scores", 88, 92, 76, separator=" | ")


