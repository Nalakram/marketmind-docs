srcPy.backtesting
=================

.. py:module:: srcPy.backtesting


Attributes
----------

.. autoapisummary::

   srcPy.backtesting.logger


Functions
---------

.. autoapisummary::

   srcPy.backtesting.load_data
   srcPy.backtesting.run_single_backtest
   srcPy.backtesting.run_backtests
   srcPy.backtesting.statistical_tests
   srcPy.backtesting.load_regimes
   srcPy.backtesting.main


Module Contents
---------------

.. py:data:: logger
   :type:  _typeshed.Incomplete

.. py:function:: load_data(start_date, end_date)

.. py:function:: run_single_backtest(regime, start, end, model, initial_cash, commission, position_size, riskfreerate, seed)

.. py:function:: run_backtests(model, regimes, initial_cash = 100000, commission = 0.001, position_size = 1.0, riskfreerate = 0.02, num_seeds = 30, max_workers = 4)

.. py:function:: statistical_tests(results)

.. py:function:: load_regimes(config_file = None)

.. py:function:: main(model)

