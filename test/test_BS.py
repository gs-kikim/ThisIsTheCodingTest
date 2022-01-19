import unittest

from src.BinarySearch import Q27, Q28


class TestGreedy(unittest.TestCase):
    def test_Q27(self):
        self.assertEqual(Q27.solution([1, 1, 2, 2, 2, 2, 3], 2), 4)
        self.assertEqual(Q27.solution([1, 1, 2, 2, 2, 2, 3], 4), -1)
        self.assertEqual(Q27.bisect_solution([1, 1, 2, 2, 2, 2, 3], 2), 4)
        self.assertEqual(Q27.bisect_solution([1, 1, 2, 2, 2, 2, 3], 4), -1)

    def test_Q28(self):
        self.assertEqual(Q28.solution(5, [-15, -6, 1, 3, 7]), 3)
        self.assertEqual(Q28.solution(7, [-15, -4, 2, 8, 9, 13, 15]), 2)
        self.assertEqual(Q28.solution(7, [-15, -4, 3, 8, 9, 13, 15]), -1)



if __name__ == '__main__':
    unittest.main()
