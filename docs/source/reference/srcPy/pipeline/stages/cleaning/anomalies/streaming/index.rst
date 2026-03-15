srcPy.pipeline.stages.cleaning.anomalies.streaming
==================================================

.. py:module:: srcPy.pipeline.stages.cleaning.anomalies.streaming


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.anomalies.streaming.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.anomalies.streaming.StreamingIsolationForest
   srcPy.pipeline.stages.cleaning.anomalies.streaming.StreamingAnomalyNormalizerStep


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: StreamingIsolationForest(contamination, refit_every, window_size = 1000)

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



   .. py:attribute:: buffer
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: counter
      :type:  int
      :value: Ellipsis



   .. py:attribute:: model
      :type:  Any
      :value: Ellipsis



   .. py:method:: predict(df)


.. py:class:: StreamingAnomalyNormalizerStep(mlflow_logger, **cfg)

   Bases: :py:obj:`BaseAnomalyNormalizerStep`


   streaming anomaly normalizer step class.


   .. py:attribute:: contamination
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: refit_every
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: window_size
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: detector
      :type:  Any
      :value: Ellipsis



