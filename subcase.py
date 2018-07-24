from sub import sub
import unittest

x = sub(3,2)


class Testsub(unittest.TestCase):
      def test_sub(self):
          self.assertEqual(x , 2)


if __name__ == "__main__":
     unittest.main()
 

