from userstring import build_user_agent

ua = build_user_agent(
    app="harperbot",
    version="2.1",
    system="macOS"
)

print(ua)
