srcPy.pipeline.stages.market_data.transforms
============================================

.. py:module:: srcPy.pipeline.stages.market_data.transforms


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.transforms.logger
   srcPy.pipeline.stages.market_data.transforms.TRANSFORM_STEPS
   srcPy.pipeline.stages.market_data.transforms.TRANSFORM_CONFIGS


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.transforms.ColumnRenameConfig
   srcPy.pipeline.stages.market_data.transforms.ColumnRenameStep
   srcPy.pipeline.stages.market_data.transforms.TypeCastConfig
   srcPy.pipeline.stages.market_data.transforms.TypeCastStep


Functions
---------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.transforms.build_steps
   srcPy.pipeline.stages.market_data.transforms.build_transform_steps


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: ColumnRenameConfig(/, **data)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for column rename.


   .. py:attribute:: mapping
      :type:  dict[str, str]
      :value: Ellipsis



.. py:class:: ColumnRenameStep(config)

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.PipelineStep`


   column rename step class.


   .. py:attribute:: mapping
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(lf)


.. py:class:: TypeCastConfig(/, **data)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for type cast.


   .. py:attribute:: model_config
      :type:  Any
      :value: Ellipsis


      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: dtypes
      :type:  dict[str, polars.DataType]
      :value: Ellipsis



.. py:class:: TypeCastStep(config)

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.PipelineStep`


   type cast step class.


   .. py:attribute:: dtypes
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(lf)


.. py:data:: TRANSFORM_STEPS
   :type:  dict[str, type[srcPy.pipeline.core.pipeline_core_base.PipelineStep]]
   :value: Ellipsis


.. py:data:: TRANSFORM_CONFIGS
   :type:  dict[str, type[pydantic.BaseModel]]
   :value: Ellipsis


.. py:function:: build_steps(configs, step_registry, config_registry)

.. py:function:: build_transform_steps(configs)

