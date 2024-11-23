"""A test demo"""

from uv_demo_pkg.squarer import square


def test_square():
    subject = square(4)
    assert subject == 16
