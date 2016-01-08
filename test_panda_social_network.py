import unittest
from panda import Panda
from panda_social_network import Panda_social_network


class TestPanda_social_network(unittest.TestCase):

    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.rado = Panda("Rado", "rado@pandamail.com", "male")
        self.pavli = Panda("Pavli", "pavli@pandamail.com", "male")
        self.maria = Panda("Maria", "maria@pandamail.com", "female")
        self.krasi = Panda("Krasi", "krasi@pandamail.com", "female")
        self.network = Panda_social_network()

    def test_has_and_add_panda_in_network(self):
        self.network.add_panda(self.ivo)
        self.assertTrue(self.network.has_panda(self.ivo))

    def test_has_panda_when_not_in_network(self):
        self.assertFalse(self.network.has_panda(self.rado))

    def test_make_and_are_friends(self):
        self.network.add_panda(self.ivo)
        self.network.add_panda(self.rado)
        self.assertFalse(self.network.are_friends(self.ivo, self.rado))
        self.network.make_friends(self.ivo, self.rado)
        self.assertTrue(self.network.are_friends(self.ivo, self.rado))

    def test_connection_level(self):
        self.network.add_panda(self.ivo)
        self.network.add_panda(self.rado)
        self.network.add_panda(self.pavli)
        self.network.add_panda(self.maria)
        self.network.make_friends(self.ivo, self.rado)
        self.network.make_friends(self.rado, self.pavli)
        self.network.make_friends(self.pavli, self.maria)
        self.assertEqual(self.network.connection_level(self.ivo, self.rado), 1)
        self.assertEqual(self.network.connection_level(self.ivo, self.pavli), 2)

    def test_are_connected(self):
        self.network.add_panda(self.ivo)
        self.network.add_panda(self.rado)
        self.network.add_panda(self.pavli)
        self.network.add_panda(self.maria)
        self.network.make_friends(self.ivo, self.rado)
        self.network.make_friends(self.rado, self.pavli)
        # self.network.make_friends(self.pavli, self.maria)
        self.assertEqual(self.network.are_connected(self.ivo, self.ivo), "Panda not a friend with itself")

    def test_how_many_gender_in_network(self):
        self.network.add_panda(self.ivo)
        self.network.add_panda(self.rado)
        self.network.add_panda(self.pavli)
        self.network.add_panda(self.maria)
        self.network.add_panda(self.krasi)
        self.network.make_friends(self.ivo, self.rado)
        self.network.make_friends(self.rado, self.pavli)
        self.network.make_friends(self.rado, self.maria)
        self.network.make_friends(self.maria, self.krasi)
        self.assertEqual(self.network.how_many_gender_in_network(2, self.rado, "female"), 1)

if __name__ == '__main__':
    unittest.main()
