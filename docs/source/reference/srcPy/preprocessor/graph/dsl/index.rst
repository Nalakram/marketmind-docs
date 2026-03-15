srcPy.preprocessor.graph.dsl
============================

.. py:module:: srcPy.preprocessor.graph.dsl


Classes
-------

.. autoapisummary::

   srcPy.preprocessor.graph.dsl.BackendAwareOp
   srcPy.preprocessor.graph.dsl.OpFactory


Functions
---------

.. autoapisummary::

   srcPy.preprocessor.graph.dsl.op
   srcPy.preprocessor.graph.dsl.sequence
   srcPy.preprocessor.graph.dsl.parallel
   srcPy.preprocessor.graph.dsl.__rshift__
   srcPy.preprocessor.graph.dsl.__or__
   srcPy.preprocessor.graph.dsl.combine_ops


Module Contents
---------------

.. py:class:: BackendAwareOp(**params)

   Bases: :py:obj:`Op`


   backend aware op class.


   .. py:attribute:: backend_hint
      :type:  str | None
      :value: Ellipsis



   .. py:method:: to_ir()


.. py:class:: OpFactory

   Factory for creating op instances.


   .. py:method:: create(op_symbol, **params)
      :staticmethod:



.. py:function:: op(op_symbol, backend_hint = None, **params)

.. py:function:: sequence(*ops)

.. py:function:: parallel(*subgraphs)

.. py:function:: __rshift__(self, other)

.. py:function:: __or__(self, other)

.. py:function:: combine_ops(name, *sub_ops, backend_selector = ...)

