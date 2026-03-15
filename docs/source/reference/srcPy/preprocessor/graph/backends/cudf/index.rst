srcPy.preprocessor.graph.backends.cudf
======================================

.. py:module:: srcPy.preprocessor.graph.backends.cudf


Attributes
----------

.. autoapisummary::

   srcPy.preprocessor.graph.backends.cudf.logger


Classes
-------

.. autoapisummary::

   srcPy.preprocessor.graph.backends.cudf.CuDFExecutor


Functions
---------

.. autoapisummary::

   srcPy.preprocessor.graph.backends.cudf.robust_scaler_cudf


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:function:: robust_scaler_cudf(ir, gdf, group_by=None, **_)

.. py:class:: CuDFExecutor(*, pool_size = '4GB', to_torch = False)

   Bases: :py:obj:`srcPy.preprocessor.graph.executor.Executor`


   cu df executor class.


   .. py:attribute:: to_torch
      :type:  Any
      :value: Ellipsis



   .. py:method:: read_parquet(path, columns=None, byte_range=None)


   .. py:method:: execute(compiled_plan, df)


