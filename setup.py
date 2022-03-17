"""Setup.py script for packaging project."""

from setuptools import setup, find_packages

import json
import os


with open('requirements.txt') as f:
    required = f.read().splitlines()

if __name__ == '__main__':
    setup(
        name='BMeyn',
        use_scm_version=True,
        #version=os.getenv('PACKAGE_VERSION', '0.0.dev0'),
        package_dir={'': 'src'},
        packages=find_packages('src', include=[
            'demo*'
        ]),
        description='A demo package.',
        install_requires= required
    )
