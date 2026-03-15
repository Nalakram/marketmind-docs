srcPy.preprocessor.graph.graph
==============================

.. py:module:: srcPy.preprocessor.graph.graph


Classes
-------

.. autoapisummary::

   srcPy.preprocessor.graph.graph.Node
   srcPy.preprocessor.graph.graph.SimpleNode
   srcPy.preprocessor.graph.graph.FusedNode
   srcPy.preprocessor.graph.graph.Graph


Functions
---------

.. autoapisummary::

   srcPy.preprocessor.graph.graph.register_node_factory
   srcPy.preprocessor.graph.graph.serialize
   srcPy.preprocessor.graph.graph.deserialize


Module Contents
---------------

.. py:class:: Node(op)

   Bases: :py:obj:`abc.ABC`


   node class.


   .. py:attribute:: op
      :type:  srcPy.preprocessor.graph.ops.Op
      :value: Ellipsis



   .. py:attribute:: inputs
      :type:  list[Node]
      :value: Ellipsis



   .. py:attribute:: outputs
      :type:  list[Node]
      :value: Ellipsis



   .. py:method:: __hash__()


   .. py:method:: __eq__(other)


   .. py:method:: to_ir()
      :abstractmethod:



.. py:class:: SimpleNode(op)

   Bases: :py:obj:`Node`


   simple node class.


   .. py:method:: to_ir()


.. py:class:: FusedNode(sub_ops, fused_kind)

   Bases: :py:obj:`Node`


   fused node class.


   .. py:attribute:: sub_ops
      :type:  list[srcPy.preprocessor.graph.ops.Op]
      :value: Ellipsis



   .. py:method:: to_ir()


.. py:function:: register_node_factory(key, factory)

.. py:class:: Graph

   graph class.


   .. py:attribute:: nodes
      :type:  list[Node]
      :value: Ellipsis



   .. py:attribute:: col_providers
      :type:  dict[str, list[Node]]
      :value: Ellipsis



   .. py:attribute:: input_requires
      :type:  set[str]
      :value: Ellipsis



   .. py:method:: add_op(op)


   .. py:method:: merge(other)


   .. py:method:: optimize()


   .. py:method:: topological_sort()


   .. py:method:: has_cycle()


   .. py:method:: shortest_path(start, end)


   .. py:method:: connected_components()


.. py:function:: serialize(graph)

.. py:function:: deserialize(data)

