"""Entry point for the probabilistic project."""

from probabilistic import __version__


def greet(name: str = "world") -> str:
    return f"Hello, {name}! (probabilistic v{__version__})"


def main() -> None:
    print(greet())


if __name__ == "__main__":
    main()
