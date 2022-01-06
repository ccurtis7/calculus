import numpy as np
from calculus import derivative, integral


class Testderivative:
    def test_one(self):
        x = np.array([0, 1, 2]).astype(float)
        y = np.array([0, 1, 2]).astype(float)

        dyr = np.array([1, 1]).astype(float)
        dyi = derivative(y, x)
        np.testing.assert_almost_equal(dyr, dyi)

    def test_two(self):
        x = np.array([0, 1, 2]).astype(float)
        y = np.array([0, -1, -2]).astype(float)

        dyr = np.array([-1, -1]).astype(float)
        dyi = derivative(y, x)
        np.testing.assert_almost_equal(dyr, dyi)

    def test_three(self):
        x = np.array([0, 1, 2]).astype(float)
        y = np.array([0, 1, 0]).astype(float)

        dyr = np.array([1, -1]).astype(float)
        dyi = derivative(y, x)
        np.testing.assert_almost_equal(dyr, dyi)


class Testintegral:
    def test_one(self):
        x = np.array([0, 1, 2]).astype(float)
        y = np.array([0, 1, 2]).astype(float)

        iyr = np.array([0.5, 2.0]).astype(float)
        iyi = integral(y, x)
        np.testing.assert_almost_equal(iyr, iyi)

    def test_two(self):
        x = np.array([0, 1, 2]).astype(float)
        y = np.array([0, -1, -2]).astype(float)

        iyr = np.array([-0.5, -2.0]).astype(float)
        iyi = integral(y, x)
        np.testing.assert_almost_equal(iyr, iyi)

    def test_three(self):
        x = np.array([0, 1, 2]).astype(float)
        y = np.array([0, 1, 0]).astype(float)

        iyr = np.array([0.5, 1.0]).astype(float)
        iyi = integral(y, x)
        np.testing.assert_almost_equal(iyr, iyi)
