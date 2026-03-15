srcPy.pipeline.stages.cleaning.imputers.missing
===============================================

.. py:module:: srcPy.pipeline.stages.cleaning.imputers.missing


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.imputers.missing.KalmanFilter
   srcPy.pipeline.stages.cleaning.imputers.missing.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.imputers.missing.BaseMissingImputer
   srcPy.pipeline.stages.cleaning.imputers.missing.MissingValueNormalizerStep
   srcPy.pipeline.stages.cleaning.imputers.missing.MissingImputer


Module Contents
---------------

.. py:data:: KalmanFilter
   :type:  Any
   :value: Ellipsis


.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: BaseMissingImputer(method = 'forward_fill', params = None, mlflow_logger = None, **_)

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.CleaningStep`


   base missing imputer class.


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


.. py:class:: MissingValueNormalizerStep(method = 'forward_fill', params = None, mlflow_logger = None, **_)

   Bases: :py:obj:`BaseMissingImputer`


   base missing imputer class.


.. py:class:: MissingImputer(method = 'forward_fill', params = None, mlflow_logger = None, **_)

   Bases: :py:obj:`MissingValueNormalizerStep`


   base missing imputer class.


