from hello import say_hello, say_goodbye


def test_say_hello():
    assert "hi" == say_hello()


def test_say_hello2():
    assert "bye" == say_goodbye()
