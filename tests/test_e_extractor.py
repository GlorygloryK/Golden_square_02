from lib.e_extractor import e_extractor


"""
Scenario 1 : String without an e returns the same string given 
"""
def test_return_string_with_no_e():
    result = e_extractor("going")
    assert result == "going"

"""
Scenario 2 : When person returns an empty string , the empty string is returned
"""
def test_return_string_with_no_e():
    result = e_extractor("")
    assert result == ""

"""
Scenario 3 : When person returns an empty string , the empty string is returned
"""
def test_return_string_with_no_e():
    result = e_extractor("nice")
    assert result == "enic"