srcPy.pipeline.stages.market_data.sources.fred
==============================================

.. py:module:: srcPy.pipeline.stages.market_data.sources.fred


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.sources.fred.FREDSource


Module Contents
---------------

.. py:class:: FREDSource(config)

   Bases: :py:obj:`srcPy.pipeline.stages.market_data.sources.base.DataSource`


   fred source class.


   .. py:attribute:: fred
      :type:  Any
      :value: Ellipsis



   .. py:method:: get_historical(symbol, start, end, *, eager = False)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = 3600.0)
      :async:



