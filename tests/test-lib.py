from bbquote.lib import get_quote


def test_quote():
    quote = get_quote()
    assert len(quote) != 0
