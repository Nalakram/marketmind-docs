srcPy.infra.infra_config
========================

.. py:module:: srcPy.infra.infra_config


Attributes
----------

.. autoapisummary::

   srcPy.infra.infra_config.logger


Classes
-------

.. autoapisummary::

   srcPy.infra.infra_config.BrokerConfig


Functions
---------

.. autoapisummary::

   srcPy.infra.infra_config.load_broker_config


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: BrokerConfig(/, **data)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for broker.


   .. py:attribute:: host
      :type:  str
      :value: Ellipsis



   .. py:attribute:: port
      :type:  int
      :value: Ellipsis



   .. py:attribute:: client_id
      :type:  int
      :value: Ellipsis



   .. py:attribute:: account
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: timeout
      :type:  float
      :value: Ellipsis



   .. py:attribute:: retries
      :type:  int
      :value: Ellipsis



   .. py:method:: validate_port(v)


   .. py:method:: validate_account(v)


.. py:function:: load_broker_config(config_path = 'pipeline_config.yaml', section = 'ibkr')

