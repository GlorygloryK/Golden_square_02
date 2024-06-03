from lib.check_codeword import *

"""
When the codeword is right (ie. is correct), this is the response 
"""
def test_the_correct_codeword():
    codeword = check_codeword("horse") 
    assert result == "Correct! Come in."
    

"""
When the codeword's first and last letters are the only ones matching (i.e. it's nearly there but not quite)
"""
def test_the_codeword_that_was_nearly_there():
    codeword = check_codeword("hose") 
    assert result == "Close, but nope."

"""
When the codeword's FIRST letter matches ONLY 
"""
def test_the_codeword_with_correct_first_letter():
    codeword = check_codeword("hopping") 
    assert result == "WRONG!"

"""

When the codeword's LAST letter matches ONLY 
"""
def test_the_codeword_with_correct_last_letter():
    codeword = check_codeword("ease") 
    assert result == "WRONG!"

"""
When the codeword is wrong
"""
def test_the_wrong_codeword():
    codeword = check_codeword("bike") 
    assert result == "WRONG!" 

