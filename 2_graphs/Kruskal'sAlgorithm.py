import numpy as np


class Kruskal:
    def __init__(self, matrix):
        self.A = np.array(matrix)
        self.d = {}
        x, y = np.shape(self.A)
        if x == y:
            self.n = x
        zeroes = list(np.diagonal(self.A))
        if zeroes == [np.int32(0) for _ in range(x)]:
            self.algorithm()
        else:
            print('Неправильно введены данные')

    def algorithm(self):
        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                if f'{j}{i}' not in self.d.keys() and self.A[i - 1][j - 1] != 0:
                    self.d[f'{i}{j}'] = self.A[i - 1][j - 1]
        list_d = list(self.d.items())
        list_d.sort(key=lambda x: x[1])
        lst = []
        lst_not = []
        for i in list_d:
            for j in lst:
                if j[0][1] == i[0][1] or j[0][1] == i[0][0]:
                    for k in lst:
                        if k[0][1] != j[0][1] and (k[0][1] == i[0][1] or k[0][1] == i[0][0]):
                            if i not in lst_not:
                                lst_not.append(i)
            else:
                if i not in lst:
                    lst.append(i)
        result = list(set(lst) - set(lst_not))
        print(*[f'{x[0]} : {x[1]}' for x in result], sep='\n')


a = [[0, 3, 1, 0, 0], [3, 0, 4, 5, 0], [1, 4, 0, 6, 7], [0, 5, 6, 0, 2], [0, 0, 7, 2, 0]]
k = Kruskal(a)
