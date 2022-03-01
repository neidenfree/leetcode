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
        if 'string' in kwargs:
            self.s: str = kwargs['string']
            self.g = self.get_graph_dict_from_string()

    def __str__(self):
        g = self.g
        s = ""
        for key in g:
            s += f'{key}: {g[key]}\n'
        return s

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

    def get_path(self, start: int, end: int) -> Optional[List[int]]:
        if start < 0 or end < 0:
            raise IndexError("Negative index!")
        if start >= len(self.g) or end >= len(self.g):
            raise IndexError('One of indices is greater then count of vertices!')

        g = self.g
        l = deque()
        l.append(start)
        visited = [False for x in range(len(self.g))]
        prev = [None for x in range(len(self.g))]
        visited[start] = True

        while len(l) is not None:
            current = l.popleft()
            visited[current] = True
            for elem in g[current]:
                if not visited[elem]:
                    if prev[elem] is None:
                        prev[elem] = current
                    l.append(elem)
            if len(l) == 0:
                break

        path = []
        temp = end
        while temp is not None:
            path.append(temp)
            temp = prev[temp]
        if start not in path:
            return None
        path.reverse()
        print(prev)
        return path

    def get_matrix(self):
        g = self.g

    def get_graph_dict_from_string(self) -> dict:
        s = self.s
        pairs = s.split(';')
        g = {}
        for p in pairs:
            one = p.split(',')[0]
            try:
                two = p.split(',')[1]
            except IndexError:
                two = None
            if two is None:
                if one not in g:
                    g[one] = []
            else:
                one, two = int(one), int(two)
                if one in g:
                    g[one].append(two)
                else:
                    g[one] = [two]
                if two in g:
                    g[two].append(one)
                else:
                    g[two] = [one]
        return g


if __name__ == '__main__':
    graph = Graph(string='0,1; 0,4; 0,2;  4,2; 2,3; 2,6; 2,5; 7')

    # graph = Graph(matrix=[
    # [0, 1, 1, 0, 0],
    # [1, 0, 0, 1, 0],
    # [1, 0, 0, 0, 0],
    # [0, 1, 0, 0, 1],
    # [0, 0, 0, 1, 0],
    # ])

    # graph = Graph(dict={
    #     0: [1, 2, 4],
    #     1: [0],
    #     3: [2],
    #     2: [0, 4, 3, 5, 6],
    #
    #     4: [0, 2],
    #     5: [2],
    #     6: [2]
    # })
    ind1, ind2 = 6, 4
    print(f'path from {ind1} to {ind2} =', graph.get_path(ind1, ind2))

    print(graph)

    # print(get_path(0, 3, g))
    # assert path_exists(0, 2, g)
    # assert not path_exists(0, 4, g)
    # assert not path_exists(0, 3, g)
    # assert path_exists(1, 2, g)
    # assert path_exists(2, 1, g)
    # assert path_exists(2, 0, g)

    # assert not is_graph_linked(g)
