"""Setup.py script for packaging project."""

from setuptools import setup, find_packages

import json
import os


with open('requirements.txt') as f:
    required = f.read().splitlines()

if __name__ == '__main__':
    setup(
        name='BMeyn',
        version=os.getenv('PACKAGE_VERSION'),
        package_dir={'': 'src'},
        packages=find_packages('src', include=[
            'demo*'
        ]),
        description='A demo package.',
        install_requires= required
    )
