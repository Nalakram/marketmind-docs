srcPy.preprocessor.graph.ops
============================

.. py:module:: srcPy.preprocessor.graph.ops


Classes
-------

.. autoapisummary::

   srcPy.preprocessor.graph.ops.OpKind
   srcPy.preprocessor.graph.ops.Op
   srcPy.preprocessor.graph.ops.ElementwiseOp
   srcPy.preprocessor.graph.ops.RollingOp
   srcPy.preprocessor.graph.ops.SequenceOp
   srcPy.preprocessor.graph.ops.ScalingOp
   srcPy.preprocessor.graph.ops.ExternalOp


Module Contents
---------------

.. py:class:: OpKind

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   op kind class.


   .. py:attribute:: elementwise
      :value: 'elementwise'



   .. py:attribute:: rolling
      :value: 'rolling'



   .. py:attribute:: sequence
      :value: 'sequence'



   .. py:attribute:: scaling
      :value: 'scaling'



   .. py:attribute:: external
      :value: 'external'



.. py:class:: Op(**params)

   Bases: :py:obj:`abc.ABC`


   op class.


   .. py:attribute:: NAME
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: KIND
      :type:  OpKind
      :value: Ellipsis



   .. py:attribute:: params
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:property:: name
      :type: str



   .. py:method:: validate_params()


   .. py:property:: requires
      :type: set[str]



   .. py:property:: provides
      :type: set[str]



   .. py:method:: is_fittable()


   .. py:method:: state_dict()


   .. py:method:: load_state_dict(state)


   .. py:method:: clone()


   .. py:method:: to_ir()
      :abstractmethod:



.. py:class:: ElementwiseOp(**params)

   Bases: :py:obj:`Op`


   elementwise op class.


   .. py:attribute:: KIND
      :type:  Any
      :value: Ellipsis



   .. py:method:: to_ir()


.. py:class:: RollingOp(**params)

   Bases: :py:obj:`Op`


   rolling op class.


   .. py:attribute:: KIND
      :type:  Any
      :value: Ellipsis



   .. py:method:: to_ir()


.. py:class:: SequenceOp(**params)

   Bases: :py:obj:`Op`


   sequence op class.


   .. py:attribute:: KIND
      :type:  Any
      :value: Ellipsis



   .. py:method:: to_ir()


.. py:class:: ScalingOp(**params)

   Bases: :py:obj:`Op`


   scaling op class.


   .. py:attribute:: KIND
      :type:  Any
      :value: Ellipsis



   .. py:method:: is_fittable()


   .. py:method:: to_ir()


.. py:class:: ExternalOp(**params)

   Bases: :py:obj:`Op`


   external op class.


   .. py:attribute:: KIND
      :type:  Any
      :value: Ellipsis



   .. py:method:: to_ir()


