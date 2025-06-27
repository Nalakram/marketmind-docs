srcPy.utils.risk_management
===========================

.. py:module:: srcPy.utils.risk_management


Classes
-------

.. autoapisummary::

   srcPy.utils.risk_management.RiskManager


Functions
---------

.. autoapisummary::

   srcPy.utils.risk_management.get_trailing_stop_loss
   srcPy.utils.risk_management.check_drawdown


Module Contents
---------------

.. py:class:: RiskManager

   .. py:attribute:: p_bins
      :type:  _typeshed.Incomplete


   .. py:attribute:: R_avg
      :type:  _typeshed.Incomplete


   .. py:attribute:: L_avg
      :type:  _typeshed.Incomplete


   .. py:method:: update_historical_data(p, r)


   .. py:method:: get_R_L_for_p(p)


   .. py:method:: calculate_kelly_fraction(p)


.. py:function:: get_trailing_stop_loss(entry_price, current_price, max_price, trail_percent = 0.02)

.. py:function:: check_drawdown(current_balance, max_balance, threshold = 0.2)

