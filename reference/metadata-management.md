# Metadata Management

This repository keeps project metadata deliberately small and human-readable so it can back a specification-style workflow.

Key files:

- `.codex/settings.json`
    captures the project name, model/infra pair, and the default tooling mode; update it when the spec needs different metadata or tooling defaults.
    The `model` entry is a conceptual label describing the spec-focused profile (not a runtime AI configuration). Update `model_description` if you need to explain a different persona or tooling narrative.
- `metadata/repro.json`
    keeps the reproducible commands that exercise the generators and the `uv run` flow; extend this list whenever new verification steps are added.
- `LICENSE`, `CONTRIBUTING.md`, and `README.md`
    describe the sharing model and contribution expectations tied to the metadata in the adjacent folders.

When changing metadata, keep consistency between the description files (README) and config files so readers immediately understand which tools to run.
