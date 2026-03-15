srcPy.domain.interfaces
=======================

.. py:module:: srcPy.domain.interfaces


Attributes
----------

.. autoapisummary::

   srcPy.domain.interfaces.PositionSchema
   srcPy.domain.interfaces.HistoricalSchema
   srcPy.domain.interfaces.T_co


Classes
-------

.. autoapisummary::

   srcPy.domain.interfaces.Order
   srcPy.domain.interfaces.Position
   srcPy.domain.interfaces.OrderExecutor
   srcPy.domain.interfaces.PositionService
   srcPy.domain.interfaces.MarketDataProvider
   srcPy.domain.interfaces.AsyncMarketDataProvider
   srcPy.domain.interfaces.EconomicDataProvider
   srcPy.domain.interfaces.ProviderFactory
   srcPy.domain.interfaces.RiskManager
   srcPy.domain.interfaces.PositionSizer


Module Contents
---------------

.. py:class:: Order

   order class.


   .. py:attribute:: order_id
      :type:  int
      :value: Ellipsis



   .. py:attribute:: action
      :type:  str
      :value: Ellipsis



   .. py:attribute:: total_quantity
      :type:  float
      :value: Ellipsis



   .. py:attribute:: order_type
      :type:  str
      :value: Ellipsis



   .. py:attribute:: lmt_price
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: aux_price
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: tif
      :type:  str
      :value: Ellipsis



   .. py:attribute:: account
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: symbol
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: solicited
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: extra
      :type:  dict[str, Any]


   .. py:method:: market(symbol, qty)
      :classmethod:



.. py:class:: Position

   position class.


   .. py:attribute:: account
      :type:  str
      :value: Ellipsis



   .. py:attribute:: symbol
      :type:  str
      :value: Ellipsis



   .. py:attribute:: position
      :type:  float
      :value: Ellipsis



   .. py:attribute:: avg_cost
      :type:  float
      :value: Ellipsis



   .. py:attribute:: model_code
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: extra
      :type:  dict[str, Any]


.. py:data:: PositionSchema
   :type:  polars._typing.SchemaDict
   :value: Ellipsis


.. py:data:: HistoricalSchema
   :type:  polars._typing.SchemaDict
   :value: Ellipsis


.. py:class:: OrderExecutor

   Bases: :py:obj:`Protocol`


   order executor class.


   .. py:method:: submit(order)


   .. py:method:: submit_batch(orders)


   .. py:method:: cancel(order_id)


   .. py:method:: status(order_id)


.. py:class:: PositionService

   Bases: :py:obj:`Protocol`


   position service implementation.


   .. py:method:: get_positions()


   .. py:method:: get_positions_as_polars()


.. py:class:: MarketDataProvider

   Bases: :py:obj:`Protocol`


   market data provider class.


   .. py:method:: get_price(symbol)


   .. py:method:: get_prices(symbols)


   .. py:method:: get_historical(symbol, start, end, interval = '1min', lazy = True)


   .. py:method:: get_historical_batch(symbols, start, end, interval = '1min', lazy = True)


   .. py:method:: map_over(symbols, fn, combine = ...)


   .. py:method:: stream_realtime(symbol, interval = 60.0)
      :async:



.. py:class:: AsyncMarketDataProvider

   Bases: :py:obj:`MarketDataProvider`, :py:obj:`Protocol`


   async market data provider class.


   .. py:method:: get_price_async(symbol)
      :async:



   .. py:method:: get_prices_async(symbols)
      :async:



.. py:class:: EconomicDataProvider

   Bases: :py:obj:`Protocol`


   economic data provider class.


   .. py:method:: get_indicator(indicator, start, end)


.. py:data:: T_co

.. py:class:: ProviderFactory

   Bases: :py:obj:`abc.ABC`, :py:obj:`Generic`\ [\ :py:obj:`T_co`\ ]


   Factory for creating provider instances.


   .. py:method:: register(provider_type)
      :classmethod:



   .. py:method:: load_entry_points(group = 'marketmind.providers')
      :classmethod:



   .. py:method:: create(provider_type, config, **kwargs)
      :classmethod:



   .. py:method:: build_provider(config, **kwargs)
      :abstractmethod:



.. py:class:: RiskManager

   Manages risk resources and operations.


   .. py:method:: validate(order)


.. py:class:: PositionSizer

   position sizer class.


   .. py:method:: size(symbol, signal, price)


