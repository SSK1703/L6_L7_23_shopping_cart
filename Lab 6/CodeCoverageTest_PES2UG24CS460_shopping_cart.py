
import pytest
from shopping_cart import item_total, cart_discount, shipping_fee


# Tests for item_total()

def test_food_item():
    assert item_total("food", 100, 2) == 210


def test_electronics_item():
    assert item_total("electronics", 100, 1) == 118


def test_clothing_item():
    assert item_total("clothing", 100, 1) == 112


def test_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        item_total("toys", 100, 1)


def test_negative_price():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", -10, 1)


def test_zero_quantity():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", 100, 0)


def test_bulk_quantity_discount():
    assert item_total("food", 100, 10) == 945


# Tests for cart_discount()

def test_high_value_prime_coupon():
    assert cart_discount(6000, True, "FLAT10") == 1200


def test_medium_value_cart():
    assert cart_discount(3000, False, "NONE") == 200


def test_low_value_cart():
    assert cart_discount(500, False, "NONE") == 0


def test_coupon_at_minimum_value():
    assert cart_discount(1000, False, "FLAT10") == 100


def test_prime_discount():
    assert cart_discount(500, True, "NONE") == 100


# Tests for shipping_fee()

def test_prime_standard_shipping():
    assert shipping_fee(100, True, False) == 0


def test_prime_express_shipping():
    assert shipping_fee(100, True, True) == 50


def test_non_prime_free_shipping():
    assert shipping_fee(500, False, False) == 0


def test_non_prime_express_shipping():
    assert shipping_fee(500, False, True) == 100


def test_paid_shipping():
    assert shipping_fee(100, False, False) == 40


def test_paid_express_shipping():
    assert shipping_fee(100, False, True) == 140
