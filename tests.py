import unittest, random
from Vector3 import Vector3
from Point import Point

class BaseSetup:
    def setUp(self):
        self.rand_pairs = (random.uniform(-10e10, 10e10), random.uniform(-10e10, 10e10), random.uniform(-10e10, 10e10))
        self.const_pairs = (1,2,3)
        self.rand_val = random.uniform(-10e10, 10e10)
        self.const_val = 69.0

    def tearDown(self):
        pass

class TestPointConstructor(BaseSetup, unittest.TestCase):

    def test_point_constructor_by_param(self):
        x, y, z = self.rand_pairs

        point = Point(x)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, 0)
        self.assertEqual(point.z, 0)

        point = Point(x, y)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)
        self.assertEqual(point.z, 0)

        point = Point(x, y, z)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)
        self.assertEqual(point.z, z)

    def test_point_constructor_by_list(self):
        x, y, z = self.rand_pairs

        point = Point(x)
        point2 = Point([x])
        self.assertEqual(point, point2)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, 0)
        self.assertEqual(point.z, 0)

        point = Point(x, y)
        point2 = Point([x, y])
        self.assertEqual(point, point2)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)
        self.assertEqual(point.z, 0)

        point = Point(x, y, z)
        point2 = Point([x, y, z])
        self.assertEqual(point, point2)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)
        self.assertEqual(point.z, z)

    def test_point_constructor_by_tuple(self):
        x, y, z = self.rand_pairs

        point = Point(x)
        point2 = Point((x))
        self.assertEqual(point, point2)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, 0)
        self.assertEqual(point.z, 0)

        point = Point(x, y)
        point2 = Point((x, y))
        self.assertEqual(point, point2)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)
        self.assertEqual(point.z, 0)

        point = Point(x, y, z)
        point2 = Point((x, y, z))
        self.assertEqual(point, point2)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)
        self.assertEqual(point.z, z)

    def test_point_constructor_by_dict(self):
        x, y, z = self.rand_pairs

        point = Point(x)
        point2 = Point({'x': x})
        self.assertEqual(point, point2)

        point = Point(x, y)
        point2 = Point({'x': x, 'y': y})
        self.assertEqual(point, point2)

        point = Point(x, y, z)
        point2 = Point({'x': x, 'y': y, 'z': z})
        self.assertEqual(point, point2)


    def test_point_constructor_by_self(self):
        x, y, z = self.rand_pairs
        point = Point(x, y, z)
        point2 = Point(point)
        self.assertEqual(point, point2)


    def test_point_constructor_string_as_args(self):
        x1, y1, z1 = self.rand_pairs
        x2, y2, z2 = map(lambda a: str(a), self.rand_pairs)
        point = Point(x1, y1, z1)
        point2 = Point(x2, y2, z2)
        self.assertEqual(point, point2)

class TestPointMethods(BaseSetup, unittest.TestCase):

    def test_point_setter(self):
        x, y, z = self.rand_pairs
        point = Point(0, 0, 0)
        point2 = Point(x, y, z)
        point.set(x, y, z)
        self.assertEqual(point, point2)

    def test_point_method_to_list(self):
        x, y, z = self.rand_pairs
        point = Point(x, y, z)
        self.assertListEqual(point.to_list(), [x, y, z])

    def test_point_method_to_list_property_shorthand(self):
        x, y, z = self.rand_pairs
        point = Point(x, y, z)
        self.assertListEqual(point.ls, [x, y, z])

    def test_point_method_to_dict(self):
        x, y, z = self.rand_pairs
        point = Point(x, y, z)
        self.assertDictEqual(point.to_dict(), {'x': x, 'y': y, 'z': z})

class TestPointArithmetics(BaseSetup, unittest.TestCase):

    def test_point_property_length(self):
        x, y, z = self.const_pairs
        point = Point(x, y, z)
        self.assertAlmostEqual(point.len, 3.7416573867739413)

    def test_point_arithmetic_neg(self):
        x, y, z = self.rand_pairs
        point = Point(x, y, z)
        point2 = Point(-x, -y, -z)
        point = -point
        self.assertEqual(point, point2)

    def test_point_arithmetic_inv(self):
        x, y, z = self.rand_pairs
        point = Point(x, y, z)
        point2 = Point(-x, -y, -z)
        point = ~point
        self.assertEqual(point, point2)

    def test_point_arithmetic_pos(self):
        x, y, z = self.rand_pairs
        point = Point(x, y, z)
        point2 = Point(x, y, z)
        point = +point
        self.assertEqual(point, point2)

    def test_point_arithmetic_add_self(self):
        x, y, z = self.rand_pairs
        point = Point(x, y, z)
        point2 = Point(x, y, z)
        point = point + point2
        self.assertEqual(point.x, x+x)
        self.assertEqual(point.y, y+y)
        self.assertEqual(point.z, z+z)

        point = Point(x, y, z)
        point2 = Point(x, y, z)
        point += point2
        self.assertEqual(point.x, x+x)
        self.assertEqual(point.y, y+y)
        self.assertEqual(point.z, z+z)

    def test_point_arithmetic_add_int_float(self):
        x, y, z = self.rand_pairs
        point = Point(x, y, z)
        point = point + self.rand_val
        self.assertEqual(point.x, x+self.rand_val)
        self.assertEqual(point.y, y+self.rand_val)
        self.assertEqual(point.z, z+self.rand_val)

        point = Point(x, y, z)
        point += self.rand_val
        self.assertEqual(point.x, x+self.rand_val)
        self.assertEqual(point.y, y+self.rand_val)
        self.assertEqual(point.z, z+self.rand_val)

        self.rand_val = int(self.rand_val)

        x, y, z = self.rand_pairs
        point = Point(x, y, z)
        point = point + self.rand_val
        self.assertEqual(point.x, x+self.rand_val)
        self.assertEqual(point.y, y+self.rand_val)
        self.assertEqual(point.z, z+self.rand_val)

        point = Point(x, y, z)
        point += self.rand_val
        self.assertEqual(point.x, x+self.rand_val)
        self.assertEqual(point.y, y+self.rand_val)
        self.assertEqual(point.z, z+self.rand_val)


    def test_point_arithmetic_sub_self(self):
        x, y, z = self.rand_pairs
        point = Point(x, y, z)
        point2 = Point(x, y, z)
        point = point - point2
        self.assertEqual(point.x, x-x)
        self.assertEqual(point.y, y-y)
        self.assertEqual(point.z, z-z)

        point = Point(x, y, z)
        point2 = Point(x, y, z)
        point -= point2
        self.assertEqual(point.x, x-x)
        self.assertEqual(point.y, y-y)
        self.assertEqual(point.z, z-z)

    def test_point_arithmetic_sub_int_float(self):
        x, y, z = self.rand_pairs
        point = Point(x, y, z)
        point = point - self.rand_val
        self.assertEqual(point.x, x-self.rand_val)
        self.assertEqual(point.y, y-self.rand_val)
        self.assertEqual(point.z, z-self.rand_val)

        point = Point(x, y, z)
        point -= self.rand_val
        self.assertEqual(point.x, x-self.rand_val)
        self.assertEqual(point.y, y-self.rand_val)
        self.assertEqual(point.z, z-self.rand_val)

        self.rand_val = int(self.rand_val)

        x, y, z = self.rand_pairs
        point = Point(x, y, z)
        point = point - self.rand_val
        self.assertEqual(point.x, x-self.rand_val)
        self.assertEqual(point.y, y-self.rand_val)
        self.assertEqual(point.z, z-self.rand_val)

        point = Point(x, y, z)
        point -= self.rand_val
        self.assertEqual(point.x, x-self.rand_val)
        self.assertEqual(point.y, y-self.rand_val)
        self.assertEqual(point.z, z-self.rand_val)

    def test_point_arithmetic_mul_and_dot_product(self):
        x, y, z = self.const_pairs
        point = Point(x, y, z)
        point2 = Point(x, y, z)
        val = point * point2
        self.assertAlmostEqual(val, 14.0)

        point = Point(x, y, z)
        point = point * self.rand_val
        self.assertAlmostEqual(point.x, x*self.rand_val)
        self.assertAlmostEqual(point.y, y*self.rand_val)
        self.assertAlmostEqual(point.z, z*self.rand_val)

    def test_point_arithmetic_div(self):
        x, y, z = self.rand_pairs

        point = Point(x, y, z)
        point = point / self.rand_val
        self.assertAlmostEqual(point.x, x/self.rand_val)
        self.assertAlmostEqual(point.y, y/self.rand_val)
        self.assertAlmostEqual(point.z, z/self.rand_val)

class TestPointErrors(BaseSetup, unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()