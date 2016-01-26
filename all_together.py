import re
from collections import deque
import json


class Panda:
    def __init__(self, name, mail, gender):
        self.name = name
        self.mail = mail
        self.gender = gender
        self.__verify_mail()

    def name(self):
        return self.name

    def email(self):
        return self.mail

    def gender(self):
        return self.gender

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.mail, self.gender)

    def __repr__(self):
        return "{} {} {}".format(self.name, self.mail, self.gender)

    def __eq__(self, other):
        if self.__hash__() == other:
            return True

    def __hash__(self):
        return hash(self.__str__())

    def __verify_mail(self):
        find = re.compile('([\w_.\-]+[@]+[\w{2,10}]+[.]+[a-zA-Z]{2,5})')
        if len(find.findall(self.mail)) == 0:
            raise Exception("You have provided invalid mail adress...")

    def isMale(self):
        return self.gender == 'male'

    def isFemale(self):
        return self.gender == 'female'

    def panda_dict(self):
        return str(self.__dict__)


class PandaSocialNetwork:

    def __init__(self):
        self.graph = {}

    def __str__(self):
        # string = ""
        # for key in self.graph:
        #     new_key = "'" + str(key) + "'"
        #     self.graph[new_key] = self.graph[key]
        #     self.graph[key] = []
            # for el in self.graph[key]:
            #     if el not in string_key_names:
            #         string_key_names += el + ", "
            # string += "'{}' : [{}]".format(key, string_key_names)
        # return "{" + string.replace(", ]", "],") + "}"
        return str(self.graph)

    def __repr__(self):
        return str(self.graph)

    def add_panda(self, panda):
        if panda in self.graph:
            raise Exception("PandaAlreadyThere")
        self.graph[panda] = []

    def has_panda(self, panda):
        return panda in self.graph

    def are_friends(self, panda1, panda2):
        if panda1 in self.graph[panda2] and panda2 in self.graph[panda1]:
            return True
        return False

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        if self.are_friends(panda1, panda2):
            raise Exception("PandasAlreadyFriends")
        self.graph[panda1].append(panda2)
        self.graph[panda2].append(panda1)

    def friends_of(self, panda):
        if not self.has_panda(panda):
            return False
        return self.graph[panda]

    def connection_level(self, start_node, end_node):
        visited = set()
        queue = deque()

        visited.add(start_node)
        queue.append((0, start_node))

        while len(queue) != 0:
            node_with_level = queue.popleft()
            node = node_with_level[1]
            level = node_with_level[0]

            if node == end_node:
                return level

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((level + 1, neighbour))
        return -1

    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1, panda2) == -1:
            return False
        elif self.connection_level(panda1, panda2) == 0:
            return "Panda not a friend with itself"
        return True

    def how_many_gender_in_network(self, level, panda, gender):
        counter = 0
        for elem in self.graph:
            if self.connection_level(panda, elem) == level:
                if elem.gender == gender:
                    counter += 1
        return counter

    def get_dict(self):
        result = {}
        panda_dict = {}
        for panda in self.graph:
            dict_of_friends = []
            for friend in self.friends_of(panda):
                dict_of_friends.append(friend.__dict__)
            result = {
                        "name": panda.name,
                        "mail": panda.mail,
                        "gender": panda.gender,
                        "friends": dict_of_friends
                        }
            panda_dict[panda.name] = result
        return panda_dict

    def dict_of_friends(self, panda):
        dict_of_friends = []
        for friend in self.friends_of(panda):
            dict_of_friends.append(friend.panda_dict())
        return dict_of_friends

    def load(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return data

    def save(self, filename):
        data = self.load(filename)
        dict_graph = {}
        for panda in self.graph:
            dict_graph[panda.panda_dict()] = self.dict_of_friends(panda)
        data.update(dict_graph)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)

    # def load_from_dict(self, data_d):
    #     playlist = PLayList("Name")
    #     songss = data_d.pop('songs')
    #     playlist.__dict__ = data_d
    #     playlist._songs = []
    #     for song in songss:
    #         newsong = Song(song["_Song__title"], song["_Song__artist"], song["_Song__album"], song["_Song__length"])
    #         newsong.__dict__ = song
    #         playlist.add_song(newsong)
    #     return playlist

    # @staticmethod
    # def load(self, filename):
    #     with open(filename, 'r') as f:
    #         data_d = json.load(f)
    #     return self.load_from_dict(data_d)


    # def save(self, file_name):
    #     with open(file_name, "w") as filee:
    #         json.dump(self.get_dict(), filee, indent=4)

    # def load(self, file_name):
    #     with open(file_name, 'r') as f:
    #         data_d = json.load(f)
    #     return self.load_from_dict(data_d)




    # def get_dict(self):
    #     dict_of_songs = []
    #     for song in self._songs:
    #         dict_of_songs.append(song.__dict__)
    #     result = {
    #             "name": self._name,
    #             "repeat": self._repeat,
    #             "shuffle": self._shuffle,
    #             "song_index": self._song_index,
    #             "songs": dict_of_songs,
    #     }
    #     return result

    # def load_from_dict(self, data):
    #     new_network = Panda_social_network()
    #     new_data = data
    #     list_friends = []
    #     i = 0
    #     for panda in data:
    #         list_friends.append(data[panda].pop("friends"))
    #         # new_network.__dict__ = list_friends
    #     print(list_friends)
    #     for panda in list_friends:
    #         # print(panda)
    #         new_panda = Panda(panda[0]["name"], panda[0]["mail"], panda[0]["gender"])
    #         print(new_panda)
    #         new_panda.__dict__ = panda[0]
    #         print(new_network)
    #         if not new_network.has_panda(new_panda):
    #             new_network.add_panda(new_panda)
    #         # print(new_network)
    #     for panda in new_network.graph:
    #         print(new_data[panda.name])
    #         # if new_panda != list_friends[i]:
    #         # new_network.make_friends(panda, data[panda.name]['friends'])
    #         # i += 1
    #         # print(new_network)
    #     return new_network
