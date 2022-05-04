import unittest
from unittest import result 
import calc

class test_calc(unittest.TestCase):
    # def test_add(self):
    #     result =calc.add(10,5)
    #     self.assertEqual(result,15)
    def test_add(self):
        self.assertEqual(calc.add(1,-1),0)
        self.assertEqual(calc.add(-1,-1),-2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(-5,5),-10)
        self.assertEqual(calc.subtract(-5,-5),0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)
        # self.assertEqual(calc.multiply(-5,-5),-25)
        self.assertEqual(calc.multiply(-5,5),-25)
        self.assertEqual(calc.multiply(-5,-5),25)
    
    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-5,5),-1)
        self.assertEqual(calc.divide(-5,-5),1)

if __name__ == "__main__":
    unittest.main()
