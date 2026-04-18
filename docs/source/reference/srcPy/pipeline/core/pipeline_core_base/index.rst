srcPy.pipeline.core.pipeline_core_base
======================================

.. py:module:: srcPy.pipeline.core.pipeline_core_base


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.core.pipeline_core_base.InT
   srcPy.pipeline.core.pipeline_core_base.OutT
   srcPy.pipeline.core.pipeline_core_base.Engine


Exceptions
----------

.. autoapisummary::

   srcPy.pipeline.core.pipeline_core_base.PipelineError
   srcPy.pipeline.core.pipeline_core_base.PipelineGraphError
   srcPy.pipeline.core.pipeline_core_base.PipelineConfigError
   srcPy.pipeline.core.pipeline_core_base.DataError
   srcPy.pipeline.core.pipeline_core_base.MissingDataError
   srcPy.pipeline.core.pipeline_core_base.InvalidSchemaError


Classes
-------

.. autoapisummary::

   srcPy.pipeline.core.pipeline_core_base.StepRegistry
   srcPy.pipeline.core.pipeline_core_base.ErrorCode
   srcPy.pipeline.core.pipeline_core_base.DataSource
   srcPy.pipeline.core.pipeline_core_base.PipelineStep
   srcPy.pipeline.core.pipeline_core_base.CompositeStep
   srcPy.pipeline.core.pipeline_core_base.CleaningStep


Module Contents
---------------

.. py:class:: StepRegistry

   Bases: :py:obj:`dict`


   step registry class.


   .. py:method:: register(name, cls)


.. py:data:: InT

.. py:data:: OutT

.. py:data:: Engine
   :type:  Any
   :value: Ellipsis


.. py:exception:: PipelineError

   Bases: :py:obj:`Exception`


   Exception raised when pipeline occurs.


   .. py:attribute:: code
      :type:  str
      :value: Ellipsis



   .. py:method:: to_dict()


.. py:exception:: PipelineGraphError

   Bases: :py:obj:`PipelineError`


   Exception raised when pipeline graph occurs.


   .. py:attribute:: code
      :type:  str
      :value: Ellipsis



.. py:exception:: PipelineConfigError

   Bases: :py:obj:`PipelineError`


   Exception raised when pipeline config occurs.


   .. py:attribute:: code
      :type:  str
      :value: Ellipsis



.. py:class:: ErrorCode(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   error code class.


   .. py:attribute:: MISSING_DATA
      :value: 'MISSING_DATA'



   .. py:attribute:: INVALID_SCHEMA
      :value: 'INVALID_SCHEMA'



   .. py:attribute:: OUTLIER_DETECTED
      :value: 'OUTLIER_DETECTED'



   .. py:attribute:: DRIFT_DETECTED
      :value: 'DRIFT_DETECTED'



   .. py:attribute:: PROCESSING_FAILURE
      :value: 'PROCESSING_FAILURE'



   .. py:attribute:: RESOURCE_EXHAUSTED
      :value: 'RESOURCE_EXHAUSTED'



.. py:exception:: DataError(message, code, details = None)

   Bases: :py:obj:`Exception`


   Exception raised when data occurs.


   .. py:attribute:: message
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: code
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: details
      :type:  Any
      :value: Ellipsis



   .. py:method:: to_dict()


.. py:exception:: MissingDataError(message, code, details = None)

   Bases: :py:obj:`DataError`


   Exception raised when data occurs.


.. py:exception:: InvalidSchemaError(message, code, details = None)

   Bases: :py:obj:`DataError`


   Exception raised when data occurs.


.. py:class:: DataSource(config)

   Bases: :py:obj:`abc.ABC`


   data source class.


   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:method:: load_data(*args, **kwargs)
      :abstractmethod:

      :async:



   .. py:method:: stream_data()
      :async:



.. py:class:: PipelineStep(name = None, **_)

   Bases: :py:obj:`abc.ABC`, :py:obj:`Generic`\ [\ :py:obj:`InT`\ , :py:obj:`OutT`\ ]


   pipeline step class.


   .. py:attribute:: STEP_NAME
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: STEP_VERSION
      :type:  str
      :value: Ellipsis



   .. py:attribute:: requires
      :type:  set[str]
      :value: Ellipsis



   .. py:attribute:: produces
      :type:  set[str]
      :value: Ellipsis



   .. py:attribute:: preferred_engine
      :type:  Engine | None
      :value: Ellipsis



   .. py:attribute:: name
      :type:  Any
      :value: Ellipsis



   .. py:method:: execute(data, context)
      :async:



   .. py:method:: apply_batch(lf, ctx)


   .. py:method:: apply_batch_pandas(df, ctx)


   .. py:method:: apply_stream(aiter, ctx)
      :async:



   .. py:method:: compose(*steps)
      :classmethod:



   .. py:method:: __rshift__(other)


.. py:class:: CompositeStep(steps, **kwargs)

   Bases: :py:obj:`PipelineStep`


   composite step class.


   .. py:attribute:: steps
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply_batch(lf, ctx)


.. py:class:: CleaningStep(name = None, **_)

   Bases: :py:obj:`PipelineStep`


   cleaning step class.


   .. py:method:: apply(df)
      :abstractmethod:



   .. py:method:: apply_batch(lf, ctx)


