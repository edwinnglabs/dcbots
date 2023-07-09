from __future__ import print_function

import sys

from setuptools import dist, setup, find_packages
from setuptools.command.build_py import build_py
from setuptools.command.develop import develop
from setuptools.command.test import test as test_command

DESCRIPTION = "Creating discord bots and webhooks with Python"
AUTHOR = '''Edwin Ng <edwinnglabs@gmail.com>'''

def read_long_description(filename="README.md"):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().strip()

def requirements(filename="requirements.txt"):
    with open(filename) as f:
        return f.readlines()

setup(
    author=AUTHOR,
    author_email='edwinnglabs@gmail.com',
    description=DESCRIPTION,
    include_package_data=True,
    install_requires=requirements('requirements.txt'),
    cmdclass={
        'build_py': build_py,
        'develop': develop,
    },
    long_description=read_long_description(),
    name='dcbots',
    packages=find_packages(),
    # version=VERSION, # being maintained by source module
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.9',
    ]
)