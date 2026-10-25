# probabilistic

Python Probablistic work.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run

```bash
probabilistic
# or
python -m probabilistic.main
```

## Test

```bash
pytest
```

## Layout

```
probabilistic/
├── pyproject.toml
├── README.md
├── src/probabilistic/
│   ├── __init__.py
│   └── main.py
└── tests/
    └── test_main.py
```
