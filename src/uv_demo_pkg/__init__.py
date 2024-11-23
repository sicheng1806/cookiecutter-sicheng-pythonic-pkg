"""uv-demo-pkg"""

__version__ = "0.1.0"
from .squarer import square


def main() -> None:
    print("Hello from uv-demo-pkg!")
    n = 4
    print(f"The square of {n} is {square(n)}")
