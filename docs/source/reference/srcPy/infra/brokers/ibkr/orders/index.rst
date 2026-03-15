srcPy.infra.brokers.ibkr.orders
===============================

.. py:module:: srcPy.infra.brokers.ibkr.orders


Classes
-------

.. autoapisummary::

   srcPy.infra.brokers.ibkr.orders.IBKROrderExecutor


Module Contents
---------------

.. py:class:: IBKROrderExecutor(conn_cfg)

   Bases: :py:obj:`srcPy.domain.interfaces.OrderExecutor`


   ibkr order executor class.


   .. py:attribute:: cfg
      :type:  Any
      :value: Ellipsis



   .. py:method:: submit(order)


   .. py:method:: cancel(order_id)


   .. py:method:: status(order_id)


