function buildUserString(
  app = "PostPhone",
  version = "1.0",
  attributes = ["Desktop", "NoCell", "Progress"]
) {
  return `${app}/${version} (${attributes.join("; ")})`;
}

console.log(buildUserString());
