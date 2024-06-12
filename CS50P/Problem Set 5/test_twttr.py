from twttr import shorten

def test_shorten():
  assert shorten("twitter") == "twttr"
  assert shorten("aeIOU") == ""
  assert shorten("zxcvbnm123") == "zxcvbnm123"