srcPy.pipeline.stages.cleaning.execution
========================================

.. py:module:: srcPy.pipeline.stages.cleaning.execution


Submodules
----------

.. toctree::
   :maxdepth: 1

   /reference/srcPy/pipeline/stages/cleaning/execution/batch/index
   /reference/srcPy/pipeline/stages/cleaning/execution/streaming/index


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.execution.CleanerPipeline
   srcPy.pipeline.stages.cleaning.execution.StreamingCleanerPipeline


Package Contents
----------------

.. py:class:: CleanerPipeline(steps, mlflow_logger = None)

   cleaner pipeline class.


   .. py:attribute:: steps
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:method:: run(df, distributed = False)


   .. py:method:: close()


.. py:class:: StreamingCleanerPipeline(steps, buffer_size = 100, window = 252)

   streaming cleaner pipeline class.


   .. py:attribute:: steps
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: buffer
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: buffer_size
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: window
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:method:: adjust_buffer_size(latency)


   .. py:method:: process_stream(stream_gen)
      :async:



   .. py:method:: close()


