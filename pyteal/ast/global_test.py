import pytest

from .. import *
# this is not necessary but mypy complains if it's not included
from .. import CompileOptions

teal2Options = CompileOptions(version=2)
teal3Options = CompileOptions(version=3)

def test_global_min_txn_fee():
    expr = Global.min_txn_fee()
    assert expr.type_of() == TealType.uint64

    expected = TealSimpleBlock([
        TealOp(expr, Op.global_, "MinTxnFee")
    ])

    actual, _ = expr.__teal__(teal2Options)

    assert actual == expected

def test_global_min_balance():
    expr = Global.min_balance()
    assert expr.type_of() == TealType.uint64

    expected = TealSimpleBlock([
        TealOp(expr, Op.global_, "MinBalance")
    ])

    actual, _ = expr.__teal__(teal2Options)

    assert actual == expected

def test_global_max_txn_life():
    expr = Global.max_txn_life()
    assert expr.type_of() == TealType.uint64

    expected = TealSimpleBlock([
        TealOp(expr, Op.global_, "MaxTxnLife")
    ])

    actual, _ = expr.__teal__(teal2Options)

    assert actual == expected

def test_global_zero_address():
    expr = Global.zero_address()
    assert expr.type_of() == TealType.bytes

    expected = TealSimpleBlock([
        TealOp(expr, Op.global_, "ZeroAddress")
    ])

    actual, _ = expr.__teal__(teal2Options)

    assert actual == expected

def test_global_group_size():
    expr = Global.group_size()
    assert expr.type_of() == TealType.uint64

    expected = TealSimpleBlock([
        TealOp(expr, Op.global_, "GroupSize")
    ])

    actual, _ = expr.__teal__(teal2Options)

    assert actual == expected

def test_global_logic_sig_version():
    expr = Global.logic_sig_version()
    assert expr.type_of() == TealType.uint64

    expected = TealSimpleBlock([
        TealOp(expr, Op.global_, "LogicSigVersion")
    ])

    actual, _ = expr.__teal__(teal2Options)

    assert actual == expected

def test_global_round():
    expr = Global.round()
    assert expr.type_of() == TealType.uint64

    expected = TealSimpleBlock([
        TealOp(expr, Op.global_, "Round")
    ])

    actual, _ = expr.__teal__(teal2Options)

    assert actual == expected

def test_global_latest_timestamp():
    expr = Global.latest_timestamp()
    assert expr.type_of() == TealType.uint64

    expected = TealSimpleBlock([
        TealOp(expr, Op.global_, "LatestTimestamp")
    ])

    actual, _ = expr.__teal__(teal2Options)

    assert actual == expected

def test_global_current_application_id():
    expr = Global.current_application_id()
    assert expr.type_of() == TealType.uint64

    expected = TealSimpleBlock([
        TealOp(expr, Op.global_, "CurrentApplicationID")
    ])

    actual, _ = expr.__teal__(teal2Options)
    
    assert actual == expected

def test_global_creator_address():
    expr = Global.creator_address()
    assert expr.type_of() == TealType.bytes

    expected = TealSimpleBlock([
        TealOp(expr, Op.global_, "CreatorAddress")
    ])

    actual, _ = expr.__teal__(teal3Options)
    
    assert actual == expected

    with pytest.raises(TealInputError):
        expr.__teal__(teal2Options)
