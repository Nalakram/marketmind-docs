srcPy.pipeline.stages.cleaning.features.altdata
===============================================

.. py:module:: srcPy.pipeline.stages.cleaning.features.altdata


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.features.altdata.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.features.altdata.AlternativeDataNormalizerStep


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: AlternativeDataNormalizerStep(mlflow_logger, enabled, esg_enabled = False, supply_chain_enabled = False, custom_sources = None)

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.CleaningStep`


   alternative data normalizer step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: enabled
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: esg_enabled
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: supply_chain_enabled
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: custom_sources
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: executor
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


