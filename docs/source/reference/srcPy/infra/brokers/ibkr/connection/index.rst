srcPy.infra.brokers.ibkr.connection
===================================

.. py:module:: srcPy.infra.brokers.ibkr.connection


Attributes
----------

.. autoapisummary::

   srcPy.infra.brokers.ibkr.connection.log


Classes
-------

.. autoapisummary::

   srcPy.infra.brokers.ibkr.connection.IBKR
   srcPy.infra.brokers.ibkr.connection.IBKRConfig


Functions
---------

.. autoapisummary::

   srcPy.infra.brokers.ibkr.connection.get_ibkr_config
   srcPy.infra.brokers.ibkr.connection.ibkr_connection


Module Contents
---------------

.. py:class:: IBKR

.. py:data:: log
   :type:  Any
   :value: Ellipsis


.. py:class:: IBKRConfig(/, **data)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for ibkr.


   .. py:attribute:: host
      :type:  str
      :value: Ellipsis



   .. py:attribute:: port
      :type:  int
      :value: Ellipsis



   .. py:attribute:: client_id
      :type:  int
      :value: Ellipsis



.. py:function:: get_ibkr_config()

.. py:function:: ibkr_connection()

