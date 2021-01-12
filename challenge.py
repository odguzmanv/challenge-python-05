import math

def square_area(side):
    """Returns the area of a square"""
    side = float(side)

    if (side < 0.0):
        raise ValueError('Negative numbers are not allowed')

    return side**2.0


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    base = float(base)
    height = float(height)
    if (base < 0.0 or height < 0.0):
        raise ValueError('Negative numbers are not allowed')

    return base * height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    base = float(base)
    height = float(height)
    if (base < 0.0 or height < 0.0):
        raise ValueError('Negative numbers are not allowed')

    return base * height / 2.0


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    diagonal_1 = float(diagonal_1)
    diagonal_2 = float(diagonal_2)
    if (diagonal_1 < 0.0 or diagonal_2 < 0.0):
        raise ValueError('Negative numbers are not allowed')

    return diagonal_1 * diagonal_2 / 2.0


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    base_minor = float(base_minor)
    base_major = float(base_major)
    height = float(height)
    if (base_minor < 0.0 or base_major < 0.0 or height < 0.0):
        raise ValueError('Negative numbers are not allowed')

    return (base_minor + base_major) * height / 2.0


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    perimeter = float(perimeter)
    apothem = float(apothem)
    if (perimeter < 0.0 or apothem < 0.0):
        raise ValueError('Negative numbers are not allowed')

    return perimeter * apothem / 2


def circumference_area(radius):
    """Returns the area of a circumference"""
    radius = float(radius)

    if (radius < 0.0):
        raise ValueError('Negative numbers are not allowed')

    return radius**2 * math.pi


if __name__ == '__main__':
    import unittest

    class TestValues:
        def __init__(self, expected,  args=[], kwargs={}):
            self.expected = expected
            self.args = args
            self.kwargs = kwargs

    class TestRaisesError:
        def __init__(self, raises_error, args=[], kwargs={}):
            self.args = args
            self.kwargs = kwargs
            self.raises_error = raises_error

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            # Initialize the needed values for the tests
            self.square_test_values = [
                TestValues(1, [1]),
                TestValues(4, [2]),
                TestValues(9, [3]),
                TestValues(6.25, [2.5]),
            ]

            self.rectangle_test_values = [
                TestValues(1, [1, 1]),
                TestValues(6, [2, 3]),
                TestValues(20, [5, 4]),
                TestValues(14.25, [2.5, 5.7]),
            ]

            self.triangle_test_values = [
                TestValues(2, [2, 2]),
                TestValues(7.5, [5, 3]),
                TestValues(0.1, [0.5, 0.4]),
            ]

            self.rhombus_test_values = [
                TestValues(3, [3, 2]),
                TestValues(7.5, [5, 3]),
                TestValues(0.1, [0.5, 0.4]),
            ]

            self.trapezoid_test_values = [
                TestValues(10, [2, 2, 5]),
                TestValues(16.5, [2.4, 2.6, 6.6]),
            ]

            self.regular_polygon_test_values = [
                TestValues(7.5, [5, 3]),
                TestValues(0.1, [0.5, 0.4]),
            ]

            self.circumference_test_values = [
                TestValues(math.pi, [1]),
                TestValues(math.pi * 30.25, [5.5]),
            ]

            self.one_param_test_raises = [
                TestRaisesError(ValueError, [-1]),
                TestRaisesError(ValueError, ['a']),
            ]

            self.two_params_test_raises = [
                TestRaisesError(ValueError, [-1, 1]),
                TestRaisesError(ValueError, [1, -1]),
                TestRaisesError(ValueError, [-1, -1]),
                TestRaisesError(ValueError, ['a', 1]),
                TestRaisesError(ValueError, [1, 'a']),
            ]

            self.three_params_test_raises = [
                TestRaisesError(ValueError, [-1, 1, 1]),
                TestRaisesError(ValueError, [1, -1, 1]),
                TestRaisesError(ValueError, [1, 1, -1]),
                TestRaisesError(ValueError, [-1, -1, -1]),
                TestRaisesError(ValueError, ['a', 1, 1]),
                TestRaisesError(ValueError, [1, 'a', 1]),
                TestRaisesError(ValueError, [1, 1, 'a']),
            ]

        @unittest.expectedFailure
        def test_values_rise(self, fn, values=[], raises=[]):
            for test_values in values:
                self.assertEqual(test_values.expected, fn(
                    *test_values.args, **test_values.kwargs))

            for test_raises in raises:
                with self.assertRaises(test_raises.raises_error):
                    fn(*test_raises.args, **test_raises.kwargs)

        def test_square_area(self):
            self.test_values_rise(
                square_area,
                self.square_test_values,
                self.one_param_test_raises
            )

        def test_rectangle_area(self):
            self.test_values_rise(
                rectangle_area,
                self.rectangle_test_values,
                self.two_params_test_raises
            )

        def test_triangle_area(self):
            self.test_values_rise(
                triangle_area,
                self.triangle_test_values,
                self.two_params_test_raises
            )

        def test_rhombus_area(self):
            self.test_values_rise(
                rhombus_area,
                self.rhombus_test_values,
                self.two_params_test_raises
            )

        def test_trapezoid_area(self):
            self.test_values_rise(
                trapezoid_area,
                self.trapezoid_test_values,
                self.three_params_test_raises
            )

        def test_regular_polygon_area(self):
            self.test_values_rise(
                regular_polygon_area,
                self.regular_polygon_test_values,
                self.two_params_test_raises
            )

        def test_circumference_area(self):
            self.test_values_rise(
                circumference_area,
                self.circumference_test_values,
                self.one_param_test_raises
            )

        def tearDown(self):
            del(self.square_test_values)
            del(self.rectangle_test_values)
            del(self.triangle_test_values)
            del(self.rhombus_test_values)
            del(self.trapezoid_test_values)
            del(self.regular_polygon_test_values)
            del(self.circumference_test_values)

            del(self.one_param_test_raises)
            del(self.two_params_test_raises)
            del(self.three_params_test_raises)

    unittest.main()