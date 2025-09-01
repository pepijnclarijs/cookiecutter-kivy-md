import os
import shutil

for root, _, files in os.walk("."):
    for filename in files:
        if filename.endswith(".jinja2"):
            src = os.path.join(root, filename)
            dst = os.path.join(root, filename.replace(".jinja2", ""))
            shutil.move(src, dst)
