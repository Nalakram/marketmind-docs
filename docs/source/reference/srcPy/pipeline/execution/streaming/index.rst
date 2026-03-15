srcPy.pipeline.execution.streaming
==================================

.. py:module:: srcPy.pipeline.execution.streaming


Classes
-------

.. autoapisummary::

   srcPy.pipeline.execution.streaming.StreamingIsolationForest
   srcPy.pipeline.execution.streaming.StreamingPipeline
   srcPy.pipeline.execution.streaming.StreamingCleanerPipeline


Module Contents
---------------

.. py:class:: StreamingIsolationForest(contamination = 0.1, refit_every = 100, window_size = 500)

   streaming isolation forest class.


   .. py:attribute:: contamination
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: refit_every
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: window_size
      :type:  Any
      :value: Ellipsis



   .. py:property:: buffer


   .. py:property:: counter


   .. py:property:: model


   .. py:method:: predict(X)


.. py:class:: StreamingPipeline(steps, config = None)

   streaming pipeline class.


   .. py:attribute:: steps
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:method:: run(data_stream, context)
      :async:



.. py:class:: StreamingCleanerPipeline(steps, config = None)

   Bases: :py:obj:`StreamingPipeline`


   streaming cleaner pipeline class.


   .. py:attribute:: enable_anomaly
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: anomaly_detector
      :type:  StreamingIsolationForest | None
      :value: Ellipsis



   .. py:attribute:: incremental_steps
      :type:  list[Any]
      :value: Ellipsis



