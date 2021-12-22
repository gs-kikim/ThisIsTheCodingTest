import src.DP.Q31 as Q31
import src.DP.Q32 as Q32
import src.DP.Q33 as Q33
import src.DP.Q34 as Q34
import unittest


class TestGreedy(unittest.TestCase):
    def test_Q31(self):
        self.assertEqual(Q31.DP_Q31(3, 4, [1, 3, 3, 2,
                                           2, 1, 4, 1,
                                           0, 6, 4, 7]), 19)
        self.assertEqual(Q31.DP_Q31(4, 4, [1, 3, 1, 5,
                                           2, 2, 4, 1,
                                           5, 0, 2, 3,
                                           0, 6, 1, 2]), 16)

    def test_Q32(self):
        self.assertEqual(Q32.DP_Q32(5, [7, 3, 8, 8, 1, 0, 2, 7, 4, 4, 4, 5, 2, 6, 5]), 30)

    def test_Q33(self):
        self.assertEqual(Q33.DP_Q33(7, [3, 5, 1, 1, 2, 4, 2],
                                    [10, 20, 10, 20, 15, 40, 200]), 45)
        self.assertEqual(Q33.DP_Q33(10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)
        self.assertEqual(Q33.DP_Q33(10, [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                                    [10, 9, 8, 7, 6, 10, 9, 8, 7, 6]), 20)
        self.assertEqual(Q33.DP_Q33(10, [5, 4, 3, 2, 1, 1, 2, 3, 4, 5],
                                    [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]), 90)

    def test_Q34(self):
        self.assertEqual(Q34.DP_Q34(7, [15, 11, 4, 8, 5, 2, 4]), 2)


if __name__ == '__main__':
    unittest.main()
