srcPy.preprocessor.graph.factory
================================

.. py:module:: srcPy.preprocessor.graph.factory


Classes
-------

.. autoapisummary::

   srcPy.preprocessor.graph.factory.OpSpec


Functions
---------

.. autoapisummary::

   srcPy.preprocessor.graph.factory.register
   srcPy.preprocessor.graph.factory.register_alias
   srcPy.preprocessor.graph.factory.resolve_name
   srcPy.preprocessor.graph.factory.build_graph
   srcPy.preprocessor.graph.factory.registry_snapshot
   srcPy.preprocessor.graph.factory.register_builtin_ops


Module Contents
---------------

.. py:class:: OpSpec

   op spec class.


   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: params
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:function:: register(name, op_cls)

.. py:function:: register_alias(alias, target)

.. py:function:: resolve_name(name)

.. py:function:: build_graph(ops, params)

.. py:function:: registry_snapshot()

.. py:function:: register_builtin_ops()

