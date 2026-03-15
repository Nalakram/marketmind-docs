srcPy.pipeline.stages.cleaning.imputers.denoise
===============================================

.. py:module:: srcPy.pipeline.stages.cleaning.imputers.denoise


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.imputers.denoise.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.imputers.denoise.DenoiseNormalizerStep


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


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


