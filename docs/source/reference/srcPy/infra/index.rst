srcPy.infra
===========

.. py:module:: srcPy.infra


Submodules
----------

.. toctree::
   :maxdepth: 1

   /reference/srcPy/infra/brokers/index
   /reference/srcPy/infra/infra_common/index
   /reference/srcPy/infra/infra_config/index
   /reference/srcPy/infra/infra_factory/index


Classes
-------

.. autoapisummary::

   srcPy.infra.BrokerConfig
   srcPy.infra.DataSourceFactory


Functions
---------

.. autoapisummary::

   srcPy.infra.ensure_lazy
   srcPy.infra.get_logger
   srcPy.infra.normalize_dataframe
   srcPy.infra.retry_async
   srcPy.infra.setup_logger
   srcPy.infra.load_broker_config
   srcPy.infra.list_sources
   srcPy.infra.register_source
   srcPy.infra.unregister_source


Package Contents
----------------

.. py:function:: ensure_lazy(df, *, schema = None)

.. py:function:: get_logger(name = None)

.. py:function:: normalize_dataframe(df, schema = None, engine = 'polars')

.. py:function:: retry_async(retries = 3, backoff_factor = 0.5, exceptions = ..., jitter = 0.2)

.. py:function:: setup_logger(name, level = ..., fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

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

.. py:class:: DataSourceFactory

   Factory for creating data source instances.


   .. py:method:: create(source_type, /, **kwargs)
      :staticmethod:



.. py:function:: list_sources()

.. py:function:: register_source(name, creator)

.. py:function:: unregister_source(name)

