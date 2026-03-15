srcPy.pipeline.stages.cleaning.features.macro
=============================================

.. py:module:: srcPy.pipeline.stages.cleaning.features.macro


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.features.macro.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.features.macro.EconomicIndicatorNormalizerStep


Functions
---------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.features.macro.fetch_fred_data


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:function:: fetch_fred_data(indicator, start, end)

.. py:class:: EconomicIndicatorNormalizerStep(mlflow_logger, enabled, indicators, timestamp_col = 'timestamp')

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.CleaningStep`


   economic indicator normalizer step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: enabled
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: indicators
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: timestamp_col
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


