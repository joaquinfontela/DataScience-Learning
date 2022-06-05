import pytest
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

if SCRIPT_DIR:
    from src.cyphers.caesar.caesar import caesar_cypher
    from src.cyphers.caesar.errors.NonPositiveRotationError import NonPositiveRotationError


class TestCaesarCypher:

    def test_negative_rotation_should_raise_NonPositiveRotationError(self):
        with pytest.raises(NonPositiveRotationError):
            caesar_cypher('test string', -3)

    def test_zero_rotation_should_raise_NonPositiveRotationError(self):
        with pytest.raises(NonPositiveRotationError):
            caesar_cypher('test string', 0)

    def test_26_rotation_should_return_same_string(self):
        assert caesar_cypher('test string', 26) == 'test string'

    def test_rotation_8(self):
        assert caesar_cypher('test string', 8) == 'bmab abzqvo'

    def test_rotation_8_with_uppercase_and_non_ascii_chars(self):
        assert caesar_cypher('tEstinG; sTRIng', 8) == 'bMabqvO; aBZQvo'
