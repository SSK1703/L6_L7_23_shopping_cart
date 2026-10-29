
import pytest
from shopping_cart import item_total, cart_discount, shipping_fee


def test_all_categories():
    assert item_total("food", 100, 1) == 105
    assert item_total("electronics", 100, 1) == 118
    assert item_total("clothing", 100, 1) == 112


def test_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        item_total("toys", 100, 1)


def test_negative_price():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", -1, 1)


def test_invalid_quantity():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", 100, 0)


def test_quantity_boundary():
    assert item_total("food", 100, 9) == 945
    assert item_total("food", 100, 10) == 945


def test_cart_value_branches():
    assert cart_discount(1999, False, "NONE") == 0
    assert cart_discount(2000, False, "NONE") == 200
    assert cart_discount(4999, False, "NONE") == 200
    assert cart_discount(5000, False, "NONE") == 500


def test_prime_branch():
    assert cart_discount(500, True, "NONE") == 100
    assert cart_discount(500, False, "NONE") == 0


def test_coupon_branches():
    assert cart_discount(1000, False, "FLAT10") == 100
    assert cart_discount(999, False, "FLAT10") == 0
    assert cart_discount(1000, False, "NONE") == 0


def test_shipping_fee_branches():
    assert shipping_fee(100, True, False) == 0
    assert shipping_fee(100, False, False) == 40
    assert shipping_fee(500, False, False) == 0


def test_express_shipping_branches():
    assert shipping_fee(100, True, True) == 50
    assert shipping_fee(100, False, True) == 140
    assert shipping_fee(500, False, True) == 100
