import unittest

from src.DFS_BFS import Q15, Q18, Q19


class TestBDFS(unittest.TestCase):
    def test_Q15(self):
        self.assertEqual(Q15.solution_([(1, 2), (1, 3), (2, 3), (2, 4)], 4, 4, 2, 1), [4])

    def test_Q18(self):
        self.assertEqual(Q18.solution("(()())()"), "(()())()")
        self.assertEqual(Q18.solution(")("), "()")
        self.assertEqual(Q18.solution("()))((()"), "()(())()")

    def test_Q19(self):
        # self.assertEqual(Q19.solution([5, 6], [0, 0, 1, 0]), (30, 30))
        self.assertEqual(Q19.solution([3, 4, 5], [1, 0, 1, 0]), (35, 17))
        self.assertEqual(Q19.solution([1, 2, 3, 4, 5, 6], [2, 1, 1, 1]), (54, -24))


if __name__ == '__main__':
    unittest.main()
