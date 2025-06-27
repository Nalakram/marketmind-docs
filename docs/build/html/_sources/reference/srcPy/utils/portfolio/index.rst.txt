srcPy.utils.portfolio
=====================

.. py:module:: srcPy.utils.portfolio


Classes
-------

.. autoapisummary::

   srcPy.utils.portfolio.PortfolioOptimizer


Functions
---------

.. autoapisummary::

   srcPy.utils.portfolio.optimise_portfolio


Module Contents
---------------

.. py:class:: PortfolioOptimizer(expected_returns, cov_matrix, capital, *, objective = 'mean_variance', constraints = None, solver = 'cvxpy', risk_free_rate = 0.0, random_state = None)

   .. py:attribute:: expected_returns
      :type:  _typeshed.Incomplete


   .. py:attribute:: cov_matrix
      :type:  _typeshed.Incomplete


   .. py:attribute:: capital
      :type:  _typeshed.Incomplete


   .. py:attribute:: objective
      :type:  _typeshed.Incomplete


   .. py:attribute:: constraints
      :type:  _typeshed.Incomplete


   .. py:attribute:: solver
      :type:  _typeshed.Incomplete


   .. py:attribute:: risk_free_rate
      :type:  _typeshed.Incomplete


   .. py:attribute:: random_state
      :type:  _typeshed.Incomplete


   .. py:method:: optimise()


.. py:function:: optimise_portfolio(expected_returns, cov_matrix, capital, **kwargs)

