import unittest

from src.implement import Q7, Q8


class TestImplement(unittest.TestCase):
    def test_Q7(self):
        self.assertEqual(Q7.solution(123402), "LUCKY")
        self.assertEqual(Q7.solution(7755), "READY")

    def test_Q8(self):
        self.assertEqual(Q8.solution("K1KA5CB7"), "ABCKK13")
        self.assertEqual(Q8.solution("AJKDLSI412K4JSJ9D"), "ADDIJJJKKLSS20")


if __name__ == '__main__':
    unittest.main()
