# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from hangman.hangman import print_hanged_man


class TestSimple(unittest.TestCase):

	def test_print_hanged_man(self):
		from io import StringIO

		out = StringIO()
		print_hanged_man(9,out)
		output= out.getvalue()
		self.assertEqual(output, "9 turns left\n  --------  \n")


if __name__ == '__main__':
    unittest.main()
