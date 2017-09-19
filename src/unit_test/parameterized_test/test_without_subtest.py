from unittest import TestCase, main
from src.unit_test.parameterized_test.test_target import rock_paper_scissors


class TestRockPaperScissors(TestCase):
    """ This test case tests rock_paper_scissors method """

    def test_with_valid_params(self):

        test_params = [
            ("Rock", "Rock", "Even"),
            ("Rock", "Paper", "Player2"),
            ("Rock", "Scissor", "Player1"),
            ("Paper", "Rock", "Player1"),
            ("Paper", "Paper", "Even"),
            ("Paper", "Scissor", "Player2"),
            ("Scissor", "Rock", "Player2"),
            ("Scissor", "Paper", "Player1"),
            ("Scissor", "Scissor", "Even"),
        ]

        for p1_shape, p2_shape, expected_result in test_params:
            self.assertEqual(rock_paper_scissors(p1_shape=p1_shape, p2_shape=p2_shape), expected_result)


if __name__ == '__main__':
    main()
