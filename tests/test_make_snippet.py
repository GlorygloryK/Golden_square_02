from lib.make_snippet import make_snippet
"""
Scenario 1: Entering a string with < 5 words
"""
def test_return_string_with_less_than_5_words():
    result = make_snippet("Love!")
    assert result == "Love!"

"""
Scenario 2: Entering an empty string
will return '' (empty string)
"""
def test_return_empty_string_when_theres_no_input():
    result = make_snippet("")
    assert result == ""

"""
Scenario 3: Entering a string with > 5 words 
will return the string PLUS '...'
"""
def test_return_string_with_more_than_5_words():
    result = make_snippet("Love this!")
    assert result == "Love ..."

