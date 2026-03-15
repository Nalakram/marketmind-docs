srcPy.preprocessor.api
======================

.. py:module:: srcPy.preprocessor.api


Attributes
----------

.. autoapisummary::

   srcPy.preprocessor.api.Backend


Classes
-------

.. autoapisummary::

   srcPy.preprocessor.api.Preprocessor
   srcPy.preprocessor.api.PlanSpec
   srcPy.preprocessor.api.ModelRegistry
   srcPy.preprocessor.api.Plan
   srcPy.preprocessor.api.PreprocessorBuilder


Functions
---------

.. autoapisummary::

   srcPy.preprocessor.api.merge_specs
   srcPy.preprocessor.api.resolve_models_in_ops
   srcPy.preprocessor.api.get_executor
   srcPy.preprocessor.api.run
   srcPy.preprocessor.api.stream
   srcPy.preprocessor.api.build_plan_from_spec
   srcPy.preprocessor.api.compile_plan


Module Contents
---------------

.. py:data:: Backend
   :type:  Any
   :value: Ellipsis


.. py:class:: Preprocessor(backend = 'polars')

   preprocessor class.


   .. py:attribute:: backend
      :type:  Any
      :value: Ellipsis



   .. py:method:: materialize(df, spec)


.. py:class:: PlanSpec

   plan spec class.


   .. py:attribute:: ops
      :type:  list[dict[str, Any]]
      :value: []



   .. py:attribute:: target
      :type:  dict[str, Any] | None
      :value: Ellipsis



   .. py:attribute:: sequence
      :type:  dict[str, Any] | None
      :value: Ellipsis



   .. py:attribute:: scaling
      :type:  dict[str, Any] | None
      :value: Ellipsis



   .. py:attribute:: meta
      :type:  dict[str, Any] | None
      :value: Ellipsis



.. py:function:: merge_specs(*specs)

.. py:class:: ModelRegistry

   model registry class.


   .. py:method:: register(name, obj)
      :classmethod:



   .. py:method:: get(name)
      :classmethod:



.. py:function:: resolve_models_in_ops(ops)

.. py:class:: Plan

   plan class.


   .. py:attribute:: ops
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: params
      :type:  dict[str, list[dict[str, Any]]]
      :value: Ellipsis



   .. py:attribute:: group_by
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: version
      :type:  str
      :value: Ellipsis



.. py:function:: get_executor(backend = 'auto')

.. py:function:: run(df, plan, *, backend = 'auto', optimize = None, pressure = None, **_ignored)

.. py:function:: stream(plan, *, backend = 'auto')

.. py:class:: PreprocessorBuilder(backend = 'auto')

   Builder for constructing preprocessor objects.


   .. py:method:: add_op(op_symbol, **params)


   .. py:method:: set_group_by(cols)


   .. py:method:: set_backend(backend)


   .. py:method:: from_dict(cfg)


   .. py:method:: build_plan()


   .. py:method:: build_runner()


   .. py:method:: add_dsl_op(op_symbol, backend_hint = None, **params)


   .. py:method:: add_sequence(*ops)


   .. py:method:: add_parallel(*builders)


   .. py:method:: add_transform(transform_name, **params)


.. py:function:: build_plan_from_spec(*args, **kwargs)

.. py:function:: compile_plan(*args, **kwargs)

