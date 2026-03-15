srcPy.pipeline.stages.market_data.sources.ibkr
==============================================

.. py:module:: srcPy.pipeline.stages.market_data.sources.ibkr


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.sources.ibkr.IBKRSource


Module Contents
---------------

.. py:class:: IBKRSource(config)

   Bases: :py:obj:`DataSource`


   ibkr source class.


   .. py:attribute:: host
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: port
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: client_id
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: default_bar_size
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: what_to_show
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: use_rth
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: ib
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: queue_maxsize
      :type:  Any
      :value: Ellipsis



   .. py:method:: __aenter__()
      :async:



   .. py:method:: __aexit__(exc_type, exc_val, exc_tb)
      :async:



   .. py:method:: get_historical(symbol, start, end, *, eager = False)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = 5.0)
      :async:



