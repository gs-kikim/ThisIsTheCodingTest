import src.greedy.Q1 as Q1
import src.greedy.Q6 as Q6
import unittest


class TestGreedy(unittest.TestCase):
    def test_Q1(self):
        self.assertEqual(Q1.greedy_Q1(5, [2, 1, 3, 2, 2]), 2)
        self.assertEqual(Q1.greedy_Q1(5, [2, 3, 1, 2, 2]), 2)
        self.assertEqual(Q1.greedy_Q1(5, [2, 1, 2, 2, 2]), 3)

    def test_Q6(self):
        self.assertEqual(Q6.greedy_Q6([3, 2, 1], 5), 1)
        self.assertEqual(Q6.greedy_Q6([0, 0, 0, 3, 1, 2, 0], 5), 4)


if __name__ == '__main__':
    unittest.main()
