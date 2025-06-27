srcPy.strategies.baseStrategies
===============================

.. py:module:: srcPy.strategies.baseStrategies


Classes
-------

.. autoapisummary::

   srcPy.strategies.baseStrategies.BaseStrategy
   srcPy.strategies.baseStrategies.LogisticRegressionStrategy
   srcPy.strategies.baseStrategies.RandomForestStrategy
   srcPy.strategies.baseStrategies.ARIMAStrategy
   srcPy.strategies.baseStrategies.GARCHStrategy
   srcPy.strategies.baseStrategies.MovingAverageCrossover
   srcPy.strategies.baseStrategies.RSIStrategy
   srcPy.strategies.baseStrategies.MACDStrategy
   srcPy.strategies.baseStrategies.BollingerBandsStrategy
   srcPy.strategies.baseStrategies.MomentumStrategy
   srcPy.strategies.baseStrategies.MeanReversionStrategy


Module Contents
---------------

.. py:class:: BaseStrategy

   Bases: :py:obj:`backtrader.Strategy`


   Base class to be subclassed for user defined strategies.


   .. py:attribute:: params
      :type:  _typeshed.Incomplete


   .. py:attribute:: order
      :type:  _typeshed.Incomplete


   .. py:attribute:: logger
      :type:  _typeshed.Incomplete


   .. py:method:: get_signal()


   .. py:method:: next()

      This method will be called for all remaining data points when the
      minimum period for all datas/indicators have been meet.



   .. py:method:: calculate_stop_price(is_long)


   .. py:method:: calculate_tp_price(is_long)


   .. py:method:: notify_order(order)

      Receives an order whenever there has been a change in one



.. py:class:: LogisticRegressionStrategy

   Bases: :py:obj:`BaseStrategy`


   Base class to be subclassed for user defined strategies.


   .. py:attribute:: params
      :type:  _typeshed.Incomplete


   .. py:attribute:: model
      :type:  _typeshed.Incomplete


   .. py:attribute:: scaler
      :type:  _typeshed.Incomplete


   .. py:attribute:: df
      :type:  _typeshed.Incomplete


   .. py:attribute:: features
      :type:  _typeshed.Incomplete


   .. py:attribute:: targets
      :type:  _typeshed.Incomplete


   .. py:method:: prenext()

      This method will be called before the minimum period of all
      datas/indicators have been meet for the strategy to start executing



   .. py:method:: next()

      This method will be called for all remaining data points when the
      minimum period for all datas/indicators have been meet.



   .. py:method:: collect_data()


   .. py:method:: get_current_features()


   .. py:method:: get_signal()


.. py:class:: RandomForestStrategy

   Bases: :py:obj:`BaseStrategy`


   Base class to be subclassed for user defined strategies.


   .. py:attribute:: params
      :type:  _typeshed.Incomplete


   .. py:attribute:: model
      :type:  _typeshed.Incomplete


   .. py:attribute:: scaler
      :type:  _typeshed.Incomplete


   .. py:attribute:: df
      :type:  _typeshed.Incomplete


   .. py:attribute:: features
      :type:  _typeshed.Incomplete


   .. py:attribute:: targets
      :type:  _typeshed.Incomplete


   .. py:method:: prenext()

      This method will be called before the minimum period of all
      datas/indicators have been meet for the strategy to start executing



   .. py:method:: next()

      This method will be called for all remaining data points when the
      minimum period for all datas/indicators have been meet.



   .. py:method:: collect_data()


   .. py:method:: get_current_features()


   .. py:method:: get_signal()


.. py:class:: ARIMAStrategy

   Bases: :py:obj:`BaseStrategy`


   Base class to be subclassed for user defined strategies.


   .. py:attribute:: params
      :type:  _typeshed.Incomplete


   .. py:attribute:: history
      :type:  _typeshed.Incomplete


   .. py:attribute:: model
      :type:  _typeshed.Incomplete


   .. py:method:: prenext()

      This method will be called before the minimum period of all
      datas/indicators have been meet for the strategy to start executing



   .. py:method:: next()

      This method will be called for all remaining data points when the
      minimum period for all datas/indicators have been meet.



   .. py:method:: get_signal()


.. py:class:: GARCHStrategy

   Bases: :py:obj:`BaseStrategy`


   Base class to be subclassed for user defined strategies.


   .. py:attribute:: params
      :type:  _typeshed.Incomplete


   .. py:attribute:: returns
      :type:  _typeshed.Incomplete


   .. py:attribute:: model
      :type:  _typeshed.Incomplete


   .. py:method:: prenext()

      This method will be called before the minimum period of all
      datas/indicators have been meet for the strategy to start executing



   .. py:method:: next()

      This method will be called for all remaining data points when the
      minimum period for all datas/indicators have been meet.



   .. py:method:: get_signal()


.. py:class:: MovingAverageCrossover

   Bases: :py:obj:`BaseStrategy`


   Base class to be subclassed for user defined strategies.


   .. py:attribute:: params
      :type:  _typeshed.Incomplete


   .. py:attribute:: sma_short
      :type:  _typeshed.Incomplete


   .. py:attribute:: sma_long
      :type:  _typeshed.Incomplete


   .. py:method:: get_signal()


.. py:class:: RSIStrategy

   Bases: :py:obj:`BaseStrategy`


   Base class to be subclassed for user defined strategies.


   .. py:attribute:: params
      :type:  _typeshed.Incomplete


   .. py:attribute:: rsi
      :type:  _typeshed.Incomplete


   .. py:method:: get_signal()


.. py:class:: MACDStrategy

   Bases: :py:obj:`BaseStrategy`


   Base class to be subclassed for user defined strategies.


   .. py:attribute:: params
      :type:  _typeshed.Incomplete


   .. py:attribute:: macd
      :type:  _typeshed.Incomplete


   .. py:method:: get_signal()


.. py:class:: BollingerBandsStrategy

   Bases: :py:obj:`BaseStrategy`


   Base class to be subclassed for user defined strategies.


   .. py:attribute:: params
      :type:  _typeshed.Incomplete


   .. py:attribute:: bbands
      :type:  _typeshed.Incomplete


   .. py:method:: get_signal()


.. py:class:: MomentumStrategy

   Bases: :py:obj:`BaseStrategy`


   Base class to be subclassed for user defined strategies.


   .. py:attribute:: params
      :type:  _typeshed.Incomplete


   .. py:attribute:: roc
      :type:  _typeshed.Incomplete


   .. py:method:: get_signal()


.. py:class:: MeanReversionStrategy

   Bases: :py:obj:`BaseStrategy`


   Base class to be subclassed for user defined strategies.


   .. py:attribute:: params
      :type:  _typeshed.Incomplete


   .. py:attribute:: sma
      :type:  _typeshed.Incomplete


   .. py:attribute:: stddev
      :type:  _typeshed.Incomplete


   .. py:method:: get_signal()


