from src.main import uppername


def test_main():
    name = uppername('virgil')
    assert name.isupper()


def test_main_upper():
    name = uppername('virgil')
    assert name == 'VIRGIL'


def test_main_str():
    name = uppername('virgil')
    assert isinstance(name, str)
