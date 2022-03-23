import unittest

from src.Graph import Q41, Q42


class TestGraph(unittest.TestCase):
    def test_Q41(self):
        self.assertEqual(Q41.solution(5, 4,
                                      [[0, 1, 0, 1, 1],
                                       [1, 0, 1, 1, 0],
                                       [0, 1, 0, 0, 0],
                                       [1, 1, 0, 0, 0],
                                       [1, 0, 0, 0, 0]],
                                      [2, 3, 4, 3]), "YES")

    def test_Q42(self):
        self.assertEqual(Q42.solution(4, 3, [4, 1, 1]), 2)
        self.assertEqual(Q42.solution(4, 6, [2, 2, 3, 3, 4, 4]), 3)


if __name__ == '__main__':
    unittest.main()
