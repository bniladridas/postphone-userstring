from userstring import build_user_agent


def main():
    ua = build_user_agent(
        app="harperbot",
        version="2.1",
        system="macOS"
    )

    print(ua)


if __name__ == "__main__":
    main()
