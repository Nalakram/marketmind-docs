srcPy.pipeline.stages.market_data.sources.coingecko
===================================================

.. py:module:: srcPy.pipeline.stages.market_data.sources.coingecko


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.sources.coingecko.CoinGeckoSource


Module Contents
---------------

.. py:class:: CoinGeckoSource(config)

   Bases: :py:obj:`APIDataSource`


   coin gecko source class.


   .. py:attribute:: base_url
      :type:  str
      :value: Ellipsis



   .. py:attribute:: vs_currency
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: coin_map
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: rate_limit
      :type:  Any
      :value: Ellipsis



   .. py:method:: get_historical(symbol, start, end, *, eager = False)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = None)
      :async:



