import unittest

from src.Graph import Q41, Q42, Q43, Q44, Q44_, Q45


class TestGraph(unittest.TestCase):
    def test_Q41(self):
        self.assertEqual(Q41.solution(5, 4,
                                      [[0, 1, 0, 1, 1],
                                       [1, 0, 0, 1, 0],
                                       [0, 0, 0, 0, 0],
                                       [1, 1, 0, 0, 0],
                                       [1, 0, 0, 0, 0]],
                                      [2, 3, 4, 3]), "YES")

    def test_Q42(self):
        self.assertEqual(Q42.solution(4, 3, [4, 1, 1]), 2)
        self.assertEqual(Q42.solution(4, 6, [2, 2, 3, 3, 4, 4]), 3)

    def test_Q43(self):
        self.assertEqual(Q43.solution(7, 11, [(0, 1, 7),
                                              (0, 3, 5),
                                              (1, 2, 8),
                                              (1, 3, 9),
                                              (1, 4, 7),
                                              (2, 4, 5),
                                              (3, 4, 15),
                                              (3, 5, 6),
                                              (4, 5, 8),
                                              (4, 6, 9),
                                              (5, 6, 11)]), 51)

    def test_Q44(self):
        self.assertEqual(Q44.solution(5, [(11, -15, -15),
                                          (14, -5, -15),
                                          (-1, -1, -5),
                                          (10, -4, -1),
                                          (19, -4, 19)]), 4)

    def test_Q44(self):
        self.assertEqual(Q44_.solution(5, [(11, -15, -15),
                                           (14, -5, -15),
                                           (-1, -1, -5),
                                           (10, -4, -1),
                                           (19, -4, 19)]), 4)

    def test_Q44(self):
        self.assertEqual(Q45.solution(5, [5, 4, 3, 2, 1],
                                      2,
                                      [(2, 4),
                                       (3, 4)]), [5, 3, 2, 4, 1])
        self.assertEqual(Q45.solution(3, [2, 3, 1], 0, []), [2, 3, 1])
        self.assertEqual(Q45.solution(4, [1, 2, 3, 4],
                                      3,
                                      [(1, 2),
                                       (3, 4),
                                       (2, 3)]), "IMPOSSIBLE")


if __name__ == '__main__':
    unittest.main()
