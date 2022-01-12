import unittest

import src.Array.Q23 as Q23
from src.Array import Q24, Q25, Q26


class TestGreedy(unittest.TestCase):
    def test_Q23(self):
        self.assertEqual(Q23.array_Q23(12, ['Junkyu 50 60 100',
                                            'Sangkeun 80 60 50',
                                            'Sunyoung 80 70 100',
                                            'Soong 50 60 90',
                                            'Haebin 50 60 100',
                                            'Kangsoo 60 80 100',
                                            'Donghyuk 80 60 100',
                                            'Sei 70 70 70',
                                            'Wonseob 70 70 90',
                                            'Sanghyun 70 70 80',
                                            'nsj 80 80 80',
                                            'Taewhan 50 60 90']),
                         ['Donghyuk', 'Sangkeun', 'Sunyoung', 'nsj', 'Wonseob', 'Sanghyun', 'Sei', 'Kangsoo', 'Haebin',
                          'Junkyu', 'Soong', 'Taewhan'])

    def test_Q23(self):
        self.assertEqual(Q23.array_Q23(12, [
            'Sei 70 70 70',
            'Wonseob 70 70 70',
            'Sanghyun 70 70 70',
            'Taewhan 70 70 70']),
                         ['Donghyuk', 'Sangkeun', 'Sunyoung', 'nsj', 'Wonseob', 'Sanghyun', 'Sei', 'Kangsoo', 'Haebin',
                          'Junkyu', 'Soong', 'Taewhan'])

    def test_Q24(self):
        self.assertEqual(Q24.array_Q24(4, [5, 1, 7, 9]), 5)

    def test_Q25(self):
        self.assertEqual(Q25.solution(5, [2, 1, 2, 6, 2, 4, 3, 3]), [3, 4, 2, 1, 5])
        self.assertEqual(Q25.solution(4, [4, 4, 4, 4, 4]), [4, 1, 2, 3])

    def test_Q26(self):
        self.assertEqual(Q26.solution(3, [10, 20, 40]), 100)
        self.assertEqual(Q26.s2(3, [10, 20, 40]), 100)


if __name__ == '__main__':
    unittest.main()
