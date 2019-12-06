import pytest
from garage_band import Band, Musician


def test_to_list():
    expected = [vocalist('Tatiana'), guitarist('Roman'),
                bassist('Eugene'), drummer('Vlad')]
    actual = Band.to_list()
    assert actual == expected
