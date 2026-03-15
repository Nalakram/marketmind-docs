srcPy.pipeline.stages.cleaning.execution.streaming
==================================================

.. py:module:: srcPy.pipeline.stages.cleaning.execution.streaming


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.execution.streaming.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.execution.streaming.StreamingCleanerPipeline


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


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


