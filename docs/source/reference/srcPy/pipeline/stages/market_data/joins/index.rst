srcPy.pipeline.stages.market_data.joins
=======================================

.. py:module:: srcPy.pipeline.stages.market_data.joins


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.joins.logger
   srcPy.pipeline.stages.market_data.joins.SOURCE_REGISTRY
   srcPy.pipeline.stages.market_data.joins.AGG_MAP
   srcPy.pipeline.stages.market_data.joins.JOIN_STEPS
   srcPy.pipeline.stages.market_data.joins.JOIN_CONFIGS


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.joins.JoinSpec
   srcPy.pipeline.stages.market_data.joins.MultiSourceJoinConfig
   srcPy.pipeline.stages.market_data.joins.MultiSourceJoinStep
   srcPy.pipeline.stages.market_data.joins.ResampleConfig
   srcPy.pipeline.stages.market_data.joins.ResampleStep


Functions
---------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.joins.build_join_steps


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:data:: SOURCE_REGISTRY
   :type:  dict[str, polars.LazyFrame]
   :value: Ellipsis


.. py:class:: JoinSpec(/, **data)

   Bases: :py:obj:`pydantic.BaseModel`


   join spec class.


   .. py:attribute:: source_name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: on
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: how
      :type:  str
      :value: Ellipsis



   .. py:attribute:: suffix
      :type:  str | None
      :value: Ellipsis



.. py:class:: MultiSourceJoinConfig(/, **data)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for multi source join.


   .. py:attribute:: joins
      :type:  list[JoinSpec]
      :value: Ellipsis



.. py:class:: MultiSourceJoinStep(config)

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.PipelineStep`


   multi source join step class.


   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(lf)


.. py:data:: AGG_MAP
   :type:  dict[str, Callable]
   :value: Ellipsis


.. py:class:: ResampleConfig(/, **data)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for resample.


   .. py:attribute:: freq
      :type:  str
      :value: Ellipsis



   .. py:attribute:: group_by
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: agg
      :type:  dict[str, str]
      :value: Ellipsis



   .. py:attribute:: timestamp_col
      :type:  str
      :value: Ellipsis



.. py:class:: ResampleStep(config)

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.PipelineStep`


   resample step class.


   .. py:attribute:: freq
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: group_by
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: agg
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: timestamp_col
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(lf)


.. py:data:: JOIN_STEPS
   :type:  dict[str, type[srcPy.pipeline.core.pipeline_core_base.PipelineStep]]
   :value: Ellipsis


.. py:data:: JOIN_CONFIGS
   :type:  dict[str, type[pydantic.BaseModel]]
   :value: Ellipsis


.. py:function:: build_join_steps(configs)

