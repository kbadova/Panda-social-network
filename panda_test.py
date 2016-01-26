import unittest
from panda import Panda


class TestPanda(unittest.TestCase):

    """docstring for Panda"""

    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.rado = Panda("Rado", "rado@pandamail.com", "male")
        self.tony = Panda("Tony", "tony@pandamail.com", "female")

    def test_Panda__eq__(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(self.ivo, ivo)
        gosho = Panda("Ivo", "ivo@pandadasmail.com", "male")
        self.assertNotEqual(self.ivo, gosho)

    def test_Panda__hash__(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(self.ivo, ivo)
        gosho = Panda("Ivo", "ivo@pandadasmail.com", "male")
        self.assertNotEqual(self.ivo, gosho)

    def test_Panda___verify_mail(self):
        ivo = Panda("Ivo", "ivo@.com", "male")
        self.assertRaises(Exception, ivo)

if __name__ == '__main__':
    unittest.main()

