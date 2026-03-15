srcPy.strategies.migrated_strategies
====================================

.. py:module:: srcPy.strategies.migrated_strategies


Classes
-------

.. autoapisummary::

   srcPy.strategies.migrated_strategies.RSIStrategy
   srcPy.strategies.migrated_strategies.MACDStrategy
   srcPy.strategies.migrated_strategies.BollingerBandsStrategy
   srcPy.strategies.migrated_strategies.MeanReversionStrategy
   srcPy.strategies.migrated_strategies.MovingAverageCrossoverStrategy
   srcPy.strategies.migrated_strategies.EnsemblePipelineStrategy


Functions
---------

.. autoapisummary::

   srcPy.strategies.migrated_strategies.clear_strategy_cache


Module Contents
---------------

.. py:function:: clear_strategy_cache()

.. py:class:: RSIStrategy(rsi_window = 14, upper = 70.0, lower = 30.0, neutral_zone = True, clip = 1.0, zero_on_any_nan = True, **kwargs)

   Bases: :py:obj:`srcPy.strategies.pipeline_strategy.PipelineStrategy`


   Strategy for rsi behavior.


   .. py:attribute:: rsi_window
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: upper
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: lower
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: neutral_zone
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: clip
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: zero_on_any_nan
      :type:  Any
      :value: Ellipsis



   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


.. py:class:: MACDStrategy(fast = 12, slow = 26, signal = 9, use_histogram = True, clip = 1.0, **kwargs)

   Bases: :py:obj:`srcPy.strategies.pipeline_strategy.PipelineStrategy`


   Strategy for macd behavior.


   .. py:attribute:: fast
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: slow
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: signal
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: use_histogram
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: clip
      :type:  Any
      :value: Ellipsis



   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


.. py:class:: BollingerBandsStrategy(period = 20, num_std = 2.0, mode = 'reversion', clip = 1.0, **kwargs)

   Bases: :py:obj:`srcPy.strategies.pipeline_strategy.PipelineStrategy`


   Strategy for bollinger bands behavior.


   .. py:attribute:: period
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: num_std
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: mode
      :type:  Literal['reversion', 'breakout']
      :value: Ellipsis



   .. py:attribute:: clip
      :type:  Any
      :value: Ellipsis



   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


.. py:class:: MeanReversionStrategy(period = 20, entry_threshold = 2.0, exit_threshold = 0.5, clip = 1.0, **kwargs)

   Bases: :py:obj:`srcPy.strategies.pipeline_strategy.PipelineStrategy`


   Strategy for mean reversion behavior.


   .. py:attribute:: period
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: entry_threshold
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: exit_threshold
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: clip
      :type:  Any
      :value: Ellipsis



   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


.. py:class:: MovingAverageCrossoverStrategy(short = 50, long = 200, ma_type = 'sma', use_momentum = False, clip = 1.0, price_col = None, **kwargs)

   Bases: :py:obj:`srcPy.strategies.pipeline_strategy.PipelineStrategy`


   Strategy for moving average crossover behavior.


   .. py:attribute:: short
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: long
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: ma_type
      :type:  Literal['sma', 'ema']
      :value: Ellipsis



   .. py:attribute:: use_momentum
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: clip
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: price_col
      :type:  Any
      :value: Ellipsis



   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


.. py:class:: EnsemblePipelineStrategy(strategy_specs, weights = None, combination_method = 'weighted', adaptive_weights = False, performance_window = 50, **kwargs)

   Bases: :py:obj:`srcPy.strategies.pipeline_strategy.PipelineStrategy`


   Strategy for ensemble pipeline behavior.


   .. py:attribute:: ADAPTIVE_UPDATE_INTERVAL
      :type:  Final[int]
      :value: Ellipsis



   .. py:attribute:: MAX_FAILURES
      :type:  Final[int]
      :value: Ellipsis



   .. py:attribute:: MIN_WEIGHT_FLOOR
      :type:  Final[float]
      :value: Ellipsis



   .. py:attribute:: strategy_specs
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: combination_method
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: adaptive_weights
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: performance_window
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: weights
      :type:  Any
      :value: Ellipsis



   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


