# -*- coding: utf-8 -*-
u"""Административный интерфейс"""

from django.contrib import admin
from satchmo_yandex_market.models import YandexMarketSite

admin.site.register(YandexMarketSite)
