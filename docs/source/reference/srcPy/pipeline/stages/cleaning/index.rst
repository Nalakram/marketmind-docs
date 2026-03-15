srcPy.pipeline.stages.cleaning
==============================

.. py:module:: srcPy.pipeline.stages.cleaning


Submodules
----------

.. toctree::
   :maxdepth: 1

   /reference/srcPy/pipeline/stages/cleaning/anomalies/index
   /reference/srcPy/pipeline/stages/cleaning/core/index
   /reference/srcPy/pipeline/stages/cleaning/execution/index
   /reference/srcPy/pipeline/stages/cleaning/features/index
   /reference/srcPy/pipeline/stages/cleaning/imputers/index
   /reference/srcPy/pipeline/stages/cleaning/validators/index


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.DenoiseNormalizerStep
   srcPy.pipeline.stages.cleaning.MissingImputer
   srcPy.pipeline.stages.cleaning.MissingValueNormalizerStep
   srcPy.pipeline.stages.cleaning.OutlierHandler
   srcPy.pipeline.stages.cleaning.OutlierNormalizerStep
   srcPy.pipeline.stages.cleaning.StepRegistry


Package Contents
----------------

.. py:class:: DenoiseNormalizerStep(method = 'ewm', params = None, mlflow_logger = None, **_)

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.CleaningStep`


   denoise normalizer step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: method
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: params
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: supported_methods
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


.. py:class:: MissingImputer(method = 'forward_fill', params = None, mlflow_logger = None, **_)

   Bases: :py:obj:`MissingValueNormalizerStep`


   base missing imputer class.


.. py:class:: MissingValueNormalizerStep(method = 'forward_fill', params = None, mlflow_logger = None, **_)

   Bases: :py:obj:`BaseMissingImputer`


   base missing imputer class.


.. py:class:: OutlierHandler(method = 'zscore', params = None, mlflow_logger = None, **_)

   Bases: :py:obj:`OutlierNormalizerStep`


   Handles base outlier events and requests.


.. py:class:: OutlierNormalizerStep(method = 'zscore', params = None, mlflow_logger = None, **_)

   Bases: :py:obj:`BaseOutlierHandler`


   Handles base outlier events and requests.


.. py:class:: StepRegistry

   step registry class.


   .. py:method:: register(*args, override = False)
      :classmethod:



   .. py:method:: get(stage, name)
      :classmethod:



   .. py:method:: load_plugins(entry_point_group, stage)
      :classmethod:



