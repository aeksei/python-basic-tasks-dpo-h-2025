from task_1_8 import get_product_counter


def test_get_product_counter():
    """"""
    products = ["яблоко"]

    actual = get_product_counter(products)
    expected = {"яблоко": 1}
    assert actual == expected
