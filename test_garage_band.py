import pytest
from garage_band import Band, Musician


def test_to_list():
    expected = []
    actual = Band.to_list()
    assert actual == expected
