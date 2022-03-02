import unittest

from src.DFS_BFS import Q15, Q18, Q19, Q21, Q22


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

    def test_Q21(self):
        self.assertEqual(Q21.solution(2, 20, 50, [[50, 30], [20, 40]]), 1)
        self.assertEqual(Q21.solution(2, 40, 50, [[50, 30], [20, 40]]), 0)
        self.assertEqual(Q21.solution(2, 20, 50, [[50, 30], [30, 40]]), 1)
        self.assertEqual(Q21.solution(3, 5, 10, [[10, 15, 20],
                                                 [20, 30, 25],
                                                 [40, 22, 10]]), 2)
        self.assertEqual(Q21.solution(4, 10, 50,
                                      [[10, 100, 20, 90],
                                       [80, 100, 60, 70],
                                       [70, 20, 30, 40],
                                       [50, 20, 100, 10]]), 3)

    def test_Q22(self):
        self.assertEqual(Q22.solution([[0, 0, 0, 1, 1],
                                       [0, 0, 0, 1, 0],
                                       [0, 1, 0, 1, 1],
                                       [1, 1, 0, 0, 1],
                                       [0, 0, 0, 0, 0], ]), 7)

        if __name__ == '__main__':
            unittest.main()
