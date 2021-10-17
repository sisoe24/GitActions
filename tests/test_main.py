from src.main import uppername


def test_main():
    name = uppername('virgil')
    assert name.isupper()

def test_main_str():
    name = uppername('virgil')
    assert name == 'VIRGIL'
