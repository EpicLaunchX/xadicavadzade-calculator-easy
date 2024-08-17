import pytest

from src.pytemplate.domain.models import Operands


def test_operands_initialization():
    operands = Operands(first_operand=10, second_operand=20)
    assert operands.first_operand == 10
    assert operands.second_operand == 20


def test_operands_negative_values():
    operands = Operands(first_operand=-5, second_operand=-10)
    assert operands.first_operand == -5
    assert operands.second_operand == -10


def test_operands_zero_values():
    operands = Operands(first_operand=0, second_operand=0)
    assert operands.first_operand == 0
    assert operands.second_operand == 0
