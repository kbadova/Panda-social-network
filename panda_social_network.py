from collections import deque
import os
import json


class panda_social_network:

    def __init__(self):
        self.graph = {}
        self.level = {}

    def __iter__(self):
        return self.graph

    def add_panda(self, panda):
        if panda in self.graph:
            raise Exception("PandaAlreadyThere")
        self.graph[panda] = []
        return True

    def has_panda(self, panda):
        return panda in self.graph

    def are_friends(self, panda1, panda2):
        if panda1 in self.graph[panda2] or panda2 in self.graph[panda1]:
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

    def connection_level(self, panda1, panda2):
        return self.bfs(panda1, panda2)

    """
    Breadth-First-Search
    S -all you can reach in 0 moves
    """
    def bfs(self, panda1, panda2='optional'):
        self.level = {panda1: 0}  # level 0
        parent = {panda1: None}
        i = 1  # start from level 1
        visited = [panda1]  # level i -1

        while visited:
            next_graph = deque()  # level i
            for node in visited:
                for neighbour in self.graph[node]:
                    if neighbour not in self.level:
                        self.level[neighbour] = i
                        parent[neighbour] = node
                        next_graph.append(neighbour)
            visited = next_graph
            i += 1
        try:
            return self.level[panda2]
        except KeyError:
            return False

    def are_connected(self, panda1, panda2):
        if self.bfs(panda1, panda2):
            return True
        return False

    def how_many_gender_in_network(self, level, panda, gender):
        i = 0
        for elem in self.graph:
            if self.bfs(elem, panda) == level and elem.gender == gender:
                i += 1
        return i

    def save(self, file_name):
        with open(file_name, 'w') as fp:
            json.dump(str(self.graph), fp, sort_keys=True, indent=4)

    def load(self, file_name):
        with open(file_name, 'r') as fp:
            self.graph = json.load(fp)
