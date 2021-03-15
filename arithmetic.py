"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of the two inputs."""

    return num1 + num2

add(1, 2)


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return num1 - num2

subtract(10, 5)

def multiply(num1, num2):
    """Multiply the two inputs together."""

    return num1 * num2

multiply(2, 3)


def divide(num1, num2):
    """Divide the first input by the second and return the result."""

    return num1 / num2

divide(7, 2)

def square(num1):
    """Return the square of the input."""

    return num1 * num1

square(2)


def cube(num1):
    """Return the cube of the input."""

    return num1 * num1 * num1

cube(5)


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""

    return num1 ** num2

power(2, 5)

def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    return num1 % num2

mod(10, 3)

def add_mult(num1, num2, num3):
    """Returns the value of sum of num1 and num2, multiplied by sum3"""

    return (num1 + num2) * num3

add_mult(1, 2, 3)

def add_cubes(num1, num2):
    """Cube num1 and num2, then sum the output."""

    return (num1 ** 3) + (num2 ** 3)

add_cubes(2, 3)