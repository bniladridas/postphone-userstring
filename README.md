# PostPhone User String

A quiet specification for a user string that signals focus, intentional computing, and steady progress without cell phones.

Example string:

PostPhone/1.0 (Desktop; NoCell; Progress)

## Python utility

The `userstring` package delivers the same format as a tiny Python API and CLI. Install it with `pip install -e .` to pull in the `click` runtime dependency so the CLI runs automatically; add `pip install -e '.[dev]'` when you need the `pytest` suite. After installation you can import `build_user_agent` or run `python -m userstring.cli`.

## Repository Structure

metadata/
    JSON and tooling context; see reference/metadata-management.md for alignment notes

docs/webpage.html
    Full-page summary that records the truth of every touched area

spec/
    Formal rules for the string format

philosophy/
    Motivations, manifesto, and guiding principles

reference/
    Examples, environment keys, and metadata guidance

implementations/
    Minimal generators that reproduce the PostPhone string
