# PostPhone User String

A quiet specification for a user string that signals focus, intentional computing, and steady progress without cell phones.

Example string:

PostPhone/1.0 (Desktop; NoCell; Progress)

## Python utility

The `userstring` package delivers the same format as a tiny Python API and CLI. Install it with `pip install -e '.[cli]'` to get the optional click-based command or `pip install -e '.[dev]'` when you need the tests. After installation you can import `build_user_agent` or run `python -m userstring.cli` (it falls back to `argparse` when `click` is absent).

## Repository Structure

metadata/
    JSON and tooling context; see reference/metadata-management.md for alignment notes

webpage.html
    Clean HTML introduction to the Project’s tone and structure

spec/
    Formal rules for the string format

philosophy/
    Motivations, manifesto, and guiding principles

reference/
    Examples, environment keys, and metadata guidance

implementations/
    Minimal generators that reproduce the PostPhone string
