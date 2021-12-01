import src.greedy.Q1 as Q1
import src.greedy.Q6 as Q6
import src.greedy.Q2 as Q2
import src.greedy.Q3 as Q3
import unittest


class TestGreedy(unittest.TestCase):
    def test_Q1(self):
        self.assertEqual(Q1.greedy_Q1(5, [2, 1, 3, 2, 2]), 2)
        self.assertEqual(Q1.greedy_Q1(5, [2, 3, 1, 2, 2]), 2)
        self.assertEqual(Q1.greedy_Q1(5, [2, 1, 2, 2, 2]), 3)

    def test_Q6(self):
        self.assertEqual(Q6.greedy_Q6([3, 2, 1], 5), 1)
        self.assertEqual(Q6.greedy_Q6([0, 0, 0, 3, 1, 2, 0], 5), 4)

    def test_Q2(self):
        self.assertEqual(Q2.greedy_Q2("0294"), 576)
        self.assertEqual(Q2.greedy_Q2("567"), 210)

    def test_Q3(self):
        self.assertEqual(Q3.greedy_Q3("0001100"), 1)
        self.assertEqual(Q3.greedy_Q3("11111"), 0)
        self.assertEqual(Q3.greedy_Q3("00000001"), 1)
        self.assertEqual(Q3.greedy_Q3("11001100110011000001"), 4)
        self.assertEqual(Q3.greedy_Q3("11101101"), 2)

    def test_Q3_1(self):
        self.assertEqual(Q3.backjun_1("0001100"), 1)
        self.assertEqual(Q3.backjun_1("11111"), 0)
        self.assertEqual(Q3.backjun_1("00000001"), 1)
        self.assertEqual(Q3.backjun_1("11001100110011000001"), 4)
        self.assertEqual(Q3.backjun_1("11101101"), 2)


if __name__ == '__main__':
    unittest.main()
