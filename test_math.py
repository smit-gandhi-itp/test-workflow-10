"""Unit tests for the math module.

This test suite provides comprehensive coverage of all mathematical
operations defined in the math.py module.
"""

import unittest
import math
from decimal import Decimal
from math import MathOperations


class TestMathOperations(unittest.TestCase):
    """Test cases for MathOperations class."""

    def setUp(self):
        """Set up test fixtures."""
        self.math_ops = MathOperations(precision=10)

    # ========== Basic Arithmetic Tests ==========

    def test_add(self):
        """Test addition operation."""
        self.assertEqual(self.math_ops.add(5, 3), 8)
        self.assertEqual(self.math_ops.add(-5, 3), -2)
        self.assertEqual(self.math_ops.add(0, 0), 0)
        self.assertAlmostEqual(self.math_ops.add(0.1, 0.2), 0.3, places=10)

    def test_add_decimal(self):
        """Test addition with Decimal precision."""
        result = self.math_ops.add(Decimal('0.1'), Decimal('0.2'))
        self.assertEqual(result, Decimal('0.3'))

    def test_subtract(self):
        """Test subtraction operation."""
        self.assertEqual(self.math_ops.subtract(10, 3), 7)
        self.assertEqual(self.math_ops.subtract(-5, -3), -2)
        self.assertEqual(self.math_ops.subtract(0, 5), -5)

    def test_multiply(self):
        """Test multiplication operation."""
        self.assertEqual(self.math_ops.multiply(5, 3), 15)
        self.assertEqual(self.math_ops.multiply(-5, 3), -15)
        self.assertEqual(self.math_ops.multiply(0, 100), 0)

    def test_divide(self):
        """Test division operation."""
        self.assertEqual(self.math_ops.divide(10, 2), 5)
        self.assertAlmostEqual(self.math_ops.divide(7, 3), 2.333333, places=5)
        with self.assertRaises(ValueError):
            self.math_ops.divide(10, 0)

    def test_power(self):
        """Test power operation."""
        self.assertEqual(self.math_ops.power(2, 3), 8)
        self.assertEqual(self.math_ops.power(5, 0), 1)
        self.assertAlmostEqual(self.math_ops.power(4, 0.5), 2, places=10)

    def test_modulo(self):
        """Test modulo operation."""
        self.assertEqual(self.math_ops.modulo(10, 3), 1)
        self.assertEqual(self.math_ops.modulo(15, 5), 0)
        with self.assertRaises(ValueError):
            self.math_ops.modulo(10, 0)

    # ========== Advanced Mathematical Operations Tests ==========

    def test_square_root(self):
        """Test square root calculation."""
        self.assertEqual(self.math_ops.square_root(16), 4)
        self.assertEqual(self.math_ops.square_root(0), 0)
        self.assertAlmostEqual(self.math_ops.square_root(2), 1.414213, places=5)
        with self.assertRaises(ValueError):
            self.math_ops.square_root(-1)

    def test_nth_root(self):
        """Test nth root calculation."""
        self.assertAlmostEqual(self.math_ops.nth_root(27, 3), 3, places=10)
        self.assertAlmostEqual(self.math_ops.nth_root(16, 4), 2, places=10)

    def test_factorial(self):
        """Test factorial calculation."""
        self.assertEqual(self.math_ops.factorial(0), 1)
        self.assertEqual(self.math_ops.factorial(5), 120)
        self.assertEqual(self.math_ops.factorial(10), 3628800)
        with self.assertRaises(ValueError):
            self.math_ops.factorial(-1)

    def test_absolute(self):
        """Test absolute value calculation."""
        self.assertEqual(self.math_ops.absolute(-5), 5)
        self.assertEqual(self.math_ops.absolute(5), 5)
        self.assertEqual(self.math_ops.absolute(0), 0)

    def test_logarithm(self):
        """Test logarithm calculation."""
        self.assertAlmostEqual(self.math_ops.logarithm(100, 10), 2, places=10)
        self.assertAlmostEqual(self.math_ops.logarithm(8, 2), 3, places=10)
        with self.assertRaises(ValueError):
            self.math_ops.logarithm(0, 10)
        with self.assertRaises(ValueError):
            self.math_ops.logarithm(-5, 10)

    def test_natural_log(self):
        """Test natural logarithm calculation."""
        self.assertAlmostEqual(self.math_ops.natural_log(math.e), 1, places=10)
        self.assertAlmostEqual(self.math_ops.natural_log(1), 0, places=10)

    def test_log10(self):
        """Test base-10 logarithm calculation."""
        self.assertEqual(self.math_ops.log10(1000), 3)
        self.assertEqual(self.math_ops.log10(100), 2)

    # ========== Trigonometric Functions Tests ==========

    def test_sine(self):
        """Test sine calculation."""
        self.assertAlmostEqual(self.math_ops.sine(0), 0, places=10)
        self.assertAlmostEqual(self.math_ops.sine(math.pi / 2), 1, places=10)
        self.assertAlmostEqual(self.math_ops.sine(90, degrees=True), 1, places=10)

    def test_cosine(self):
        """Test cosine calculation."""
        self.assertAlmostEqual(self.math_ops.cosine(0), 1, places=10)
        self.assertAlmostEqual(self.math_ops.cosine(math.pi), -1, places=10)
        self.assertAlmostEqual(self.math_ops.cosine(180, degrees=True), -1, places=10)

    def test_tangent(self):
        """Test tangent calculation."""
        self.assertAlmostEqual(self.math_ops.tangent(0), 0, places=10)
        self.assertAlmostEqual(self.math_ops.tangent(math.pi / 4), 1, places=10)
        self.assertAlmostEqual(self.math_ops.tangent(45, degrees=True), 1, places=10)

    def test_arcsine(self):
        """Test arcsine calculation."""
        self.assertAlmostEqual(self.math_ops.arcsine(0), 0, places=10)
        self.assertAlmostEqual(self.math_ops.arcsine(1), math.pi / 2, places=10)
        with self.assertRaises(ValueError):
            self.math_ops.arcsine(2)

    def test_arccosine(self):
        """Test arccosine calculation."""
        self.assertAlmostEqual(self.math_ops.arccosine(1), 0, places=10)
        self.assertAlmostEqual(self.math_ops.arccosine(0), math.pi / 2, places=10)
        with self.assertRaises(ValueError):
            self.math_ops.arccosine(2)

    def test_arctangent(self):
        """Test arctangent calculation."""
        self.assertAlmostEqual(self.math_ops.arctangent(0), 0, places=10)
        self.assertAlmostEqual(self.math_ops.arctangent(1), math.pi / 4, places=10)

    # ========== Statistical Functions Tests ==========

    def test_mean(self):
        """Test mean calculation."""
        self.assertEqual(self.math_ops.mean([1, 2, 3, 4, 5]), 3)
        self.assertEqual(self.math_ops.mean([10, 20, 30]), 20)
        with self.assertRaises(ValueError):
            self.math_ops.mean([])

    def test_median(self):
        """Test median calculation."""
        self.assertEqual(self.math_ops.median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(self.math_ops.median([1, 2, 3, 4]), 2.5)
        self.assertEqual(self.math_ops.median([5]), 5)
        with self.assertRaises(ValueError):
            self.math_ops.median([])

    def test_mode(self):
        """Test mode calculation."""
        self.assertEqual(self.math_ops.mode([1, 2, 2, 3, 4]), 2)
        self.assertEqual(self.math_ops.mode([5, 5, 5, 1, 2]), 5)
        with self.assertRaises(ValueError):
            self.math_ops.mode([])
        with self.assertRaises(ValueError):
            self.math_ops.mode([1, 2, 3, 4])

    def test_variance(self):
        """Test variance calculation."""
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        self.assertAlmostEqual(self.math_ops.variance(data), 4, places=5)
        with self.assertRaises(ValueError):
            self.math_ops.variance([])

    def test_standard_deviation(self):
        """Test standard deviation calculation."""
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        self.assertAlmostEqual(self.math_ops.standard_deviation(data), 2, places=5)

    def test_range_value(self):
        """Test range calculation."""
        self.assertEqual(self.math_ops.range_value([1, 2, 3, 4, 5]), 4)
        self.assertEqual(self.math_ops.range_value([10, 50, 30]), 40)
        with self.assertRaises(ValueError):
            self.math_ops.range_value([])

    # ========== Geometric Functions Tests ==========

    def test_circle_area(self):
        """Test circle area calculation."""
        self.assertAlmostEqual(self.math_ops.circle_area(5), math.pi * 25, places=10)
        self.assertEqual(self.math_ops.circle_area(0), 0)
        with self.assertRaises(ValueError):
            self.math_ops.circle_area(-5)

    def test_circle_circumference(self):
        """Test circle circumference calculation."""
        self.assertAlmostEqual(self.math_ops.circle_circumference(5), 2 * math.pi * 5, places=10)
        with self.assertRaises(ValueError):
            self.math_ops.circle_circumference(-5)

    def test_rectangle_area(self):
        """Test rectangle area calculation."""
        self.assertEqual(self.math_ops.rectangle_area(5, 10), 50)
        self.assertEqual(self.math_ops.rectangle_area(0, 10), 0)
        with self.assertRaises(ValueError):
            self.math_ops.rectangle_area(-5, 10)

    def test_rectangle_perimeter(self):
        """Test rectangle perimeter calculation."""
        self.assertEqual(self.math_ops.rectangle_perimeter(5, 10), 30)
        with self.assertRaises(ValueError):
            self.math_ops.rectangle_perimeter(-5, 10)

    def test_triangle_area(self):
        """Test triangle area calculation."""
        self.assertEqual(self.math_ops.triangle_area(10, 5), 25)
        with self.assertRaises(ValueError):
            self.math_ops.triangle_area(-10, 5)

    def test_sphere_volume(self):
        """Test sphere volume calculation."""
        self.assertAlmostEqual(self.math_ops.sphere_volume(3), (4/3) * math.pi * 27, places=10)
        with self.assertRaises(ValueError):
            self.math_ops.sphere_volume(-3)

    def test_sphere_surface_area(self):
        """Test sphere surface area calculation."""
        self.assertAlmostEqual(self.math_ops.sphere_surface_area(3), 4 * math.pi * 9, places=10)
        with self.assertRaises(ValueError):
            self.math_ops.sphere_surface_area(-3)

    def test_cylinder_volume(self):
        """Test cylinder volume calculation."""
        self.assertAlmostEqual(self.math_ops.cylinder_volume(3, 5), math.pi * 9 * 5, places=10)
        with self.assertRaises(ValueError):
            self.math_ops.cylinder_volume(-3, 5)

    def test_distance_2d(self):
        """Test 2D distance calculation."""
        self.assertEqual(self.math_ops.distance_2d(0, 0, 3, 4), 5)
        self.assertEqual(self.math_ops.distance_2d(0, 0, 0, 0), 0)

    def test_distance_3d(self):
        """Test 3D distance calculation."""
        self.assertAlmostEqual(self.math_ops.distance_3d(0, 0, 0, 1, 1, 1), math.sqrt(3), places=10)

    # ========== Number Theory Tests ==========

    def test_is_prime(self):
        """Test prime number checking."""
        self.assertTrue(self.math_ops.is_prime(2))
        self.assertTrue(self.math_ops.is_prime(17))
        self.assertFalse(self.math_ops.is_prime(1))
        self.assertFalse(self.math_ops.is_prime(4))
        self.assertFalse(self.math_ops.is_prime(0))

    def test_gcd(self):
        """Test greatest common divisor calculation."""
        self.assertEqual(self.math_ops.gcd(48, 18), 6)
        self.assertEqual(self.math_ops.gcd(100, 50), 50)

    def test_lcm(self):
        """Test least common multiple calculation."""
        self.assertEqual(self.math_ops.lcm(4, 6), 12)
        self.assertEqual(self.math_ops.lcm(21, 6), 42)

    def test_fibonacci(self):
        """Test Fibonacci number calculation."""
        self.assertEqual(self.math_ops.fibonacci(0), 0)
        self.assertEqual(self.math_ops.fibonacci(1), 1)
        self.assertEqual(self.math_ops.fibonacci(10), 55)
        with self.assertRaises(ValueError):
            self.math_ops.fibonacci(-1)

    # ========== Conversion Tests ==========

    def test_degrees_to_radians(self):
        """Test degrees to radians conversion."""
        self.assertAlmostEqual(self.math_ops.degrees_to_radians(180), math.pi, places=10)
        self.assertAlmostEqual(self.math_ops.degrees_to_radians(90), math.pi / 2, places=10)

    def test_radians_to_degrees(self):
        """Test radians to degrees conversion."""
        self.assertAlmostEqual(self.math_ops.radians_to_degrees(math.pi), 180, places=10)
        self.assertAlmostEqual(self.math_ops.radians_to_degrees(math.pi / 2), 90, places=10)

    def test_celsius_to_fahrenheit(self):
        """Test Celsius to Fahrenheit conversion."""
        self.assertEqual(self.math_ops.celsius_to_fahrenheit(0), 32)
        self.assertEqual(self.math_ops.celsius_to_fahrenheit(100), 212)

    def test_fahrenheit_to_celsius(self):
        """Test Fahrenheit to Celsius conversion."""
        self.assertEqual(self.math_ops.fahrenheit_to_celsius(32), 0)
        self.assertEqual(self.math_ops.fahrenheit_to_celsius(212), 100)


class TestConvenienceFunctions(unittest.TestCase):
    """Test cases for convenience functions."""

    def test_convenience_add(self):
        """Test convenience add function."""
        from math import add
        self.assertEqual(add(5, 3), 8)

    def test_convenience_subtract(self):
        """Test convenience subtract function."""
        from math import subtract
        self.assertEqual(subtract(10, 3), 7)

    def test_convenience_multiply(self):
        """Test convenience multiply function."""
        from math import multiply
        self.assertEqual(multiply(5, 3), 15)

    def test_convenience_divide(self):
        """Test convenience divide function."""
        from math import divide
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_convenience_power(self):
        """Test convenience power function."""
        from math import power
        self.assertEqual(power(2, 3), 8)

    def test_convenience_square_root(self):
        """Test convenience square root function."""
        from math import square_root
        self.assertEqual(square_root(16), 4)
        with self.assertRaises(ValueError):
            square_root(-1)


if __name__ == '__main__':
    unittest.main()
