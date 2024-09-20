#!/usr/bin/env python
import os

from setuptools import find_packages, setup

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
README = open(os.path.join(ROOT_DIR, "README.md")).read()
VERSION = open(os.path.join(ROOT_DIR, "version.txt")).read()

setup(
    name="django-quill-editor",
    version=VERSION,
    url="https://github.com/LeeHanYeong/django-quill-editor",
    author="lhy",
    author_email="dev@lhy.kr",
    license="MIT",
    description="Integrate Quill editor with Django project.",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["test*", "sample"]),
    include_package_data=True,
    install_requires=[
        "django>=3.2",
    ],
    python_requires=">3.8",
    zip_safe=True,
    classifiers=[
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Development Status :: 4 - Beta",
    ],
)
