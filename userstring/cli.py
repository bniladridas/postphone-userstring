import argparse
from .generator import build_user_agent


try:
    import click  # type: ignore
except ImportError:
    click = None


if click is not None:
    @click.command()
    @click.option("--app", default="userstring")
    @click.option("--version", default="0.0.1")
    @click.option("--system", default="unknown")
    def main(app, version, system):
        ua = build_user_agent(app, version, system)
        click.echo(ua)
else:
    def main():
        parser = argparse.ArgumentParser(description="Build a user string")
        parser.add_argument("--app", default="userstring")
        parser.add_argument("--version", default="0.0.1")
        parser.add_argument("--system", default="unknown")
        args = parser.parse_args()
        ua = build_user_agent(args.app, args.version, args.system)
        print(ua)


if __name__ == "__main__":
    main()
