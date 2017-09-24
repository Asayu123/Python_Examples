from unittest import TestCase
from src.unit_test.parameterized_test.test_target import rock_paper_scissors


class TestRockPaperScissors(TestCase):
    """ This test case tests rock_paper_scissors method """

    def test_with_valid_params(self):
        """
        Without SubTest, Test will exit on first failure.
        Consequently, we can not test all patterns.
        """

        test_patterns = [
            ("Rock", "Rock", "Even"),  # Will pass.
            ("Rock", "Paper", "Player2"),  # Will pass.
            ("Rock", "Scissor", "Player1"),  # The Unit test will fail with this parameter. Even worse, we can't know that failed test parameters from the test result.
            ("Paper", "Rock", "Player1"),  # Following parameters are not tested because the test exits on the first failure.
            ("Paper", "Paper", "Even"),
            ("Paper", "Scissor", "Player2"),  # This pattern should fail by bugs, but won't be detected thanks to above failure.
            ("Scissor", "Rock", "Player2"),
            ("Scissor", "Paper", "Player1"),
            ("Scissor", "Scissor", "Even"),
        ]

        for p1_shape, p2_shape, expected_result in test_patterns:
            self.assertEqual(rock_paper_scissors(p1_shape=p1_shape, p2_shape=p2_shape), expected_result)
