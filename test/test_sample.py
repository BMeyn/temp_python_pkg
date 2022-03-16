import pytest

from src.sample import sample

def test_sample():
  res = sample()
  assert res == 'Hello World'
