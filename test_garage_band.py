import pytest
from garage_band import Band, Musician, Vocalist, Guitarist, Bassist, Drummer


def test_to_list():
    expected = []
    actual = Band.to_list()
    assert actual == expected


def test_band_instance():
    assert Band()


def test_musician_instance():
    assert Musician()


def test_play_solo():
    vocals = Musician(['Tati', 'Jinjer', 'Vocals'])
    assert 'Tati is playing/singing a solo!' == vocals.play_solo()
