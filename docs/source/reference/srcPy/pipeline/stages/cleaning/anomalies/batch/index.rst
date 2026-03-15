srcPy.pipeline.stages.cleaning.anomalies.batch
==============================================

.. py:module:: srcPy.pipeline.stages.cleaning.anomalies.batch


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.anomalies.batch.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.anomalies.batch.AnomalyNormalizerStep


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: AnomalyNormalizerStep(mlflow_logger, **cfg)

   Bases: :py:obj:`BaseAnomalyNormalizerStep`


   anomaly normalizer step class.


   .. py:attribute:: contamination
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: refit_every_rows
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: sample_size
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: method
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: model
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: executor
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: counter
      :type:  int
      :value: Ellipsis



   .. py:attribute:: fit_future
      :type:  Any
      :value: Ellipsis



   .. py:method:: close()


   .. py:method:: __del__()


