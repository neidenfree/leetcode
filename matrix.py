from __future__ import annotations

from random import randint


class Matrix:
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self._mat = [[]]
            self._shape = (0, 0)

        if "shape" in kwargs:
            if type(kwargs['shape']) == tuple and len(kwargs['shape']) == 2:
                self._shape = kwargs['shape']
                self._mat = []
                for _ in range(kwargs['shape'][0]):
                    a = []
                    for _ in range(kwargs['shape'][1]):
                        a.append(randint(0, 10))
                    self._mat.append(a)
            else:
                raise TypeError("For shape you must provide a tuple with exactly two positive variables!")

        if "mat" in kwargs:
            try:
                if kwargs["mat"][0][0] is not None:
                    mat = kwargs["mat"]
                    self._mat = mat
                    self._shape = (len(mat), len(mat[0]))
            except TypeError:
                raise TypeError("You must provide a two-dimensional array!")

    def __str__(self):
        res = ""
        for i in range(self._shape[0]):
            for j in range(self._shape[1]):
                res += "%3d " % self._mat[i][j]
            res += "\n"
        return res

    def rotate(self) -> Matrix:
        if self._shape[0] != self._shape[1]:
            raise IndexError("You can't rotate non-square matrices!")
        if self._shape == (1, 1):
            return self
        mat = self._mat
        res = []
        for i in range(self._shape[0]):
            temp = []
            for j in range(self._shape[1]):
                temp.append(mat[self._shape[0] - 1 - j][i])
            res.append(temp)

        return Matrix(mat=res)

    def zero_matrix(self) -> Matrix:
        """
        Write an algorithm such that if an element in an MxN matrix if 0,
        its entire row and column are set to 0.
        :return: Matrix
        """
        set_columns = set()
        set_rows = set()

        mat = self._mat
        for i in range(self._shape[0]):
            for j in range(self._shape[1]):
                if mat[i][j] == 0:
                    set_columns.add(i)
                    set_rows.add(j)
        for col in set_columns:
            for j in range(self._shape[1]):
                mat[col][j] = 0
        for row in set_rows:
            for i in range(self._shape[0]):
                mat[i][row] = 0
        return Matrix(mat=mat)
