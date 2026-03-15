srcPy.infra.brokers.ibkr.historical
===================================

.. py:module:: srcPy.infra.brokers.ibkr.historical


Attributes
----------

.. autoapisummary::

   srcPy.infra.brokers.ibkr.historical.logger


Classes
-------

.. autoapisummary::

   srcPy.infra.brokers.ibkr.historical.IBKR
   srcPy.infra.brokers.ibkr.historical.BarData
   srcPy.infra.brokers.ibkr.historical.Stock
   srcPy.infra.brokers.ibkr.historical.util
   srcPy.infra.brokers.ibkr.historical.NoDataError


Functions
---------

.. autoapisummary::

   srcPy.infra.brokers.ibkr.historical.create_mock_bars
   srcPy.infra.brokers.ibkr.historical.fetch_historical_data
   srcPy.infra.brokers.ibkr.historical.fetch_multiple_historical_data


Module Contents
---------------

.. py:class:: IBKR(*args, **kwargs)

   ibkr class.


   .. py:method:: connect(*args, **kwargs)


   .. py:method:: reqHistoricalData(*args, **kwargs)


   .. py:method:: disconnect()


.. py:class:: BarData(*args, **kwargs)

   bar data class.


.. py:class:: Stock(*args, **kwargs)

   stock class.


.. py:class:: util

   util class.


   .. py:method:: df(*args, **kwargs)
      :staticmethod:



.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: NoDataError(symbol)

   Bases: :py:obj:`srcPy.utils.exceptions.DataFetchError`


   Exception raised when no data occurs.


.. py:function:: create_mock_bars(n, start_date = '2025-01-01')

.. py:function:: fetch_historical_data(symbol, end_date = '', duration = '1 Y', bar_size = '1 day', ibkr_client = None, use_cache = True, what_to_show = 'TRADES', use_rth = True, format_date = 1)

.. py:function:: fetch_multiple_historical_data(symbols, end_date = '', duration = '1 Y', bar_size = '1 day', use_cache = True, what_to_show = 'TRADES', use_rth = True, format_date = 1)
   :async:


