#!/usr/bin/env python
import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATH_DOCKERFILE_LOCAL = os.path.join(ROOT_DIR, "Dockerfile")
PATH_DOCKERFILE_DEPLOY = os.path.join(ROOT_DIR, "Dockerfile.deploy")

os.chdir(ROOT_DIR)
dockerfile = open(PATH_DOCKERFILE_LOCAL).read()

sub_case_list = [
    # buildkit의 Cache기능을 사용하지 않는다
    (r"--mount.*?\\", r"\\"),
    # pip install시 cache없이 설치한다
    (r"pip install", r"pip install --no-cache-dir"),
]
for pattern, repl in sub_case_list:
    dockerfile = re.sub(pattern, repl, dockerfile)

open(PATH_DOCKERFILE_DEPLOY, "wt").write(dockerfile)
