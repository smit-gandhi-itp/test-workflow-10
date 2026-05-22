"""Math utility module for all mathematical calculations.

This module provides a comprehensive set of mathematical operations
including basic arithmetic, advanced calculations, statistical functions,
and geometric computations.
"""

import math
from typing import List, Union, Tuple
from decimal import Decimal, getcontext


class MathOperations:
    """A comprehensive class for mathematical operations."""

    def __init__(self, precision: int = 10):
        """Initialize MathOperations with specified decimal precision.
        
        Args:
            precision: Number of decimal places for precise calculations (default: 10)
        """
        self.precision = precision
        getcontext().prec = precision

    # ========== Basic Arithmetic Operations ==========

    def add(self, a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Union[float, Decimal]:
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        if isinstance(a, Decimal) or isinstance(b, Decimal):
            return Decimal(str(a)) + Decimal(str(b))
        return a + b

    def subtract(self, a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Union[float, Decimal]:
        """Subtract b from a.
        
        Args:
            a: Number to subtract from
            b: Number to subtract
            
        Returns:
            Difference of a and b
        """
        if isinstance(a, Decimal) or isinstance(b, Decimal):
            return Decimal(str(a)) - Decimal(str(b))
        return a - b

    def multiply(self, a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Union[float, Decimal]:
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        if isinstance(a, Decimal) or isinstance(b, Decimal):
            return Decimal(str(a)) * Decimal(str(b))
        return a * b

    def divide(self, a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Union[float, Decimal]:
        """Divide a by b.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Quotient of a and b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        if isinstance(a, Decimal) or isinstance(b, Decimal):
            return Decimal(str(a)) / Decimal(str(b))
        return a / b

    def power(self, base: Union[int, float], exponent: Union[int, float]) -> float:
        """Raise base to the power of exponent.
        
        Args:
            base: Base number
            exponent: Exponent
            
        Returns:
            base raised to the power of exponent
        """
        return math.pow(base, exponent)

    def modulo(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Calculate a modulo b.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Remainder of a divided by b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot calculate modulo with zero divisor")
        return a % b

    # ========== Advanced Mathematical Operations ==========

    def square_root(self, n: Union[int, float]) -> float:
        """Calculate the square root of n.
        
        Args:
            n: Number to calculate square root of
            
        Returns:
            Square root of n
            
        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(n)

    def nth_root(self, n: Union[int, float], root: int) -> float:
        """Calculate the nth root of a number.
        
        Args:
            n: Number to calculate root of
            root: Which root to calculate
            
        Returns:
            nth root of n
        """
        return math.pow(n, 1.0 / root)

    def factorial(self, n: int) -> int:
        """Calculate the factorial of n.
        
        Args:
            n: Non-negative integer
            
        Returns:
            Factorial of n
            
        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        return math.factorial(n)

    def absolute(self, n: Union[int, float]) -> Union[int, float]:
        """Calculate the absolute value of n.
        
        Args:
            n: Number
            
        Returns:
            Absolute value of n
        """
        return abs(n)

    def logarithm(self, n: Union[int, float], base: Union[int, float] = math.e) -> float:
        """Calculate the logarithm of n with specified base.
        
        Args:
            n: Number to calculate logarithm of
            base: Base of logarithm (default: e for natural log)
            
        Returns:
            Logarithm of n with specified base
            
        Raises:
            ValueError: If n is not positive or base is invalid
        """
        if n <= 0:
            raise ValueError("Logarithm is only defined for positive numbers")
        if base <= 0 or base == 1:
            raise ValueError("Invalid logarithm base")
        return math.log(n, base)

    def natural_log(self, n: Union[int, float]) -> float:
        """Calculate the natural logarithm (base e) of n.
        
        Args:
            n: Number to calculate natural logarithm of
            
        Returns:
            Natural logarithm of n
        """
        return self.logarithm(n, math.e)

    def log10(self, n: Union[int, float]) -> float:
        """Calculate the base-10 logarithm of n.
        
        Args:
            n: Number to calculate logarithm of
            
        Returns:
            Base-10 logarithm of n
        """
        return self.logarithm(n, 10)

    # ========== Trigonometric Functions ==========

    def sine(self, angle: Union[int, float], degrees: bool = False) -> float:
        """Calculate the sine of an angle.
        
        Args:
            angle: Angle value
            degrees: If True, angle is in degrees; otherwise radians (default: False)
            
        Returns:
            Sine of the angle
        """
        if degrees:
            angle = math.radians(angle)
        return math.sin(angle)

    def cosine(self, angle: Union[int, float], degrees: bool = False) -> float:
        """Calculate the cosine of an angle.
        
        Args:
            angle: Angle value
            degrees: If True, angle is in degrees; otherwise radians (default: False)
            
        Returns:
            Cosine of the angle
        """
        if degrees:
            angle = math.radians(angle)
        return math.cos(angle)

    def tangent(self, angle: Union[int, float], degrees: bool = False) -> float:
        """Calculate the tangent of an angle.
        
        Args:
            angle: Angle value
            degrees: If True, angle is in degrees; otherwise radians (default: False)
            
        Returns:
            Tangent of the angle
        """
        if degrees:
            angle = math.radians(angle)
        return math.tan(angle)

    def arcsine(self, value: Union[int, float], degrees: bool = False) -> float:
        """Calculate the arcsine (inverse sine) of a value.
        
        Args:
            value: Value between -1 and 1
            degrees: If True, return result in degrees; otherwise radians (default: False)
            
        Returns:
            Arcsine of the value
            
        Raises:
            ValueError: If value is not in range [-1, 1]
        """
        if not -1 <= value <= 1:
            raise ValueError("Arcsine is only defined for values between -1 and 1")
        result = math.asin(value)
        return math.degrees(result) if degrees else result

    def arccosine(self, value: Union[int, float], degrees: bool = False) -> float:
        """Calculate the arccosine (inverse cosine) of a value.
        
        Args:
            value: Value between -1 and 1
            degrees: If True, return result in degrees; otherwise radians (default: False)
            
        Returns:
            Arccosine of the value
            
        Raises:
            ValueError: If value is not in range [-1, 1]
        """
        if not -1 <= value <= 1:
            raise ValueError("Arccosine is only defined for values between -1 and 1")
        result = math.acos(value)
        return math.degrees(result) if degrees else result

    def arctangent(self, value: Union[int, float], degrees: bool = False) -> float:
        """Calculate the arctangent (inverse tangent) of a value.
        
        Args:
            value: Value
            degrees: If True, return result in degrees; otherwise radians (default: False)
            
        Returns:
            Arctangent of the value
        """
        result = math.atan(value)
        return math.degrees(result) if degrees else result

    # ========== Statistical Functions ==========

    def mean(self, numbers: List[Union[int, float]]) -> float:
        """Calculate the arithmetic mean (average) of a list of numbers.
        
        Args:
            numbers: List of numbers
            
        Returns:
            Mean of the numbers
            
        Raises:
            ValueError: If the list is empty
        """
        if not numbers:
            raise ValueError("Cannot calculate mean of empty list")
        return sum(numbers) / len(numbers)

    def median(self, numbers: List[Union[int, float]]) -> float:
        """Calculate the median of a list of numbers.
        
        Args:
            numbers: List of numbers
            
        Returns:
            Median of the numbers
            
        Raises:
            ValueError: If the list is empty
        """
        if not numbers:
            raise ValueError("Cannot calculate median of empty list")
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        return sorted_numbers[mid]

    def mode(self, numbers: List[Union[int, float]]) -> Union[int, float]:
        """Calculate the mode (most frequent value) of a list of numbers.
        
        Args:
            numbers: List of numbers
            
        Returns:
            Mode of the numbers
            
        Raises:
            ValueError: If the list is empty or has no unique mode
        """
        if not numbers:
            raise ValueError("Cannot calculate mode of empty list")
        frequency = {}
        for num in numbers:
            frequency[num] = frequency.get(num, 0) + 1
        max_freq = max(frequency.values())
        modes = [num for num, freq in frequency.items() if freq == max_freq]
        if len(modes) == len(numbers):
            raise ValueError("No unique mode exists")
        return modes[0]

    def variance(self, numbers: List[Union[int, float]], sample: bool = False) -> float:
        """Calculate the variance of a list of numbers.
        
        Args:
            numbers: List of numbers
            sample: If True, calculate sample variance; otherwise population variance (default: False)
            
        Returns:
            Variance of the numbers
            
        Raises:
            ValueError: If the list is empty or has only one element for sample variance
        """
        if not numbers:
            raise ValueError("Cannot calculate variance of empty list")
        if sample and len(numbers) < 2:
            raise ValueError("Sample variance requires at least 2 values")
        avg = self.mean(numbers)
        squared_diffs = [(x - avg) ** 2 for x in numbers]
        divisor = len(numbers) - 1 if sample else len(numbers)
        return sum(squared_diffs) / divisor

    def standard_deviation(self, numbers: List[Union[int, float]], sample: bool = False) -> float:
        """Calculate the standard deviation of a list of numbers.
        
        Args:
            numbers: List of numbers
            sample: If True, calculate sample standard deviation; otherwise population (default: False)
            
        Returns:
            Standard deviation of the numbers
        """
        return math.sqrt(self.variance(numbers, sample))

    def range_value(self, numbers: List[Union[int, float]]) -> Union[int, float]:
        """Calculate the range (max - min) of a list of numbers.
        
        Args:
            numbers: List of numbers
            
        Returns:
            Range of the numbers
            
        Raises:
            ValueError: If the list is empty
        """
        if not numbers:
            raise ValueError("Cannot calculate range of empty list")
        return max(numbers) - min(numbers)

    # ========== Geometric Functions ==========

    def circle_area(self, radius: Union[int, float]) -> float:
        """Calculate the area of a circle.
        
        Args:
            radius: Radius of the circle
            
        Returns:
            Area of the circle
            
        Raises:
            ValueError: If radius is negative
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius ** 2

    def circle_circumference(self, radius: Union[int, float]) -> float:
        """Calculate the circumference of a circle.
        
        Args:
            radius: Radius of the circle
            
        Returns:
            Circumference of the circle
            
        Raises:
            ValueError: If radius is negative
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return 2 * math.pi * radius

    def rectangle_area(self, length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
        """Calculate the area of a rectangle.
        
        Args:
            length: Length of the rectangle
            width: Width of the rectangle
            
        Returns:
            Area of the rectangle
            
        Raises:
            ValueError: If length or width is negative
        """
        if length < 0 or width < 0:
            raise ValueError("Dimensions cannot be negative")
        return length * width

    def rectangle_perimeter(self, length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
        """Calculate the perimeter of a rectangle.
        
        Args:
            length: Length of the rectangle
            width: Width of the rectangle
            
        Returns:
            Perimeter of the rectangle
            
        Raises:
            ValueError: If length or width is negative
        """
        if length < 0 or width < 0:
            raise ValueError("Dimensions cannot be negative")
        return 2 * (length + width)

    def triangle_area(self, base: Union[int, float], height: Union[int, float]) -> Union[int, float]:
        """Calculate the area of a triangle.
        
        Args:
            base: Base of the triangle
            height: Height of the triangle
            
        Returns:
            Area of the triangle
            
        Raises:
            ValueError: If base or height is negative
        """
        if base < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative")
        return 0.5 * base * height

    def sphere_volume(self, radius: Union[int, float]) -> float:
        """Calculate the volume of a sphere.
        
        Args:
            radius: Radius of the sphere
            
        Returns:
            Volume of the sphere
            
        Raises:
            ValueError: If radius is negative
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return (4 / 3) * math.pi * radius ** 3

    def sphere_surface_area(self, radius: Union[int, float]) -> float:
        """Calculate the surface area of a sphere.
        
        Args:
            radius: Radius of the sphere
            
        Returns:
            Surface area of the sphere
            
        Raises:
            ValueError: If radius is negative
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return 4 * math.pi * radius ** 2

    def cylinder_volume(self, radius: Union[int, float], height: Union[int, float]) -> float:
        """Calculate the volume of a cylinder.
        
        Args:
            radius: Radius of the cylinder base
            height: Height of the cylinder
            
        Returns:
            Volume of the cylinder
            
        Raises:
            ValueError: If radius or height is negative
        """
        if radius < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative")
        return math.pi * radius ** 2 * height

    def distance_2d(self, x1: Union[int, float], y1: Union[int, float], 
                    x2: Union[int, float], y2: Union[int, float]) -> float:
        """Calculate the Euclidean distance between two points in 2D space.
        
        Args:
            x1: X-coordinate of first point
            y1: Y-coordinate of first point
            x2: X-coordinate of second point
            y2: Y-coordinate of second point
            
        Returns:
            Distance between the two points
        """
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def distance_3d(self, x1: Union[int, float], y1: Union[int, float], z1: Union[int, float],
                    x2: Union[int, float], y2: Union[int, float], z2: Union[int, float]) -> float:
        """Calculate the Euclidean distance between two points in 3D space.
        
        Args:
            x1: X-coordinate of first point
            y1: Y-coordinate of first point
            z1: Z-coordinate of first point
            x2: X-coordinate of second point
            y2: Y-coordinate of second point
            z2: Z-coordinate of second point
            
        Returns:
            Distance between the two points
        """
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    # ========== Number Theory Functions ==========

    def is_prime(self, n: int) -> bool:
        """Check if a number is prime.
        
        Args:
            n: Integer to check
            
        Returns:
            True if n is prime, False otherwise
        """
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def gcd(self, a: int, b: int) -> int:
        """Calculate the greatest common divisor of two integers.
        
        Args:
            a: First integer
            b: Second integer
            
        Returns:
            Greatest common divisor of a and b
        """
        return math.gcd(a, b)

    def lcm(self, a: int, b: int) -> int:
        """Calculate the least common multiple of two integers.
        
        Args:
            a: First integer
            b: Second integer
            
        Returns:
            Least common multiple of a and b
        """
        return abs(a * b) // math.gcd(a, b)

    def fibonacci(self, n: int) -> int:
        """Calculate the nth Fibonacci number.
        
        Args:
            n: Position in Fibonacci sequence (0-indexed)
            
        Returns:
            nth Fibonacci number
            
        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative indices")
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    # ========== Conversion Functions ==========

    def degrees_to_radians(self, degrees: Union[int, float]) -> float:
        """Convert degrees to radians.
        
        Args:
            degrees: Angle in degrees
            
        Returns:
            Angle in radians
        """
        return math.radians(degrees)

    def radians_to_degrees(self, radians: Union[int, float]) -> float:
        """Convert radians to degrees.
        
        Args:
            radians: Angle in radians
            
        Returns:
            Angle in degrees
        """
        return math.degrees(radians)

    def celsius_to_fahrenheit(self, celsius: Union[int, float]) -> float:
        """Convert Celsius to Fahrenheit.
        
        Args:
            celsius: Temperature in Celsius
            
        Returns:
            Temperature in Fahrenheit
        """
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit: Union[int, float]) -> float:
        """Convert Fahrenheit to Celsius.
        
        Args:
            fahrenheit: Temperature in Fahrenheit
            
        Returns:
            Temperature in Celsius
        """
        return (fahrenheit - 32) * 5/9


# Convenience functions for quick access without instantiating the class

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Quick add function."""
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Quick subtract function."""
    return a - b

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Quick multiply function."""
    return a * b

def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """Quick divide function."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base: Union[int, float], exponent: Union[int, float]) -> float:
    """Quick power function."""
    return math.pow(base, exponent)

def square_root(n: Union[int, float]) -> float:
    """Quick square root function."""
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(n)
