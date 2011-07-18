# -*- coding: utf-8 -*-
from django import template
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist

from product.models import Product
from product.modules.configurable.models import ProductVariation, ConfigurableProduct
from satchmo_ext.brand.models import Brand,BrandProduct

try:
    from xml.etree.ElementTree import Element, SubElement, tostring
except ImportError:
    from elementtree.ElementTree import Element, SubElement, tostring

register = template.Library()

@register.filter(name='brand')
def brand(value):
    u"""
    Возвращает объект бренда по продукту
    """
    result = None
    b = BrandProduct.objects.filter(product=value).all()
    if b:
        result = b.all()[0].brand
    return result

@register.filter(name='in_stock')
def in_stock(product):
    u"""
    Возвращает наличие остатка самого продукта и его вариантов
    """
    in_stock = product.in_stock()
    try:
        configurable = ConfigurableProduct.objects.get(product=product)
        # есть подварианты продукта
        for variation in ProductVariation.objects.select_related().filter(
                parent=configurable).all():
            if variation.product.in_stock():
                in_stock = True
                break
    except ObjectDoesNotExist:
        pass
    return in_stock

