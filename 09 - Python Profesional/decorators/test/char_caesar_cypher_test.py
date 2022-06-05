import pytest
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

if SCRIPT_DIR:
    from src.cyphers.caesar.caesar import get_char_caesar_cypher
    from src.cyphers.caesar.errors.NonPositiveRotationError import NonPositiveRotationError


class TestCharCaesarCypher:

    def test_c_with_rotation_5_should_return_h(self):
        assert get_char_caesar_cypher('c', 5) == 'h'

    def test_t_with_rotation_6_should_return_z(self):
        assert get_char_caesar_cypher('t', 6) == 'z'

    def test_v_with_rotation_5_should_return_a(self):
        assert get_char_caesar_cypher('v', 5) == 'a'

    def test_rotation_0_should_raise_NonPositiveRotationError(self):
        with pytest.raises(NonPositiveRotationError):
            get_char_caesar_cypher('e', 0)

    def test_rotation_negative_3_should_raise_NonPositiveRotationError(self):
        with pytest.raises(NonPositiveRotationError):
            get_char_caesar_cypher('e', -3)

    def test_x_with_rotation_26_should_return_x(self):
        assert get_char_caesar_cypher('x', 26) == 'x'

    def test_G_with_rotation_7_should_return_N(self):
        assert get_char_caesar_cypher('G', 7) == 'N'

    def test_semicolon_should_return_semicolon(self):
        assert get_char_caesar_cypher(';', 4) == ';'
