srcPy.pipeline.stages.cleaning.imputers.outliers
================================================

.. py:module:: srcPy.pipeline.stages.cleaning.imputers.outliers


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.imputers.outliers.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.imputers.outliers.BaseOutlierHandler
   srcPy.pipeline.stages.cleaning.imputers.outliers.OutlierNormalizerStep
   srcPy.pipeline.stages.cleaning.imputers.outliers.OutlierHandler


Functions
---------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.imputers.outliers.efficient_outlier_mask


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:function:: efficient_outlier_mask(num, threshold)

.. py:class:: BaseOutlierHandler(method = 'zscore', params = None, mlflow_logger = None, **_)

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.CleaningStep`


   Handles base outlier events and requests.


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


.. py:class:: OutlierNormalizerStep(method = 'zscore', params = None, mlflow_logger = None, **_)

   Bases: :py:obj:`BaseOutlierHandler`


   Handles base outlier events and requests.


.. py:class:: OutlierHandler(method = 'zscore', params = None, mlflow_logger = None, **_)

   Bases: :py:obj:`OutlierNormalizerStep`


   Handles base outlier events and requests.


