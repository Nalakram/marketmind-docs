srcPy.preprocessor.graph.backends.registry
==========================================

.. py:module:: srcPy.preprocessor.graph.backends.registry


Attributes
----------

.. autoapisummary::

   srcPy.preprocessor.graph.backends.registry.logger


Functions
---------

.. autoapisummary::

   srcPy.preprocessor.graph.backends.registry.register
   srcPy.preprocessor.graph.backends.registry.get
   srcPy.preprocessor.graph.backends.registry.list_ops
   srcPy.preprocessor.graph.backends.registry.auto_register_from_utils


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:function:: register(backend, op, fn)

.. py:function:: get(backend, op)

.. py:function:: list_ops(backend = None)

.. py:function:: auto_register_from_utils()

