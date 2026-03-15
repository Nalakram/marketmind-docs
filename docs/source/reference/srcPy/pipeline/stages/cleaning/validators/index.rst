srcPy.pipeline.stages.cleaning.validators
=========================================

.. py:module:: srcPy.pipeline.stages.cleaning.validators


Submodules
----------

.. toctree::
   :maxdepth: 1

   /reference/srcPy/pipeline/stages/cleaning/validators/contracts/index
   /reference/srcPy/pipeline/stages/cleaning/validators/drift/index
   /reference/srcPy/pipeline/stages/cleaning/validators/io/index
   /reference/srcPy/pipeline/stages/cleaning/validators/schema/index
   /reference/srcPy/pipeline/stages/cleaning/validators/stream/index


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.validators.logger
   srcPy.pipeline.stages.cleaning.validators.validator_steps


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.validators.DriftDetectionStep
   srcPy.pipeline.stages.cleaning.validators.IOValidationStep
   srcPy.pipeline.stages.cleaning.validators.ValidationStep
   srcPy.pipeline.stages.cleaning.validators.StreamValidationStep
   srcPy.pipeline.stages.cleaning.validators.StepRegistry


Functions
---------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.validators.get_logger


Package Contents
----------------

.. py:class:: DriftDetectionStep(mlflow_logger, enabled = True, reference_data = None, threshold = 0.05, columns = None, test = None, strict = True)

   Bases: :py:obj:`srcPy.pipeline.stages.cleaning.core.base.CleaningStep`


   drift detection step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: enabled
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: reference_data
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: threshold
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: columns
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: test
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: strict
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


.. py:class:: IOValidationStep(mlflow_logger, file_path, format = None, max_size_bytes = ..., fs = None)

   Bases: :py:obj:`srcPy.pipeline.stages.cleaning.core.base.CleaningStep`


   io validation step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: file_path
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: format
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: max_size_bytes
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: fs
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: supported_formats
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


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


.. py:function:: get_logger(name = None)

.. py:class:: StepRegistry

   step registry class.


   .. py:method:: register(name, step_cls)
      :classmethod:



   .. py:method:: get(name)
      :classmethod:



   .. py:method:: freeze()
      :classmethod:



   .. py:method:: thaw()
      :classmethod:



   .. py:method:: list_registered()
      :classmethod:



.. py:data:: logger
   :type:  _typeshed.Incomplete

.. py:data:: validator_steps
   :type:  _typeshed.Incomplete

