import src.DP.Q31 as Q31
import src.DP.Q32 as Q32
import unittest


class TestGreedy(unittest.TestCase):
    def test_Q31(self):
        self.assertEqual(Q31.DP_Q31(3, 4, [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]), 19)
        self.assertEqual(Q31.DP_Q31(4, 4, [1, 3, 1, 5, 2, 24, 1, 5, 0, 2, 3, 0, 6, 1, 2]), 16)

    def test_Q32(self):
        self.assertEqual(Q32.DP_Q32(5, [7, 3, 8, 8, 1, 0, 2, 7, 4, 4, 4, 5, 2, 6, 5]), 30)


if __name__ == '__main__':
    unittest.main()
