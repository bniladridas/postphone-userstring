def build_user_string(
    app="PostPhone",
    version="1.0",
    attributes=None
):
    if attributes is None:
        attributes = ["Desktop", "NoCell", "Progress"]

    return f"{app}/{version} ({'; '.join(attributes)})"


if __name__ == "__main__":
    print(build_user_string())
