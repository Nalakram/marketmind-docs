srcPy.preprocessor.graph.expr
=============================

.. py:module:: srcPy.preprocessor.graph.expr


Classes
-------

.. autoapisummary::

   srcPy.preprocessor.graph.expr.ExprMeta
   srcPy.preprocessor.graph.expr.Expr
   srcPy.preprocessor.graph.expr.Column
   srcPy.preprocessor.graph.expr.Literal
   srcPy.preprocessor.graph.expr.OpExpr


Functions
---------

.. autoapisummary::

   srcPy.preprocessor.graph.expr.register_expr
   srcPy.preprocessor.graph.expr.expr_factory
   srcPy.preprocessor.graph.expr.register_builtin_builders


Module Contents
---------------

.. py:function:: register_expr(op, builder)

.. py:class:: ExprMeta

   Bases: :py:obj:`abc.ABCMeta`


   expr meta class.


.. py:class:: Expr(args = (), params = None)

   Bases: :py:obj:`abc.ABC`


   expr class.


   .. py:attribute:: op
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: args
      :type:  Sequence[Expr]
      :value: Ellipsis



   .. py:attribute:: params
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:method:: validate()


   .. py:method:: __add__(other)


   .. py:method:: __sub__(other)


   .. py:method:: __mul__(other)


   .. py:method:: __truediv__(other)


   .. py:method:: __neg__()


   .. py:method:: __pow__(other)


   .. py:method:: __radd__(other)


   .. py:method:: __rsub__(other)


   .. py:method:: __rmul__(other)


   .. py:method:: __rtruediv__(other)


   .. py:method:: __rpow__(other)


   .. py:method:: __hash__()


   .. py:method:: __eq__(other)


   .. py:method:: to_ir()
      :abstractmethod:



   .. py:method:: optimize()


.. py:class:: Column(name)

   Bases: :py:obj:`Expr`


   column class.


   .. py:attribute:: op
      :value: Ellipsis



   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:method:: validate()


   .. py:method:: to_ir()


.. py:class:: Literal(value)

   Bases: :py:obj:`Expr`


   literal class.


   .. py:attribute:: op
      :value: Ellipsis



   .. py:attribute:: value
      :type:  Any
      :value: Ellipsis



   .. py:method:: to_ir()


.. py:class:: OpExpr(op, args, params = None)

   Bases: :py:obj:`Expr`


   op expr class.


   .. py:attribute:: op
      :type:  Any
      :value: Ellipsis



   .. py:method:: to_ir()


   .. py:method:: optimize()


.. py:function:: expr_factory(op, args = (), **params)

.. py:function:: register_builtin_builders()

