Модуль Яндекс.Маркет для Satchmo
================================

Зависимости
-----------

- sorl-thumbnail_

.. _sorl-thumbnail: https://github.com/sorl/sorl-thumbnail

Установка
---------

Стандартная команда::

        python setup.py install

В ``INSTALLED_APPS`` в настройках прописываем::

        INSTALLED_APPS = (
                ...,
                'satchmo_yandex_market',
        )

В ``SATCHMO_SETTINGS`` в ``settings.py`` добавить что-то вроде::

        SATCHMO_SETTINGS = {
                ...,
                'SHOP_URLS' : patterns('',
                        (r'offers\.xml', 'satchmo_yandex_market.views.offers', {}),
                ),
        }
