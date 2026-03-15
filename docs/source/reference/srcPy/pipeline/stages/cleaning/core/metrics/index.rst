srcPy.pipeline.stages.cleaning.core.metrics
===========================================

.. py:module:: srcPy.pipeline.stages.cleaning.core.metrics


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.core.metrics.mlflow


Exceptions
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.core.metrics.CleaningMetricsError
   srcPy.pipeline.stages.cleaning.core.metrics.MLflowUnavailable


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.core.metrics.AsyncMLflowLogger


Functions
---------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.core.metrics.log_metric_mlflow
   srcPy.pipeline.stages.cleaning.core.metrics.record_step_latency_ms
   srcPy.pipeline.stages.cleaning.core.metrics.wire_cleaner_observers


Module Contents
---------------

.. py:exception:: CleaningMetricsError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: MLflowUnavailable

   Bases: :py:obj:`CleaningMetricsError`


   Common base class for all non-exit exceptions.


.. py:data:: mlflow
   :type:  Any
   :value: Ellipsis


.. py:class:: AsyncMLflowLogger

   async m lflow logger class.


   .. py:method:: log_metrics(metrics, *, step = None)
      :async:



   .. py:method:: log_params(params)
      :async:



   .. py:method:: set_experiment(name)
      :async:



   .. py:method:: start_run(*, run_name = None, nested = True, tags = None)
      :async:



   .. py:method:: end_run()
      :async:



   .. py:method:: log_artifact(local_path, *, artifact_path = None)
      :async:



.. py:function:: log_metric_mlflow(key, value)
   :async:


.. py:function:: record_step_latency_ms(value_ms, *, step = 'unknown')

.. py:function:: wire_cleaner_observers(*, get_latency, get_buffer_len, get_data_volume)

