from src.main import uppername


def test_main():
    name = uppername('virgil')
    assert name.isupper()
