from plates import is_valid

def test_is_valid():
  assert is_valid("H") != True
  assert is_valid("SDFSDFF222") != True
  assert is_valid("AAA22A") != True
  assert is_valid("AAA222") == True
  assert is_valid("AAA022") != True
  assert is_valid("AA, !22") != True