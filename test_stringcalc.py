"""String Calculator Kata Tests"""

import stringcalc


def test_add_no_arg():
    assert stringcalc.add() == 0


def test_add_empty_string():
    assert stringcalc.add("") == 0


def test_add_zero():
    assert stringcalc.add("0") == 0


def test_add_one_int():
    assert stringcalc.add("4") == 4


def test_add_two_ints():
    assert stringcalc.add("1,2") == 3


def test_add_many_ints():
    assert stringcalc.add("1,2,3,4,5,6,7,8,9") == 45


def test_add_with_newline_sep():
    assert stringcalc.add("1\n10,3") == 14
