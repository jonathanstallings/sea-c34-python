import pytest
import break_me as br


def test_name_break():
    with pytest.raises(NameError):
        br.name_break()


def test_type_break():
    with pytest.raises(TypeError):
        br.type_break()


def test_syntax_break():
    with pytest.raises(SyntaxError):
        br.syntax_break()


def test_attribute_break():
    with pytest.raises(AttributeError):
        br.attribute_break()

