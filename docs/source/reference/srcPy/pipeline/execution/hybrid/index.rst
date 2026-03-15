srcPy.pipeline.execution.hybrid
===============================

.. py:module:: srcPy.pipeline.execution.hybrid


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.execution.hybrid.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.execution.hybrid.HybridCleanerPipeline


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: HybridCleanerPipeline(steps, streaming = False, buffer_size = 100, window = 252, mlflow_logger = None)

   Bases: :py:obj:`srcPy.pipeline.execution.batch.BatchPipeline`


   hybrid cleaner pipeline class.


   .. py:attribute:: config
      :type:  dict
      :value: Ellipsis



   .. py:attribute:: streaming
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: streaming_pipeline
      :type:  Any
      :value: Ellipsis



   .. py:method:: run_batch(df, distributed = False)


   .. py:method:: run_stream(stream_gen)
      :async:



   .. py:method:: run(df = None, stream_gen = None, distributed = False)
      :async:



