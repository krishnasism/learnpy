[![Unit tests](https://github.com/krishnasism/learnpy/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/krishnasism/learnpy/actions/workflows/test.yml)

# learnpy

A rustlings inspired python hands on coding journey


## Start Learning!

1. Clone this repository
2. Install dependencies
```zsh
# Navigate to repo
cd learnpy

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install requirements
pip install -e .
```
3. Start coding!
```zsh
learn-py start
```
4. Go to any exercise under `exercises` and start coding as instructed. Start with `0000_intro.py` to understand all the features!

**NOTE:** You can only run `learn-py` from the `learnpy` directory.

---

# Local Development
```zsh
# Create a venv
uv venv

# Activate venv
source .venv/bin/activate

# Install deps
uv pip install -e .

# Install dev deps
uv pip install -r requirements-dev.txt

# Run
learn-py start
```

## Tests
```zsh
pytest tests/
```
