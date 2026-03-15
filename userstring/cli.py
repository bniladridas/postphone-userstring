from .constants import DEFAULT_APP, DEFAULT_SYSTEM, DEFAULT_VERSION
from .generator import build_user_agent


try:
    import click  # type: ignore
except ImportError:
    click = None


if click is not None:
    @click.command()
    @click.option("--app", default=DEFAULT_APP)
    @click.option("--version", default=DEFAULT_VERSION)
    @click.option("--system", default=DEFAULT_SYSTEM)
    def main(app, version, system):
        ua = build_user_agent(app, version, system)
        click.echo(ua)
else:
    def main():
        import argparse

        parser = argparse.ArgumentParser(description="Build a user string")
        parser.add_argument("--app", default=DEFAULT_APP)
        parser.add_argument("--version", default=DEFAULT_VERSION)
        parser.add_argument("--system", default=DEFAULT_SYSTEM)
        args = parser.parse_args()
        ua = build_user_agent(args.app, args.version, args.system)
        print(ua)


if __name__ == "__main__":
    main()
