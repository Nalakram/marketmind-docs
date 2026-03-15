srcPy.pipeline.stages.cleaning.validators.schema
================================================

.. py:module:: srcPy.pipeline.stages.cleaning.validators.schema


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.validators.schema.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.validators.schema.ValidationStep


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: ValidationStep(mlflow_logger, required_columns = None, ohlcv_mode = False, schema = None, strict = True)

   Bases: :py:obj:`srcPy.pipeline.stages.cleaning.core.base.CleaningStep`


   validation step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: required_columns
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: ohlcv_mode
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: schema
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: strict
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


