srcPy.backtest_pipeline
=======================

.. py:module:: srcPy.backtest_pipeline


Attributes
----------

.. autoapisummary::

   srcPy.backtest_pipeline.SERVICE_NAME
   srcPy.backtest_pipeline.TENANT_ID
   srcPy.backtest_pipeline.metrics
   srcPy.backtest_pipeline.tracing
   srcPy.backtest_pipeline.logger
   srcPy.backtest_pipeline.CACHE_TTL
   srcPy.backtest_pipeline.L2_TYPE
   srcPy.backtest_pipeline.CACHE
   srcPy.backtest_pipeline.DataSplit


Classes
-------

.. autoapisummary::

   srcPy.backtest_pipeline.ObsTimer
   srcPy.backtest_pipeline.RunSpec
   srcPy.backtest_pipeline.RunResult
   srcPy.backtest_pipeline.SupportsClean


Functions
---------

.. autoapisummary::

   srcPy.backtest_pipeline.load_data
   srcPy.backtest_pipeline.run_backtests
   srcPy.backtest_pipeline.statistical_tests
   srcPy.backtest_pipeline.load_regimes
   srcPy.backtest_pipeline.main


Module Contents
---------------

.. py:data:: SERVICE_NAME
   :type:  Any
   :value: Ellipsis


.. py:data:: TENANT_ID
   :type:  Any
   :value: Ellipsis


.. py:data:: metrics
   :type:  Any
   :value: Ellipsis


.. py:data:: tracing
   :type:  Any
   :value: Ellipsis


.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: ObsTimer(name, labels = None)

   obs timer class.


   .. py:attribute:: name
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: labels
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: t0
      :type:  float
      :value: Ellipsis



   .. py:method:: __enter__()


   .. py:method:: __exit__(exc_type, exc, tb)


.. py:data:: CACHE_TTL
   :type:  Any
   :value: Ellipsis


.. py:data:: L2_TYPE
   :type:  Any
   :value: Ellipsis


.. py:data:: CACHE
   :type:  Any
   :value: Ellipsis


.. py:class:: RunSpec

   run spec class.


   .. py:attribute:: strategy_key
      :type:  str
      :value: Ellipsis



   .. py:attribute:: params
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: regime
      :type:  str
      :value: Ellipsis



   .. py:attribute:: start
      :type:  str
      :value: Ellipsis



   .. py:attribute:: end
      :type:  str
      :value: Ellipsis



   .. py:attribute:: seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: leverage_cap
      :type:  float
      :value: Ellipsis



   .. py:attribute:: turn_cost
      :type:  float
      :value: Ellipsis



   .. py:attribute:: initial_nav
      :type:  float
      :value: Ellipsis



.. py:class:: RunResult

   run result class.


   .. py:attribute:: ok
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: regime
      :type:  str
      :value: Ellipsis



   .. py:attribute:: seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: metrics_out
      :type:  Mapping[str, Any] | None
      :value: Ellipsis



.. py:type:: DataSplit
   :canonical: ...


.. py:class:: SupportsClean

   Bases: :py:obj:`Protocol`


   supports clean class.


   .. py:method:: clean(df)


.. py:function:: load_data(start_date, end_date, cleaner = None)

.. py:function:: run_backtests(strategy_key, params, regimes, *, leverage_cap = 1.0, commission = 0.0, slippage_perc = 0.0005, initial_nav = 1.0, num_seeds = 8, max_workers = None, cleaner = None, timeout_s = None)

.. py:function:: statistical_tests(results)

.. py:function:: load_regimes(config_file = None, cli_args = None)

.. py:function:: main(strategy = 'momentum', params = None, regimes = None, *, leverage_cap = 1.0, commission = 0.0, slippage_perc = 0.0005, initial_nav = 1.0, num_seeds = 8, max_workers = None, cleaner = None, timeout_s = None)

