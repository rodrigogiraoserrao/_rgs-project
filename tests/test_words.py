import pytest

from rgs_project import as_words


@pytest.mark.parametrize(
    ["string", "words"],
    [
        ("Hello, world!", ["hello", "world"]),
        ("hello", ["hello"]),
        ("!!HELLO..?", ["hello"]),
    ],
)
def test_as_words(string, words):
    assert as_words(string) == words
