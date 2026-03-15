srcPy.strategies.adaptive_strategy_engine
=========================================

.. py:module:: srcPy.strategies.adaptive_strategy_engine


Attributes
----------

.. autoapisummary::

   srcPy.strategies.adaptive_strategy_engine.LOG


Classes
-------

.. autoapisummary::

   srcPy.strategies.adaptive_strategy_engine.DriftState
   srcPy.strategies.adaptive_strategy_engine.EvolutionEvent
   srcPy.strategies.adaptive_strategy_engine.EvolutionCallback
   srcPy.strategies.adaptive_strategy_engine.AdaptiveParameterSpace
   srcPy.strategies.adaptive_strategy_engine.MultiFrameDriftState
   srcPy.strategies.adaptive_strategy_engine.MultiTimeframeDriftMonitor
   srcPy.strategies.adaptive_strategy_engine.StrategyEnsemble
   srcPy.strategies.adaptive_strategy_engine.SelfEvolvingAdapter
   srcPy.strategies.adaptive_strategy_engine.LoggingEvolutionCallback
   srcPy.strategies.adaptive_strategy_engine.FileEvolutionCallback


Functions
---------

.. autoapisummary::

   srcPy.strategies.adaptive_strategy_engine.create_evolving_system


Module Contents
---------------

.. py:class:: DriftState

   drift state class.


   .. py:attribute:: ref_mean
      :type:  float
      :value: Ellipsis



   .. py:attribute:: ref_std
      :type:  float
      :value: Ellipsis



.. py:data:: LOG
   :type:  Any
   :value: Ellipsis


.. py:class:: EvolutionEvent

   evolution event class.


   .. py:attribute:: timestamp
      :type:  pandas.Timestamp
      :value: Ellipsis



   .. py:attribute:: event_type
      :type:  str
      :value: Ellipsis



   .. py:attribute:: strategy_name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: old_params
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: new_params
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: performance_delta
      :type:  float
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  dict[str, Any]


.. py:class:: EvolutionCallback

   Bases: :py:obj:`Protocol`


   evolution callback class.


   .. py:method:: on_evolution_event(event)


.. py:class:: AdaptiveParameterSpace(base_space, adaptation_rate = 0.1, memory_length = 100)

   adaptive parameter space class.


   .. py:attribute:: base_space
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: adaptation_rate
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: memory_length
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: performance_history
      :type:  dict[str, collections.deque]
      :value: Ellipsis



   .. py:attribute:: current_space
      :type:  Any
      :value: Ellipsis



   .. py:method:: update(params, score)


   .. py:method:: evolve_space()


.. py:class:: MultiFrameDriftState

   multi frame drift state class.


   .. py:attribute:: short_term
      :type:  DriftState | None
      :value: Ellipsis



   .. py:attribute:: medium_term
      :type:  DriftState | None
      :value: Ellipsis



   .. py:attribute:: long_term
      :type:  DriftState | None
      :value: Ellipsis



.. py:class:: MultiTimeframeDriftMonitor(short_window = 20, medium_window = 60, long_window = 200, sensitivity = 2.5)

   multi timeframe drift monitor class.


   .. py:attribute:: short_window
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: medium_window
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: long_window
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: sensitivity
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: state
      :type:  Any
      :value: Ellipsis



   .. py:method:: check_drift(returns)


.. py:class:: StrategyEnsemble(strategies, rebalance_frequency = 50)

   strategy ensemble class.


   .. py:attribute:: strategy_specs
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: rebalance_frequency
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: blend_weights
      :type:  dict[str, float]
      :value: Ellipsis



   .. py:attribute:: performance_history
      :type:  dict[str, list[float]]
      :value: Ellipsis



   .. py:attribute:: steps_since_rebalance
      :type:  int
      :value: Ellipsis



   .. py:method:: update_performance(strategy_name, score)


   .. py:method:: should_rebalance()


   .. py:method:: rebalance_weights()


.. py:class:: SelfEvolvingAdapter(strategies, ctx, prices, evolution_frequency = 100, optimization_trials = 30, min_history_for_evolution = 50, backtest_cfg = None, callbacks = None)

   Adapter for self evolving interface.


   .. py:attribute:: strategies
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: ctx
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: prices
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: evolution_frequency
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: optimization_trials
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: min_history
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: backtest_cfg
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: callbacks
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: step_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: evolution_history
      :type:  list[EvolutionEvent]
      :value: Ellipsis



   .. py:attribute:: strategy_instances
      :type:  dict[str, srcPy.strategies.pipeline_strategy.PipelineStrategy]
      :value: Ellipsis



   .. py:attribute:: champion_challengers
      :type:  dict[str, srcPy.strategies.pipeline_strategy.ChampionChallenger]
      :value: Ellipsis



   .. py:attribute:: adaptive_spaces
      :type:  dict[str, AdaptiveParameterSpace]
      :value: Ellipsis



   .. py:attribute:: drift_monitors
      :type:  dict[str, MultiTimeframeDriftMonitor]
      :value: Ellipsis



   .. py:attribute:: ensemble
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: performance_buffer
      :type:  dict[str, pandas.Series]
      :value: Ellipsis



   .. py:attribute:: last_weights
      :type:  pandas.DataFrame | None
      :value: Ellipsis



   .. py:method:: generate_trade_intent()


   .. py:method:: get_evolution_summary()


   .. py:method:: force_evolution(strategy_name = None)


.. py:class:: LoggingEvolutionCallback

   logging evolution callback class.


   .. py:method:: on_evolution_event(event)


.. py:class:: FileEvolutionCallback(filepath)

   file evolution callback class.


   .. py:attribute:: filepath
      :type:  Any
      :value: Ellipsis



   .. py:method:: on_evolution_event(event)


.. py:function:: create_evolving_system(price_data)

