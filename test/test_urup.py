import unittest

from urup import to_md


class TestUrup(unittest.TestCase):
    def test_valid(self):
        code = r'''
"""
Heading
=======

Some maths goes like $\bm \sigma$.
"""

def add(a, b):
    return a + b'''

        expected = r'''
Heading
=======

Some maths goes like $\boldsymbol \sigma$.

~~~py
def add(a, b):
    return a + b
~~~
'''
        self.assertEqual(to_md.convert(code), expected)

    def test_start_with_code(self):
        code = r'''
def add(a, b):
    return a + b
"""
This was some code.
"""'''
        self.assertRaises(AssertionError, to_md.convert, code)

if __name__ == "__main__":
    unittest.main()
