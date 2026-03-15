srcPy.pipeline.stages.cleaning.core.builder
===========================================

.. py:module:: srcPy.pipeline.stages.cleaning.core.builder


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.core.builder.PipelineBuilder


Functions
---------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.core.builder.choose_combo
   srcPy.pipeline.stages.cleaning.core.builder.topo_order


Module Contents
---------------

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


.. py:function:: choose_combo(cfg, ctx, name = None)

.. py:function:: topo_order(steps, order_cfg)

