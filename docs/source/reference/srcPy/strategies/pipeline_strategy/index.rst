srcPy.strategies.pipeline_strategy
==================================

.. py:module:: srcPy.strategies.pipeline_strategy


Attributes
----------

.. autoapisummary::

   srcPy.strategies.pipeline_strategy.LOG


Exceptions
----------

.. autoapisummary::

   srcPy.strategies.pipeline_strategy.PipelineError
   srcPy.strategies.pipeline_strategy.ValidationError
   srcPy.strategies.pipeline_strategy.MaterializationError


Classes
-------

.. autoapisummary::

   srcPy.strategies.pipeline_strategy.TradeIntent
   srcPy.strategies.pipeline_strategy.StrategyContext
   srcPy.strategies.pipeline_strategy.RegimeDetector
   srcPy.strategies.pipeline_strategy.RiskManager
   srcPy.strategies.pipeline_strategy.PositionSizer
   srcPy.strategies.pipeline_strategy.FeatureStep
   srcPy.strategies.pipeline_strategy.FeaturePlan
   srcPy.strategies.pipeline_strategy.StrategySpec
   srcPy.strategies.pipeline_strategy.StrategyRegistry
   srcPy.strategies.pipeline_strategy.PipelineStrategy
   srcPy.strategies.pipeline_strategy.BacktestConfig
   srcPy.strategies.pipeline_strategy.SweepResult
   srcPy.strategies.pipeline_strategy.DriftState
   srcPy.strategies.pipeline_strategy.ChampionChallenger
   srcPy.strategies.pipeline_strategy.NullRegime
   srcPy.strategies.pipeline_strategy.LinearSizer
   srcPy.strategies.pipeline_strategy.TurnoverLimiterRisk
   srcPy.strategies.pipeline_strategy.BlendSpec
   srcPy.strategies.pipeline_strategy.LegacyBaseStrategy


Functions
---------

.. autoapisummary::

   srcPy.strategies.pipeline_strategy.feature_op
   srcPy.strategies.pipeline_strategy.op_pct_change
   srcPy.strategies.pipeline_strategy.op_roll_mean
   srcPy.strategies.pipeline_strategy.op_roll_std
   srcPy.strategies.pipeline_strategy.op_ema
   srcPy.strategies.pipeline_strategy.op_zscore
   srcPy.strategies.pipeline_strategy.materialize_features
   srcPy.strategies.pipeline_strategy.backtest_portfolio
   srcPy.strategies.pipeline_strategy.parameter_sweep
   srcPy.strategies.pipeline_strategy.optuna_tune
   srcPy.strategies.pipeline_strategy.detect_drift
   srcPy.strategies.pipeline_strategy.blend


Module Contents
---------------

.. py:data:: LOG
   :type:  Any
   :value: Ellipsis


.. py:exception:: PipelineError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: ValidationError

   Bases: :py:obj:`PipelineError`


   Common base class for all non-exit exceptions.


.. py:exception:: MaterializationError

   Bases: :py:obj:`PipelineError`


   Common base class for all non-exit exceptions.


.. py:class:: TradeIntent

   trade intent class.


   .. py:attribute:: weights
      :type:  pandas.Series | pandas.DataFrame
      :value: Ellipsis



   .. py:attribute:: raw
      :type:  Mapping[str, Any]


   .. py:attribute:: diagnostics
      :type:  Mapping[str, Any]


.. py:class:: StrategyContext

   strategy context class.


   .. py:attribute:: prices
      :type:  pandas.Series | pandas.DataFrame
      :value: Ellipsis



   .. py:attribute:: features
      :type:  pandas.DataFrame | polars.DataFrame | None
      :value: Ellipsis



   .. py:attribute:: timestamps
      :type:  pandas.Index | None
      :value: Ellipsis



   .. py:attribute:: asset_names
      :type:  list[str] | None
      :value: Ellipsis



   .. py:attribute:: backend
      :type:  str
      :value: Ellipsis



   .. py:attribute:: cache_dir
      :type:  str | pathlib.Path
      :value: Ellipsis



   .. py:attribute:: random_state
      :type:  int
      :value: Ellipsis



   .. py:method:: validate()


.. py:class:: RegimeDetector

   Bases: :py:obj:`Protocol`


   regime detector class.


   .. py:method:: gate(features)


.. py:class:: RiskManager

   Bases: :py:obj:`Protocol`


   Manages risk resources and operations.


   .. py:method:: clamp(weights, prices, **kwargs)


.. py:class:: PositionSizer

   Bases: :py:obj:`Protocol`


   position sizer class.


   .. py:method:: size(signal, **kwargs)


.. py:class:: FeatureStep

   feature step class.


   .. py:attribute:: op
      :type:  str
      :value: Ellipsis



   .. py:attribute:: inputs
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: args
      :type:  tuple[Any, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: kwargs
      :type:  Mapping[str, Any]


   .. py:attribute:: out
      :type:  str
      :value: Ellipsis



.. py:class:: FeaturePlan

   feature plan class.


   .. py:attribute:: steps
      :type:  list[FeatureStep]
      :value: Ellipsis



   .. py:method:: signature()


.. py:function:: feature_op(name)

.. py:function:: op_pct_change(df, col, periods = 1, out = None)

.. py:function:: op_roll_mean(df, col, window, minp = None, out = None)

.. py:function:: op_roll_std(df, col, window, minp = None, out = None)

.. py:function:: op_ema(df, col, span, adjust = False, out = None)

.. py:function:: op_zscore(df, col, window, minp = None, out = None)

.. py:function:: materialize_features(ctx, plan, price_col = None)

.. py:class:: StrategySpec

   strategy spec class.


   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: params
      :type:  Mapping[str, Any]


.. py:class:: StrategyRegistry

   strategy registry class.


   .. py:method:: register(name, strat_cls)
      :classmethod:



   .. py:method:: get(name)
      :classmethod:



   .. py:method:: clear_for_test()
      :classmethod:



.. py:class:: PipelineStrategy(**params)

   Strategy for pipeline behavior.


   .. py:attribute:: regime
      :type:  RegimeDetector | None
      :value: Ellipsis



   .. py:attribute:: risk
      :type:  RiskManager | None
      :value: Ellipsis



   .. py:attribute:: sizer
      :type:  PositionSizer | None
      :value: Ellipsis



   .. py:attribute:: params
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: random_state
      :type:  Any
      :value: Ellipsis



   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


   .. py:method:: generate_trade_intent(ctx)


.. py:class:: BacktestConfig

   Configuration for backtest.


   .. py:attribute:: cost_per_unit_turnover
      :type:  float
      :value: Ellipsis



   .. py:attribute:: leverage_cap
      :type:  float
      :value: Ellipsis



   .. py:attribute:: initial_nav
      :type:  float
      :value: Ellipsis



.. py:function:: backtest_portfolio(prices, weights, cfg)

.. py:class:: SweepResult

   sweep result class.


   .. py:attribute:: params
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: score
      :type:  float
      :value: Ellipsis



   .. py:attribute:: details
      :type:  Mapping[str, Any]


.. py:function:: parameter_sweep(strategy_cls, param_grid, ctx, *, prices = None, backtest_cfg = None, n_jobs = 1)

.. py:function:: optuna_tune(strategy_cls, sampler_spec, ctx, *, prices = None, backtest_cfg = None, n_trials = 50)

.. py:class:: DriftState

   drift state class.


   .. py:attribute:: ref_mean
      :type:  float
      :value: Ellipsis



   .. py:attribute:: ref_std
      :type:  float
      :value: Ellipsis



.. py:function:: detect_drift(series, st, threshold = 3.0, sensitivity = 1.0)

.. py:class:: ChampionChallenger

   champion challenger class.


   .. py:attribute:: strategy_cls
      :type:  type[PipelineStrategy]
      :value: Ellipsis



   .. py:attribute:: ctx
      :type:  StrategyContext
      :value: Ellipsis



   .. py:attribute:: prices
      :type:  pandas.DataFrame
      :value: Ellipsis



   .. py:attribute:: backtest_cfg
      :type:  BacktestConfig


   .. py:attribute:: champion_params
      :type:  dict[str, Any]


   .. py:attribute:: history
      :type:  list[tuple[str, dict[str, Any], float]]
      :value: []



   .. py:method:: evaluate(params)


   .. py:method:: step(challenger_params, improvement = 0.01)


.. py:class:: NullRegime

   null regime class.


   .. py:method:: gate(features)


.. py:class:: LinearSizer(scale = 1.0, clip = 1.0)

   linear sizer class.


   .. py:attribute:: scale
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: clip
      :type:  Any
      :value: Ellipsis



   .. py:method:: size(signal, **_)


.. py:class:: TurnoverLimiterRisk(max_turnover = 0.5)

   turnover limiter risk class.


   .. py:attribute:: max_turnover
      :type:  Any
      :value: Ellipsis



   .. py:method:: clamp(weights, prices, **_)


.. py:class:: BlendSpec

   blend spec class.


   .. py:attribute:: parts
      :type:  list[tuple[float, PipelineStrategy]]
      :value: Ellipsis



   .. py:method:: normalize()


.. py:function:: blend(ctx, spec)

.. py:class:: LegacyBaseStrategy(legacy_impl, **params)

   Bases: :py:obj:`PipelineStrategy`


   Strategy for legacy base behavior.


   .. py:attribute:: legacy
      :type:  Any
      :value: Ellipsis



   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


