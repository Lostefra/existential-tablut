import unittest

import numpy as np

from src.search.utils import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_legal_actions(self):
        white_result = [(2, 2, 25), (2, 2, 24), (2, 2, 8), (2, 2, 1),
                        (2, 2, 0), (2, 2, 16), (2, 2, 17), (2, 2, 18),
                        (2, 2, 19), (2, 2, 20), (2, 2, 21), (2, 4, 24),
                        (2, 4, 8), (2, 4, 9), (3, 4, 26), (3, 4, 25), (3, 4,
                                                                       24),
                        (3, 4, 8), (3, 4, 9), (3, 4, 10), (4, 3, 24), (4, 3,
                                                                       2),
                        (4, 3, 1), (4, 3, 0), (4, 3, 16), (4, 3, 17),
                        (4, 3, 18), (4, 5, 2), (4, 5, 1), (4, 5, 0),
                        (4, 5, 16), (4, 5, 17), (4, 5, 18),
                        (4, 6, 3), (4, 6, 2), (4, 6, 1), (4, 6, 0), (4, 6, 16),
                        (4, 6, 17), (4, 6, 18), (4, 6, 19), (5, 4, 26),
                        (5, 4, 25), (5, 4, 24), (5, 4, 8), (5, 4, 9), (5, 4,
                                                                       10),
                        (6, 4, 27), (6, 4, 26), (6, 4, 25), (6, 4, 24),
                        (6, 4, 8), (6, 4, 9), (6, 4, 10), (6, 4, 11)]
        black_result = [(0, 3, 26), (0, 3, 25), (0, 3, 24), (0, 3, 16),
                        (0, 3, 17), (0, 3, 18), (0, 5, 8), (0, 5, 9),
                        (0, 5, 10), (0, 5, 16), (0, 5, 17), (0, 5, 18),
                        (1, 4, 27), (1, 4, 26), (1, 4, 25), (1, 4, 24),
                        (1, 4, 8), (1, 4, 9),
                        (1, 4, 10), (1, 4, 11), (2, 7, 25), (2, 7, 24),
                        (2, 7, 8), (2, 7, 1), (2, 7, 0), (2, 7, 16), (3, 0, 8),
                        (3, 0, 9), (3, 0, 10), (3, 0, 2), (3, 0, 1), (3, 0, 0),
                        (3, 8, 26), (3, 8, 25),
                        (3, 8, 24), (3, 8, 2), (3, 8, 1), (3, 8, 0), (4, 1, 8),
                        (4, 1, 3), (4, 1, 2), (4, 1, 1), (4, 1, 0), (4, 1, 16),
                        (4, 1, 17), (4, 1, 18), (4, 1, 19), (4, 8, 24),
                        (5, 0, 8), (5, 0, 9),
                        (5, 0, 10), (5, 0, 16), (5, 0, 17), (5, 0, 18),
                        (5, 8, 26), (5, 8, 25), (5, 8, 24), (5, 8, 16),
                        (5, 8, 17), (5, 8, 18), (7, 4, 27), (7, 4, 26),
                        (7, 4, 25), (7, 4, 24), (7, 4, 8), (7, 4, 9), (7, 4,
                                                                       10),
                        (7, 4, 11), (8, 3, 26), (8, 3, 25), (8, 3, 24),
                        (8, 3, 2), (8, 3, 1), (8, 3, 0), (8, 5, 8), (8, 5, 9),
                        (8, 5, 10), (8, 5, 2), (8, 5, 1), (8, 5, 0)]

        w_pawns = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 1, 1, 0, 0],
                            [0, 0, 0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        w_king = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        b_pawns = np.array([[0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [1, 0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 1, 0, 0, 0, 0, 0, 0, 1],
                            [1, 0, 0, 0, 0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 1, 1, 1, 0, 0, 0]])
        random_layer = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 1, 1, 1, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        white_turn = np.zeros((1, 9, 9), dtype='bool')

        white_state = self.__create_state(w_pawns, w_king, b_pawns,
                                          random_layer, white_turn)
        white_actions = self.game.legal_actions(white_state)
        self.assertEqual(white_actions, white_result)

        black_turn = np.ones((1, 9, 9), dtype='bool')
        black_state = self.__create_state(w_pawns, w_king, b_pawns,
                                          random_layer, black_turn)
        black_actions = self.game.legal_actions(black_state)
        self.assertEqual(black_actions, black_result)

    def test_terminal(self):
        w_pawns = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        random_layer = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 1, 1, 1, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        black_turn = np.ones((1, 9, 9), dtype='bool')

        print("King captured in throne")
        w_king = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        b_pawns = np.array([[0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 1, 0, 0, 0, 1],
                            [1, 0, 0, 1, 0, 1, 0, 0, 1],
                            [1, 0, 0, 0, 1, 0, 0, 0, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 1, 1, 0, 0, 0]])
        state = self.__create_state(w_pawns, w_king, b_pawns, random_layer,
                                    black_turn)
        self.assertTrue(self.game.terminal(state))

        print("King not captured in throne")
        w_king = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        b_pawns = np.array([[0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 1, 0, 0, 0, 1],
                            [1, 0, 1, 0, 0, 1, 0, 0, 1],
                            [1, 0, 0, 0, 1, 0, 0, 0, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 1, 1, 0, 0, 0]])
        state = self.__create_state(w_pawns, w_king, b_pawns, random_layer,
                                    black_turn)
        self.assertFalse(self.game.terminal(state))

        print("King captured next to the throne")
        w_king = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        b_pawns = np.array([[0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 1, 0, 0, 0, 0, 1],
                            [1, 0, 1, 0, 0, 0, 1, 0, 1],
                            [1, 0, 0, 1, 0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 1, 1, 0, 0, 0]])
        state = self.__create_state(w_pawns, w_king, b_pawns, random_layer,
                                    black_turn)
        self.assertTrue(self.game.terminal(state))

        print("King not captured next to the throne")
        w_king = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        b_pawns = np.array([[0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 0, 1, 0, 0, 0, 1, 0, 1],
                            [1, 0, 0, 1, 0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 1, 1, 0, 0, 0]])
        state = self.__create_state(w_pawns, w_king, b_pawns, random_layer,
                                    black_turn)
        self.assertFalse(self.game.terminal(state))

        print("King captured by two sides")
        w_king = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        b_pawns = np.array([[0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 1, 0, 1, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 0, 0, 1, 0, 1],
                            [1, 0, 0, 0, 1, 0, 0, 0, 1],
                            [0, 0, 0, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 1, 1, 0, 0, 0]])
        state = self.__create_state(w_pawns, w_king, b_pawns, random_layer,
                                    black_turn)
        self.assertTrue(self.game.terminal(state))

        print("King next to throne not captured by two sides")
        w_king = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        b_pawns = np.array([[0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 0, 0, 0, 0],
                            [1, 0, 0, 1, 0, 0, 0, 0, 1],
                            [1, 0, 0, 0, 0, 0, 1, 0, 1],
                            [1, 0, 0, 1, 1, 0, 0, 0, 1],
                            [0, 0, 0, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 1, 1, 0, 0, 0]])
        state = self.__create_state(w_pawns, w_king, b_pawns, random_layer,
                                    black_turn)
        self.assertFalse(self.game.terminal(state))

        print("King in throne not captured by two sides")
        w_king = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        b_pawns = np.array([[0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 1, 0, 0, 0, 1],
                            [1, 0, 1, 0, 0, 0, 1, 0, 1],
                            [1, 0, 0, 0, 1, 0, 0, 0, 1],
                            [0, 0, 0, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 1, 1, 0, 0, 0]])
        state = self.__create_state(w_pawns, w_king, b_pawns, random_layer,
                                    black_turn)
        self.assertFalse(self.game.terminal(state))

    @staticmethod
    def __create_state(w_pawns, w_king, b_pawns, r_layer, turn):
        white_planes = np.tile([w_pawns, w_king], (8, 1, 1))
        black_planes = np.tile(b_pawns, (8, 1, 1))
        random_planes = np.tile(r_layer, (8, 1, 1))

        return np.concatenate(
            [white_planes, black_planes, random_planes, turn])


if __name__ == '__main__':
    unittest.main()