srcPy.pipeline.stages.market_data.sources.base
==============================================

.. py:module:: srcPy.pipeline.stages.market_data.sources.base


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.sources.base.DataSource
   srcPy.pipeline.stages.market_data.sources.base.APIDataSource


Module Contents
---------------

.. py:class:: DataSource(config)

   Bases: :py:obj:`abc.ABC`


   data source class.


   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:method:: get_historical(symbol, start, end, *, eager = False)
      :abstractmethod:

      :async:



   .. py:method:: get_realtime(symbol, *, interval = 60.0)
      :abstractmethod:

      :async:



   .. py:method:: __aenter__()
      :async:



   .. py:method:: __aexit__(exc_type, exc_val, exc_tb)
      :async:



   .. py:method:: close()
      :async:



.. py:class:: APIDataSource(config)

   Bases: :py:obj:`DataSource`


   api data source class.


   .. py:attribute:: session
      :type:  Any
      :value: Ellipsis



   .. py:method:: __aexit__(exc_type, exc_val, exc_tb)
      :async:



   .. py:method:: close()
      :async:



