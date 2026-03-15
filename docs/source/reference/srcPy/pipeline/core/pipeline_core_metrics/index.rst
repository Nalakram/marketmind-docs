srcPy.pipeline.core.pipeline_core_metrics
=========================================

.. py:module:: srcPy.pipeline.core.pipeline_core_metrics


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.core.pipeline_core_metrics.ERROR_COUNTER
   srcPy.pipeline.core.pipeline_core_metrics.STEP_EXECUTION_TIME
   srcPy.pipeline.core.pipeline_core_metrics.mlflow


Exceptions
----------

.. autoapisummary::

   srcPy.pipeline.core.pipeline_core_metrics.PipelineMetricsError
   srcPy.pipeline.core.pipeline_core_metrics.MLflowUnavailable


Classes
-------

.. autoapisummary::

   srcPy.pipeline.core.pipeline_core_metrics.AsyncMLflowLogger


Functions
---------

.. autoapisummary::

   srcPy.pipeline.core.pipeline_core_metrics.track_step_execution
   srcPy.pipeline.core.pipeline_core_metrics.wire_streaming_observers


Module Contents
---------------

.. py:exception:: PipelineMetricsError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: MLflowUnavailable

   Bases: :py:obj:`PipelineMetricsError`


   Common base class for all non-exit exceptions.


.. py:data:: ERROR_COUNTER
   :type:  Any
   :value: Ellipsis


.. py:data:: STEP_EXECUTION_TIME
   :type:  Any
   :value: Ellipsis


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



.. py:function:: track_step_execution(step_name, *, stage = 'unknown', engine = 'unknown')

.. py:function:: wire_streaming_observers(get_buffer_len, get_processed_volume)

