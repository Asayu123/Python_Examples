from test.support import captured_stdout
from unittest import TestCase

from .test_target import print_something


class StdoutCaptureTestCase(TestCase):
    def test_print_something(self):
        test_value = 'Hello'

        with captured_stdout() as stdout:  # captured_stdout() yields stream that contain strings of stdout.
            print_something(value=test_value)

        self.assertEqual(stdout.getvalue(),
                         'Hello\n')  # stdout.getvalue() returns the entire contents of stdout includes Line Feed.

    def test_multiple_lines(self):
        with captured_stdout() as stdout:
            print_something(value='Hello')
            print_something(value='World')

            lines = stdout.getvalue().splitlines()  # Splitlines method divide strings to an array, Line Feed will disappear.

        self.assertEqual(lines[0], 'Hello')
        self.assertEqual(lines[1], 'World')
