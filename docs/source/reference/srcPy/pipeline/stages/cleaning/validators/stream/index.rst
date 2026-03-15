srcPy.pipeline.stages.cleaning.validators.stream
================================================

.. py:module:: srcPy.pipeline.stages.cleaning.validators.stream


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.validators.stream.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.validators.stream.StreamValidationStep


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: StreamValidationStep(mlflow_logger, schema = None, strict = True, sampling_rate = 1.0)

   Bases: :py:obj:`srcPy.pipeline.stages.cleaning.core.base.CleaningStep`


   stream validation step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: schema
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: strict
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: sampling_rate
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


