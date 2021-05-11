#!/usr/bin/env python
import subprocess
import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
VERSION_FILE = os.path.join(ROOT_DIR, "version.txt")

if __name__ == "__main__":
    # Write new version
    previous_version = open(VERSION_FILE).read()
    main, minor = previous_version.rsplit(".", 1)
    new_version = "{main}.{minor}".format(main=main, minor=int(minor) + 1)
    open(VERSION_FILE, "wt").write(new_version)

    # Generating distribution archives
    subprocess.run("python setup.py sdist bdist_wheel", shell=True)
    # Upload the distribution archives
    subprocess.run("twine upload dist/*", shell=True)
