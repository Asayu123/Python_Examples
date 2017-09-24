from unittest import TestCase
from src.unit_test.parameterized_test.test_target import rock_paper_scissors


class TestRockPaperScissors(TestCase):
    """ This test case tests rock_paper_scissors method """

    def test_with_valid_params(self):
        """
        With SubTest, All patterns will be tested even if there are some failures.
        Consequently, we can test all patterns every time.
        """

        test_patterns = [
            ("Rock", "Rock", "Even"),  # Will pass.
            ("Rock", "Paper", "Player2"),  # Will pass.
            ("Rock", "Scissor", "Player1"),  # Will fail by bugs, and the test result shows test parameters as well.
            ("Paper", "Rock", "Player1"),  # Will pass.
            ("Paper", "Paper", "Even"),  # Will pass.
            ("Paper", "Scissor", "Player2"),  # Will fail by bugs, and the test result shows test parameters as well.
            ("Scissor", "Rock", "Player2"),  # Will pass.
            ("Scissor", "Paper", "Player1"),  # Will pass.
            ("Scissor", "Scissor", "Even"),  # Will pass.
        ]

        for p1_shape, p2_shape, expected_result in test_patterns:
            with self.subTest(p1_shape=p1_shape, p2_shape=p2_shape):
                self.assertEqual(rock_paper_scissors(p1_shape=p1_shape, p2_shape=p2_shape), expected_result)
