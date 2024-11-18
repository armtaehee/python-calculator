import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add2(self):
        self.assertEqual(self.calc.add(10,-20),-10)
    def test_sub(self):
        self.assertEqual(self.calc.subtract(10,-20),30)
    def test_sub2(self):
        self.assertEqual(self.calc.subtract(-10,20),-30)
    def test_mul(self):
        self.assertEqual(self.calc.multiply(10,20),200)
    def test_mul2(self):
        self.assertEqual(self.calc.multiply(0,1),0)
    def test_divide(self):
        self.assertEqual(self.calc.divide(10,2),5)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(0,2),0)
    def test_mol(self):
        self.assertEqual(self.calc.modulo(6,2),0)
    def test_mol2(self):
        self.assertEqual(self.calc.modulo(5,2),1)
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()