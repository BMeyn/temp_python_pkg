# Template for python package


[![HitCount](https://hits.dwyl.com/BMeyn/temp_python_package.svg?style=flat-square)](http://hits.dwyl.com/BMeyn/temp_python_package)
[![PyPI version](https://badge.fury.io/py/BMeyn.svg)](https://badge.fury.io/py/BMeyn)
[![codecov](https://codecov.io/gh/BMeyn/temp_python_pkg/branch/main/graph/badge.svg?token=VDV7VE33IJ)](https://codecov.io/gh/BMeyn/temp_python_pkg)
[![Python package](https://github.com/BMeyn/temp_python_pkg/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/BMeyn/temp_python_pkg/actions/workflows/python-package.yml)

![Tests Status](./docs/badget/tests-badge.svg?dummy=8484744)
![Coverage Status](./docs/badget/coverage-badge.svg?dummy=8484744)

## required action secrets
- codecov_token
  - adds test code coverage annotations to PRs
- flake8_token #TODO: rename token
  - github token for read and write access 
  - required to update PRs with actions
- pypi_test_token
  - Api token for pypi test releases
  - required for python package test release
- pypi_token
  - api token for pypi release
  - required for python package release
