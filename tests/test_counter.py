from lib.counter import *
"""
When no number is added, the count is still zero
"""
def _test_correct_answer():
    counter = Counter()
    counter.report()
    assert counter.report() == "Counted to 0 so far."
"""
When the number 7 is added 
"""
def _test_correct_answer():
    counter = Counter()
    counter.add(7)
    counter.report()
    assert counter.report() == "Counted to 7 so far."

    """
When the number 7 and another number 2 is added 
"""
def _test_correct_answer():
    counter = Counter()
    counter.add(7)
    counter.add(3)
    counter.report()
    assert counter.report() == "Counted to 10 so far."