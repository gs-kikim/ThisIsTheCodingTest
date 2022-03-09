import unittest

from src.SP import Q37, Q38, Q38_1


class TestShortestPathProblem(unittest.TestCase):
    def test_Q27(self):
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

    def test_Q28(self):
        self.assertEqual(Q38.solution(6, 6, [(1, 5),
                                             (3, 4),
                                             (4, 2),
                                             (4, 6),
                                             (5, 2),
                                             (5, 4)
                                             ]), 1)

    def test_Q28(self):
        self.assertEqual(Q38_1.solution(6, 6, [(1, 5),
                                             (3, 4),
                                             (4, 2),
                                             (4, 6),
                                             (5, 2),
                                             (5, 4)
                                             ]), 1)
