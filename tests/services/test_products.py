"""
1. Test product count zero, product count with products
2. Test product returns all/pagination
3. Test product filters (title, description, no match)
"""

import pytest
from tests.factories.products import ProductModelFactory

from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.products.services.products import BaseProductService


@pytest.mark.django_db
def test_get_products_count_zero(product_service: BaseProductService):
    """Test product count zero with no products in database."""
    product_count = product_service.get_product_count(ProductFilters())
    assert product_count == 0, f'{product_count=}'


@pytest.mark.django_db
def test_get_products_count_exist(product_service: BaseProductService):
    """Test product count zero with no products in database."""
    expected_count = 5
    ProductModelFactory.create_batch(size=expected_count)
    product_count = product_service.get_product_count(ProductFilters())
    assert product_count == expected_count, f'{product_count=}'


@pytest.mark.django_db
def test_get_product_all(product_service: BaseProductService):
    expected_count = 5
    products = ProductModelFactory.create_batch(size=expected_count)
    products_title = {product.title for product in products}

    fetched_products = product_service.get_product_list(ProductFilters(), PaginationIn())
    fetched_products_title = {product.title for product in fetched_products}

    assert len(fetched_products_title) == expected_count, f"{fetched_products_title=}"
    # as expected_count < paginathin_linit use '==', else 'in'
    assert products_title == fetched_products_title, f"{fetched_products_title=}"
