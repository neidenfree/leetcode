from typing import List, Optional
from collections import deque


class Graph:
    def __init__(self, **kwargs):
        if 'matrix' in kwargs:
            self.m = kwargs['matrix']
            self.g = self.get_graph_dict()
        if 'dict' in kwargs:
            self.g = kwargs['dict']
            self.m = self.get_matrix()

    def get_graph_dict(self) -> Optional[dict]:
        if len(self.m) == 0:
            return None
        d = {}
        for i, vertex in enumerate(self.m):
            d[i] = [x for x in range(len(vertex)) if vertex[x] == 1]
        return d

    def path_exists(self, ind1: int, ind2: int) -> bool:
        g = self.g
        l = deque()
        l.append(ind1)
        visited = []
        while len(l) is not None:
            current_vertex = l.popleft()
            visited.append(current_vertex)
            if type(g[current_vertex]) is list:
                for el in g[current_vertex]:
                    if el not in visited:
                        if el == ind2:
                            return True
                        l.append(el)
            else:
                if g[current_vertex] not in visited:
                    if l == ind2:
                        return True
                    l.append(g[current_vertex])
                    # visited.append(g[current_vertex])
            if len(l) == 0:
                return False
        return False

    def is_graph_linked(self) -> bool:
        g = self.g
        if g is None:
            return False
        l = deque()
        l.append(0)
        visited = []
        while len(l) is not None:
            current_vertex = l.popleft()
            visited.append(current_vertex)
            if type(g[current_vertex]) is list:
                for el in g[current_vertex]:
                    if el not in visited:
                        l.append(el)
            else:
                if g[current_vertex] not in visited:
                    l.append(g[current_vertex])
            if len(l) == 0:
                break
        return len(visited) == len(self.g)

    def get_path(self, ind1: int, ind2: int) -> Optional[List[int]]:
        g = self.g
        l = deque()
        l.append(ind1)
        visited = [False for x in range(len(self.g))]
        prev = [None for x in range(len(self.g))]
        visited[ind1] = True

        while len(l) is not None:
            current = l.popleft()
            visited[current] = True
            for elem in g[current]:
                if not visited[elem]:
                    prev[elem] = current
                    l.append(elem)
            if len(l) == 0:
                break


        path = []
        temp = ind2
        while temp is not None:
            path.append(temp)
            temp = prev[temp]
        path.reverse()
        return path

    def get_matrix(self):
        g = self.g


if __name__ == '__main__':
    # graph = Graph(matrix=[
    # [0, 1, 1, 0, 0],
    # [1, 0, 0, 1, 0],
    # [1, 0, 0, 0, 0],
    # [0, 1, 0, 0, 1],
    # [0, 0, 0, 1, 0],
    # ])
    graph = Graph(dict={
        0: [1, 2, 4],
        1: [0],
        2: [3, 5, 6],
        3: [2],
        4: [0, 2],
        5: [2],
        6: [2]
    })

    print(graph.get_path(1, 6))

    # print(get_path(0, 3, g))
    # assert path_exists(0, 2, g)
    # assert not path_exists(0, 4, g)
    # assert not path_exists(0, 3, g)
    # assert path_exists(1, 2, g)
    # assert path_exists(2, 1, g)
    # assert path_exists(2, 0, g)

    # assert not is_graph_linked(g)
