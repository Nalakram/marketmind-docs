srcPy.pipeline.stages.market_data.sources.quandl
================================================

.. py:module:: srcPy.pipeline.stages.market_data.sources.quandl


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.sources.quandl.QuandlSource


Module Contents
---------------

.. py:class:: QuandlSource(config)

   Bases: :py:obj:`srcPy.pipeline.stages.market_data.sources.base.DataSource`


   quandl source class.


   .. py:attribute:: api_key
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: base_url
      :type:  str
      :value: Ellipsis



   .. py:method:: get_historical(symbol, start, end, *, eager = False)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = 300.0)
      :async:



