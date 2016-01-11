
from collections import deque
import json

M = 8


class Node(object):
    """docstring for  Node"""
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class LinkedList(object):
    """docstring for LinkedList"""
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def __str__(self):
        return str(self.root.get_data())

    def __repr__(self):
        return str(self.root.get_data())

    def set_size(self):
        return self.size

    def get_size(self):
        return self.size

    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root == this_node
                self.size -= 1
                return True    # data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False


class HashTable():
    """docstring for HashTable"""
    def __init__(self):
        super(HashTable, self).__init__()
        self.m = M
        self.users = {}
        self.size = 0

    def hash_validator(self):
        if len(self.users) > self.m:
            self.grow_table()
        if self.m == len(self.users) / 4:
            return self.shrink_table()

    def construct_hash_table(self):
        if len(self.users) == 0:
            self.users = {x: None for x in range(self.m)}
        else:
            hash_table = {x: None for x in range(self.m)}
            for elem in self.users:
                hash_table[elem] = self.users[elem]
            self.users = hash_table

    def insert(self, user):
        b = LinkedList()
        b.add(user)
        self.users[hash(user) % len(self.users)] = b

    def remove(self, user):
        pass

    def grow_table(self):
        self.m *= 2
        hash_table = self.construct_hash_table()
        for elem in self.users:
            hash_table[elem] = self.users[elem]
        self.users = hash_table
        return True

    def shrink_table(self):
        self.m /= 2
        self.construct_hash_table()


class Panda_social_network(HashTable):

    def __init__(self):
        super(Panda_social_network, self).__init__()
        self.graph = {}
        self.level = {}
        self.m = 8  # constant size of hash table

    def __iter__(self):
        return self.graph

    def add_panda(self, panda):
        if panda in self.graph:
            raise Exception("PandaAlreadyThere")
        self.graph[hash(panda)] = []
        self.level[hash(panda)] = panda
        return True

    def has_panda(self, panda):
        return hash(panda) in self.graph

    def are_friends(self, panda1, panda2):
        if panda1 in self.graph[hash(panda2)] and panda2 in self.graph[hash(panda1)]:
            return True
        return False

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        if self.are_friends(panda1, panda2):
            raise Exception("PandasAlreadyFriends")
        self.graph[hash(panda1)].append(hash(panda2))
        self.graph[hash(panda2)].append(hash(panda1))

    def friends_of(self, panda):
        if not self.has_panda(panda):
            return False
        return self.graph[hash(panda)]

    def connection_level(self, start_node, end_node):
        visited = set()
        queue = deque()

        visited.add(hash(start_node))
        queue.append((0, hash(start_node)))

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
            elem = self.level[elem]
            if self.connection_level(panda, elem) == level:
                if elem.gender == gender:
                    counter += 1
        return counter

    def for_json(self):
        return {str(k): str(self.graph[k]) for k in self.graph}

    def save(self, file_name):
        print(self.for_json())
        with open(file_name, "w") as filee:
            json.dump(self.for_json(), filee)
            filee.close()

    def load(self, file_name):
        with open(file_name, "r") as filee:
            self.graph = json.load(filee)
            print(self.graph)

    """
     for item in old.table:
        new.table.insert
    """
    """if n > m construct_table"""

