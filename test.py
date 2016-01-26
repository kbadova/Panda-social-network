# from panda import Panda
# from panda_social_network import Panda_social_network
from all_together import Panda, PandaSocialNetwork


def main():
    network = PandaSocialNetwork()
    ivo = Panda("Ivo", "ivo@pandamail.com", "male")
    # rado = Panda("Rado", "rado@pandamail.com", "male")
    # tony = Panda("Tony", "tony@pandamail.com", "female")
    print("sdv")
    print(ivo.name() == "Ivo")  # True

    # for panda in [ivo, rado, tony]:
    #     network.add_panda(panda)

    # network.make_friends(ivo, rado)
    # network.make_friends(rado, tony)

    # network.connection_level(ivo, rado) == 1  # True
    # network.connection_level(ivo, tony) == 2  # True

    # network.how_many_gender_in_network(1, rado, "female") == 1  # True
    # print(network)
    # network.save("file.json")
    # new_network = network.load("file.json")
    # print(new_network)
    # print(new_network.connection_level(ivo, rado) == 1)  # True
    # # # new_network = network.load("file.json")
    # # # print(new_network)
    # print(new_network.has_panda(new_network.ivo))

if __name__ == '__main__':
    main()

