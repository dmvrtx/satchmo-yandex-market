# -*- coding: utf-8 -*-
u"""Модели настроек Яндекс.Маркета"""

from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _

class YandexMarketSite(models.Model):
    u"""
    Настройки сайта для вывода товаров в Яндекс.Маркет
    """
    site = models.ForeignKey(Site, verbose_name=_('Site'), unique=True)
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    company = models.CharField(max_length=200, verbose_name=_('Company'))
    url = models.URLField(verbose_name=_('URL'))
    email = models.EmailField(verbose_name=_('Email'), blank=True)
    notes = models.CharField(max_length=1024, verbose_name=_('Notes'), blank=True)

    class Meta:
        verbose_name = _('Yandex.Market site')
        verbose_name_plural = _('Yandex.Market sites')
