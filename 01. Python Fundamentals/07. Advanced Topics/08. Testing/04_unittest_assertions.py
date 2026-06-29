# 04 — unittest assertion methods
# Run: python 04_unittest_assertions.py
#
# TestCase gives many readable assert helpers. Prefer the specific one —
# it produces clearer failure messages than a plain assertEqual.

import unittest

class TestAssertions(unittest.TestCase):
    # --- 1. Equality and truthiness ---
    def test_equality(self):
        self.assertEqual(2 + 2, 4)
        self.assertNotEqual(2 + 2, 5)

    def test_boolean(self):
        self.assertTrue(3 > 1)
        self.assertFalse(1 > 3)

    # --- 2. None and identity ---
    def test_none(self):
        value = None
        self.assertIsNone(value)
        self.assertIsNotNone(123)

    # --- 3. Membership ---
    def test_membership(self):
        self.assertIn("a", "cat")
        self.assertNotIn("z", "cat")

    # --- 4. Types ---
    def test_types(self):
        self.assertIsInstance(5, int)
        self.assertNotIsInstance("5", int)

    # --- 5. Comparisons and floats ---
    def test_numbers(self):
        self.assertGreater(10, 5)
        self.assertLessEqual(5, 5)
        self.assertAlmostEqual(0.1 + 0.2, 0.3)   # handles float rounding

    # --- 6. Collections ---
    def test_collections(self):
        self.assertListEqual([1, 2], [1, 2])
        self.assertDictEqual({"a": 1}, {"a": 1})

if __name__ == "__main__":
    unittest.main(verbosity=2)
