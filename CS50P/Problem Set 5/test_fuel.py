from fuel import convert, gauge
import pytest


def test_convert():
    with pytest.raises(ValueError):
      convert("123")
    with pytest.raises(ValueError):
      convert("cat/dog")
    with pytest.raises(ValueError):
      convert("5/3")
    with pytest.raises(ZeroDivisionError):
      convert("3/0")
    assert convert("2/4") == 50


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(15) == "15%"