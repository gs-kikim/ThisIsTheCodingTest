import unittest

from src.SP import Q37, Q38, Q38_1, Q39, Q40


class TestShortestPathProblem(unittest.TestCase):
    def test_Q37(self):
        self.assertEqual(Q37.solution(5,
                                      14,
                                      [(1, 2, 2),
                                       (1, 3, 3),
                                       (1, 4, 1),
                                       (1, 5, 10),
                                       (2, 4, 2),
                                       (3, 4, 1),
                                       (3, 5, 1),
                                       (4, 5, 3),
                                       (3, 5, 10),
                                       (3, 1, 8),
                                       (1, 4, 2),
                                       (5, 1, 7),
                                       (3, 4, 2),
                                       (5, 2, 4)]),
                         [[0, 2, 3, 1, 4],
                          [12, 0, 15, 2, 5],
                          [8, 5, 0, 1, 1],
                          [10, 7, 13, 0, 3],
                          [7, 4, 10, 6, 0]])

    def test_Q38(self):
        self.assertEqual(Q38.solution(6, 6, [(1, 5),
                                             (3, 4),
                                             (4, 2),
                                             (4, 6),
                                             (5, 2),
                                             (5, 4)
                                             ]), 1)

    def test_Q38(self):
        self.assertEqual(Q38_1.solution(6, 6, [(1, 5),
                                               (3, 4),
                                               (4, 2),
                                               (4, 6),
                                               (5, 2),
                                               (5, 4)
                                               ]), 1)

    def test_Q39(self):
        self.assertEqual(Q39.solution(3, [[5, 5, 4],
                                          [3, 9, 1],
                                          [3, 2, 7]]), 20)
        self.assertEqual(Q39.solution(5, [[3, 7, 2, 0, 1],
                                          [2, 8, 0, 9, 1],
                                          [1, 2, 1, 8, 1],
                                          [9, 8, 9, 2, 0],
                                          [3, 6, 5, 1, 5]]), 19)
        self.assertEqual(Q39.solution(7, [[9, 0, 5, 1, 1, 5, 3],
                                          [4, 1, 2, 1, 6, 5, 3],
                                          [0, 7, 6, 1, 6, 8, 5],
                                          [1, 1, 7, 8, 3, 2, 3],
                                          [9, 4, 0, 7, 6, 4, 1],
                                          [5, 8, 3, 2, 4, 8, 3],
                                          [7, 4, 8, 4, 8, 3, 4]]), 36)

    def test_Q40(self):
        self.assertEqual(Q40.solution(6, 7, [(3, 6),
                                             (4, 3),
                                             (3, 2),
                                             (1, 3),
                                             (1, 2),
                                             (2, 4),
                                             (5, 2)]), (4, 2, 3))
