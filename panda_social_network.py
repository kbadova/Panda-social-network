from collection import deque


class panda_social_network:

    def __init__(self):
        self.graph = {}

    def add_panda(self, panda):
        if panda in self.graph:
            raise Exception("PandaAlreadyThere")
        self.graph[panda] = []

    def has_panda(self, panda):
        return panda in self.graph

    def are_frinds(self, panda1, panda2):
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
        self.graph[hash(panda1)].append(panda2)
        self.graph[hash(panda2)].append(panda1)

    def friends_of(self, panda):
        if not self.has_panda(panda):
            return False
        return self.graph[panda]

    def connection_level(self, panda1, panda2):
        pass

    """
    Breadth-First-Search
    S -all you can reach in 0 moves
    """
    def bfs(self, s, graph):
        level = {s: 0}  # level 0
        parent = {s: None}
        i = 1
        visited = [s]  # level i -1

        while visited:
            next_graph = deque()
            for node in visited:
                for v in graph[node]:
                    if v not in level:
                        level[v] = i
                        parent[v] = node
                        next_graph.append(v)
            visited = next_graph
            i += 1
