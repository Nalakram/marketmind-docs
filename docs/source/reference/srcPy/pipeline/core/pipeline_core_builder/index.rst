srcPy.pipeline.core.pipeline_core_builder
=========================================

.. py:module:: srcPy.pipeline.core.pipeline_core_builder


Classes
-------

.. autoapisummary::

   srcPy.pipeline.core.pipeline_core_builder.PipelineBuilder
   srcPy.pipeline.core.pipeline_core_builder.Pipeline


Functions
---------

.. autoapisummary::

   srcPy.pipeline.core.pipeline_core_builder.choose_combo
   srcPy.pipeline.core.pipeline_core_builder.topo_order


Module Contents
---------------

.. py:function:: choose_combo(cfg, ctx, name = None)

.. py:function:: topo_order(steps, order_cfg)

.. py:class:: PipelineBuilder(stage, config = None)

   Builder for constructing pipeline objects.


   .. py:attribute:: stage
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: steps
      :type:  list[Any]
      :value: Ellipsis



   .. py:method:: for_stage(stage, config = None)
      :classmethod:



   .. py:method:: from_preset_and_params(preset, params)


   .. py:method:: add_steps(steps)


   .. py:method:: build()


   .. py:method:: validate_contracts()


.. py:class:: Pipeline(steps, config)

   pipeline class.


   .. py:attribute:: steps
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:method:: fit_transform(df)


