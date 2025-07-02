from roastme import get_roast

def test_output():
    assert isinstance(get_roast("harsh"), str)
