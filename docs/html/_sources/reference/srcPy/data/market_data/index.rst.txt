srcPy.data.market_data
======================

.. py:module:: srcPy.data.market_data


Attributes
----------

.. autoapisummary::

   srcPy.data.market_data.logger
   srcPy.data.market_data.FETCH_FAILURES
   srcPy.data.market_data.FETCH_SUCCESSES
   srcPy.data.market_data.FETCH_DURATION
   srcPy.data.market_data.HAVE_CUDF


Classes
-------

.. autoapisummary::

   srcPy.data.market_data.DataSource
   srcPy.data.market_data.AlphaVantageSource
   srcPy.data.market_data.CoinGeckoSource
   srcPy.data.market_data.FileSource
   srcPy.data.market_data.MarketDataManager


Functions
---------

.. autoapisummary::

   srcPy.data.market_data.validate_dataframe
   srcPy.data.market_data.normalize
   srcPy.data.market_data.add_moving_average
   srcPy.data.market_data.add_rsi
   srcPy.data.market_data.cached_historical


Module Contents
---------------

.. py:data:: logger
   :type:  _typeshed.Incomplete

.. py:data:: FETCH_FAILURES
   :type:  _typeshed.Incomplete

.. py:data:: FETCH_SUCCESSES
   :type:  _typeshed.Incomplete

.. py:data:: FETCH_DURATION
   :type:  _typeshed.Incomplete

.. py:class:: DataSource

   Bases: :py:obj:`abc.ABC`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: get_historical(symbol, start, end)
      :abstractmethod:



   .. py:method:: get_realtime(symbol)
      :abstractmethod:

      :async:



.. py:class:: AlphaVantageSource(config)

   Bases: :py:obj:`DataSource`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: api_key
      :type:  _typeshed.Incomplete


   .. py:attribute:: base_url
      :type:  str


   .. py:method:: get_historical(symbol, start, end)


   .. py:method:: get_realtime(symbol)
      :async:



.. py:class:: CoinGeckoSource

   Bases: :py:obj:`DataSource`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: cg
      :type:  _typeshed.Incomplete


   .. py:attribute:: coin_map
      :type:  _typeshed.Incomplete


   .. py:method:: get_historical(symbol, start, end)


   .. py:method:: get_realtime(symbol)
      :async:



.. py:class:: FileSource(file_path)

   Bases: :py:obj:`DataSource`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: file_path
      :type:  _typeshed.Incomplete


   .. py:attribute:: ext
      :type:  _typeshed.Incomplete


   .. py:method:: get_historical(symbol, start, end)


   .. py:method:: get_realtime(symbol)
      :async:



.. py:function:: validate_dataframe(df, required_columns = None)

.. py:function:: normalize(df, columns)

.. py:function:: add_moving_average(df, window = 14, price_col = 'Close')

.. py:function:: add_rsi(df, window = 14, price_col = 'Close')

.. py:class:: MarketDataManager(config)

   .. py:attribute:: config
      :type:  _typeshed.Incomplete


   .. py:attribute:: sources
      :type:  _typeshed.Incomplete


   .. py:method:: add_source(source)


   .. py:method:: get_historical(symbol, start, end, source_name = None)


   .. py:method:: get_realtime(symbol, source_name = None)
      :async:



   .. py:method:: get_historical_batch(symbols, start, end, source_name = None)
      :async:



   .. py:method:: stream_realtime(symbol, source_name = None, interval = 60)
      :async:



.. py:function:: cached_historical(manager, symbol, start, end, source_name = None)

.. py:data:: HAVE_CUDF
   :type:  bool

