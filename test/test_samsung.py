import unittest

from src.Samsung import Q46


class TestSamsung(unittest.TestCase):
    def test_Q46(self):
        self.assertEqual(Q46.solution(3, [[0, 0, 0],
                                          [0, 0, 0]
                                          [0, 9, 0]]), 0)
        self.assertEqual(Q46.solution(3, [[0, 0, 1],
                                          [0, 0, 0]
                                          [0, 9, 0]]), 3)

        self.assertEqual(Q46.solution(4, [[4, 3, 2, 1],
                                          [0, 0, 0, 0],
                                          [0, 0, 9, 0],
                                          [1, 2, 3, 4]]), 14)

if __name__ == '__main__':
    unittest.main()
