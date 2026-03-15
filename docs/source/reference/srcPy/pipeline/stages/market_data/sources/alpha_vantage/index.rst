srcPy.pipeline.stages.market_data.sources.alpha_vantage
=======================================================

.. py:module:: srcPy.pipeline.stages.market_data.sources.alpha_vantage


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.sources.alpha_vantage.AlphaVantageSource


Module Contents
---------------

.. py:class:: AlphaVantageSource(config)

   Bases: :py:obj:`APIDataSource`


   alpha vantage source class.


   .. py:attribute:: api_key
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: base_url
      :type:  str
      :value: Ellipsis



   .. py:attribute:: rate_limit
      :type:  Any
      :value: Ellipsis



   .. py:method:: get_historical(symbol, start, end, *, eager = False)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = None)
      :async:



