srcPy.pipeline.core.pipeline_core_context
=========================================

.. py:module:: srcPy.pipeline.core.pipeline_core_context


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.core.pipeline_core_context.TimeFreq


Classes
-------

.. autoapisummary::

   srcPy.pipeline.core.pipeline_core_context.PipelineContext


Module Contents
---------------

.. py:data:: TimeFreq
   :type:  Any
   :value: Ellipsis


.. py:class:: PipelineContext

   pipeline context class.


   .. py:attribute:: frequency
      :type:  TimeFreq
      :value: Ellipsis



   .. py:attribute:: asset_class
      :type:  str
      :value: Ellipsis



   .. py:attribute:: latency
      :type:  Literal['ultra', 'low', 'batch']
      :value: Ellipsis



   .. py:attribute:: streaming
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: time_col
      :type:  str
      :value: Ellipsis



   .. py:attribute:: df
      :type:  srcPy.utils.optional_imports.pl.DataFrame | srcPy.utils.optional_imports.pl.LazyFrame | srcPy.utils.optional_imports.pd.DataFrame | None
      :value: Ellipsis



   .. py:attribute:: assume_sorted
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: sample
      :type:  int
      :value: Ellipsis



   .. py:attribute:: backend
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: executor
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: optimize
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: cache
      :type:  bool
      :value: Ellipsis



   .. py:method:: as_lazy()


   .. py:method:: infer_frequency()


   .. py:method:: refine(**kwargs)


