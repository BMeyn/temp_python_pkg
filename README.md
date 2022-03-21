# Template for python package test

![banner](docs/images/668F6A24-209D-4B91-AFF7-D9F77DD37707.png)

[![HitCount](https://hits.dwyl.com/BMeyn/temp_python_package.svg?style=flat-square)](http://hits.dwyl.com/BMeyn/temp_python_package)
[![PyPI version](https://badge.fury.io/py/BMeyn.svg)](https://badge.fury.io/py)
![Tests Status](docs/badget/tests-badget.svg?dummy=8484744)
![Coverage Status](docs/badget/coverage-badget.svg?dummy=8484744)


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
