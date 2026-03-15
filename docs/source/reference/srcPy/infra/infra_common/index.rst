srcPy.infra.infra_common
========================

.. py:module:: srcPy.infra.infra_common


Functions
---------

.. autoapisummary::

   srcPy.infra.infra_common.retry_async
   srcPy.infra.infra_common.normalize_dataframe
   srcPy.infra.infra_common.ensure_lazy
   srcPy.infra.infra_common.setup_logger


Module Contents
---------------

.. py:function:: retry_async(retries = 3, backoff_factor = 0.5, exceptions = ..., jitter = 0.2)

.. py:function:: normalize_dataframe(df, schema = None, engine = 'polars')

.. py:function:: ensure_lazy(df, *, schema = None)

.. py:function:: setup_logger(name, level = ..., fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

