
"""
Unit tests for the calculator library
"""

from RandomChecks import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_addition(self):
        assert 1000 == calculator.add(500, 5000)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(199, 2)