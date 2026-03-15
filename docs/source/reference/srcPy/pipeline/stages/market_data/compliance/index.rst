srcPy.pipeline.stages.market_data.compliance
============================================

.. py:module:: srcPy.pipeline.stages.market_data.compliance


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.compliance.logger
   srcPy.pipeline.stages.market_data.compliance.COMPLIANCE_STEPS
   srcPy.pipeline.stages.market_data.compliance.COMPLIANCE_CONFIGS


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.compliance.AnonymizationConfig
   srcPy.pipeline.stages.market_data.compliance.DataAnonymizationStep
   srcPy.pipeline.stages.market_data.compliance.RegulatoryFilterConfig
   srcPy.pipeline.stages.market_data.compliance.RegulatoryFilterStep


Functions
---------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.compliance.get_hash_func
   srcPy.pipeline.stages.market_data.compliance.build_compliance_steps


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: AnonymizationConfig(/, **data)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for anonymization.


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: sensitive_columns
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: hash_algorithm
      :type:  str
      :value: Ellipsis



   .. py:attribute:: salt
      :type:  str | None
      :value: Ellipsis



.. py:function:: get_hash_func(algo, salt = None)

.. py:class:: DataAnonymizationStep(config)

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.PipelineStep`


   data anonymization step class.


   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: hasher
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(lf)


.. py:class:: RegulatoryFilterConfig(/, **data)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for regulatory filter.


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: restricted_symbols
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: min_volume_threshold
      :type:  float | None
      :value: Ellipsis



.. py:class:: RegulatoryFilterStep(config)

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.PipelineStep`


   regulatory filter step class.


   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(lf)


.. py:data:: COMPLIANCE_STEPS
   :type:  dict[str, type[srcPy.pipeline.core.pipeline_core_base.PipelineStep]]
   :value: Ellipsis


.. py:data:: COMPLIANCE_CONFIGS
   :type:  dict[str, type[pydantic.BaseModel]]
   :value: Ellipsis


.. py:function:: build_compliance_steps(configs)

