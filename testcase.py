import test
import unittest

obj = test.Calculator(2,3)

class Testaddition(unittest.TestCase):
      def test_add(self):
          self.assertEqual(test.Calculator.add(2, 3) , 5)

      def test_addWithoutStatic(self):
          self.assertEqual(obj.addWithoutStatic(), 5)

if __name__ == "__main__":
     unittest.main()
