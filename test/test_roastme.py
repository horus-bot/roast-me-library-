from roastme import get_roast

def test_get_roast_returns_string():
    assert isinstance(get_roast(), str)
    assert len(get_roast()) > 0
