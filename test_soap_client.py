from soap_client import convert_number_to_words

def test_number_to_words():
    result = convert_number_to_words(456)
    assert "four hundred" in result.lower()
