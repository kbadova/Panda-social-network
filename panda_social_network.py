from collections import deque
import json
from panda import Panda


class PandaSocialNetwork:

    def __init__(self):
        self.graph = {}

    def __str__(self):
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
                if elem.gender() == gender:
                    counter += 1
        return counter

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
