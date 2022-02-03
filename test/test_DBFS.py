import unittest

from src.DFS_BFS import Q15


class TestBDFS(unittest.TestCase):
    def test_Q15(self):
        self.assertEqual(Q15.solution_([(1,2),(1,3),(2,3),(2,4)],4,4,2,1), [4])

if __name__ == '__main__':
    unittest.main()