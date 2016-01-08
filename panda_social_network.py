from collections import deque
import sqlite3
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'panda_network.db')
DB = sqlite3.connect(DB_PATH)
c = DB.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS users
#     (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
#     name            CHAR(70)     NOT NULL,
#     mail CHAR(20) NOT NULL),
#     gender char(20) NOT NULL;''')

# c.execute(
#     '''
#         CREATE TABLE IF NOT EXISTS 

#     ''')

class panda_social_network:

    def __init__(self):
        self.graph = {}
        self.level = {}

    def add_panda(self, panda):
        if panda in self.graph:
            raise Exception("PandaAlreadyThere")
        self.graph[panda] = []

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
        print(self.level)
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
        self.bfs(panda)
        key = []
        key.append(list(self.level.keys())[list(self.level.values()).index(level)])
        i = sum([1 for panda in key if panda.gender == gender])
        return i

    def save(file_name):
        pass

    def load(file_name):
        pass
