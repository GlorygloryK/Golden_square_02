from lib.fizzbuzz import * 

"""
If number's not divisible by 3 or 5, 
you just input the number
"""
def test_num_not_div_by_three_or_five():
    result = fizzbuzz(8)
    assert result == 8


"""
If number's divisible by 3 only and NOT 5
chuck out the string 'Fizz'
"""
def test_num_div_by_three_only():
    result = fizzbuzz(9)
    assert result == 'Fizz'


"""
If number's divisible by 5 only and NOT 3
chuck out the string 'Buzz'
"""

def test_num_div_by_five_only():
    result = fizzbuzz(10)
    assert result == 'Buzz'

"""
If number's divisible by BOTH 3 and 5
chuck out the string 'Fizzbuzz'
"""

def test_num_div_by_three_and_five_giving_fizzbuzz():
    result = fizzbuzz(15)
    assert result == 'Fizzbuzz'
