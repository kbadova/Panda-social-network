import unittest
import re
from panda import Panda
from panda_social_network import panda_social_network


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
        needle = re.compile('([\w_.\-]+[@]+[\w{2,10}]+[.]+[a-zA-Z]{2,5})')
        mail = needle.findall(self.rado.mail)
        self.assertTrue(mail)
        mail = 'asd.@ee.e'
        self.assertTrue(mail, False)


class Testpanda_social_network(unittest.TestCase):
    """docstring for ClassName"""
    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.rado = Panda("Rado", "rado@pandamail.com", "male")
        self.tony = Panda("Tony", "tony@pandamail.com", "female")
        self.network = panda_social_network()

    def test_social_network_add_panda(self):
        self.assertTrue(self.network.add_panda(self.ivo))
        with self.assertRaises(Exception):
            self.network.add_panda(self.ivo)

    def test_social_network_make_friends(self):
        self.network.make_friends(self.ivo, self.rado)
        

    def test_social_network_has_panda_are_friends(self):
        self.network.add_panda(self.ivo)
        self.assertTrue(self.ivo in self.network.graph)
        self.assertFalse(self.rado in self.network.graph)

    def test_social_network_friends_of(self):
        self.network.add_panda(self.ivo)
        self.network.add_panda(self.rado)
        self.network.make_friends(self.ivo, self.rado)
        self.assertTrue(self.ivo in self.network.graph)
        self.assertTrue(self.network.friends_of(self.ivo))
        self.assertFalse(self.network.friends_of(self.tony))

    def test_social_network_connection_level(self):
        pass

    def test_social_network_bfs(self):
        pass



if __name__ == '__main__':
    unittest.main()
