# /// script
# dependencies = [
#   "pyyaml"
# ]
# ///

import yaml
import os

keywords = set()
for filename in os.listdir("_members"):
    if filename.endswith(".md"):
        with open(os.path.join("_members", filename)) as f:
            content = f.readlines()[1:]
            frontmatter = yaml.safe_load("".join(content[:content.index("---\n")]))
            keywords.update(set(frontmatter.get("keywords", [])))

print(yaml.dump({"keywords": list(keywords)}))
