import unittest

from src.implement import Q7, Q8, Q9, Q10, Q11


class TestImplement(unittest.TestCase):
    def test_Q7(self):
        self.assertEqual(Q7.solution(123402), "LUCKY")
        self.assertEqual(Q7.solution(7755), "READY")

    def test_Q8(self):
        self.assertEqual(Q8.solution("K1KA5CB7"), "ABCKK13")
        self.assertEqual(Q8.solution("AJKDLSI412K4JSJ9D"), "ADDIJJJKKLSS20")
        self.assertEqual(Q8.solution("ABCDE"), "ABCDE")# ABCDE0

    def test_Q9(self):
        self.assertEqual(Q9.solution("aabbaccc"), 7)
        self.assertEqual(Q9.solution("ababcdcdababcdcd"), 9)
        self.assertEqual(Q9.solution("abcabcdede"), 8)
        self.assertEqual(Q9.solution("abcabcabcabcdededededede"), 14)
        self.assertEqual(Q9.solution("xababcdcdababcdcd"), 17)

    def test_Q10(self):
        self.assertEqual(Q10.solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
                                      [[1, 1, 1], [1, 1, 0], [1, 0, 1]]), True)

    def test_Q11(self):
        self.assertEqual(Q11.solution(6, 3, [(3, 4), (2, 5), (5, 3)], 3, [(3, "D"), (15, 'L'), (17, 'D')]), 9)
        self.assertEqual(
            Q11.solution(10, 4, [(1, 2), (1, 3), (1, 4), (1, 5)], 4, [(8, "D"), (10, "D"), (11, "D"), (13, "L")]), 21)
        self.assertEqual(
            Q11.solution(10, 5, [(1, 5), (1, 3), (1, 2), (1, 6), (1, 7)], 4,
                         [(8, "D"), (10, 'D'), (11, 'D'), (13, 'L')]), 13)



if __name__ == '__main__':
    unittest.main()
