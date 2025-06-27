srcPy.data.ib_data_collection
=============================

.. py:module:: srcPy.data.ib_data_collection


Attributes
----------

.. autoapisummary::

   srcPy.data.ib_data_collection.logger


Exceptions
----------

.. autoapisummary::

   srcPy.data.ib_data_collection.NoDataError


Functions
---------

.. autoapisummary::

   srcPy.data.ib_data_collection.create_mock_bars
   srcPy.data.ib_data_collection.fetch_historical_data
   srcPy.data.ib_data_collection.fetch_multiple_historical_data


Module Contents
---------------

.. py:data:: logger
   :type:  _typeshed.Incomplete

.. py:exception:: NoDataError(symbol)

   Bases: :py:obj:`srcPy.utils.exceptions.DataFetchError`


   Raised when a data provider returns an error or invalid payload.

   This is the generic parent for all data‑acquisition failures. Sub‑classes
   may specialise the scenario further (e.g. :class:`NoDataError`).

   :param message: Human‑readable summary. Defaults to ``"Error fetching data"``.
   :type message: str, optional
   :param details: Context such as the provider name, HTTP status code or retry count.
   :type details: dict | None, optional

   .. attribute:: details

      Structured diagnostic information.

      :type: dict


.. py:function:: create_mock_bars(n, start_date = '2025-01-01')

.. py:function:: fetch_historical_data(symbol, end_date = '', duration = '1 Y', bar_size = '1 day', ib_client = None, use_cache = True, what_to_show = 'TRADES', use_rth = True, format_date = 1)

.. py:function:: fetch_multiple_historical_data(symbols, end_date = '', duration = '1 Y', bar_size = '1 day', use_cache = True, what_to_show = 'TRADES', use_rth = True, format_date = 1)
   :async:


