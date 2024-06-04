from lib.present import *

def test_wrap_content():
    present = Present()
    present.wrap("toy")
    assert present.unwrap == "toy"