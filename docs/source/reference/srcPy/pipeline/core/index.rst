srcPy.pipeline.core
===================

.. py:module:: srcPy.pipeline.core


Submodules
----------

.. toctree::
   :maxdepth: 1

   /reference/srcPy/pipeline/core/pipeline_core_base/index
   /reference/srcPy/pipeline/core/pipeline_core_builder/index
   /reference/srcPy/pipeline/core/pipeline_core_context/index
   /reference/srcPy/pipeline/core/pipeline_core_metrics/index
   /reference/srcPy/pipeline/core/pipeline_core_plugins/index
   /reference/srcPy/pipeline/core/pipeline_core_registry/index


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.core.ERROR_COUNTER
   srcPy.pipeline.core.STEP_EXECUTION_TIME


Exceptions
----------

.. autoapisummary::

   srcPy.pipeline.core.DataError


Classes
-------

.. autoapisummary::

   srcPy.pipeline.core.ErrorCode
   srcPy.pipeline.core.PipelineStep
   srcPy.pipeline.core.Pipeline
   srcPy.pipeline.core.PipelineBuilder
   srcPy.pipeline.core.PipelineContext
   srcPy.pipeline.core.AsyncMLflowLogger
   srcPy.pipeline.core.StepRegistry


Functions
---------

.. autoapisummary::

   srcPy.pipeline.core.track_step_execution
   srcPy.pipeline.core.discover_all_plugins
   srcPy.pipeline.core.load_stage_plugins


Package Contents
----------------

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


.. py:class:: ErrorCode

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


.. py:class:: Pipeline(steps, config)

   pipeline class.


   .. py:attribute:: steps
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:method:: fit_transform(df)


.. py:class:: PipelineBuilder(stage, config = None)

   Builder for constructing pipeline objects.


   .. py:attribute:: stage
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: steps
      :type:  list[Any]
      :value: Ellipsis



   .. py:method:: for_stage(stage, config = None)
      :classmethod:



   .. py:method:: from_preset_and_params(preset, params)


   .. py:method:: add_steps(steps)


   .. py:method:: build()


   .. py:method:: validate_contracts()


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


.. py:class:: AsyncMLflowLogger

   async m lflow logger class.


   .. py:method:: log_metrics(metrics, *, step = None)
      :async:



   .. py:method:: log_params(params)
      :async:



   .. py:method:: set_experiment(name)
      :async:



   .. py:method:: start_run(*, run_name = None, nested = True, tags = None)
      :async:



   .. py:method:: end_run()
      :async:



   .. py:method:: log_artifact(local_path, *, artifact_path = None)
      :async:



.. py:data:: ERROR_COUNTER
   :type:  Any
   :value: Ellipsis


.. py:data:: STEP_EXECUTION_TIME
   :type:  Any
   :value: Ellipsis


.. py:function:: track_step_execution(step_name, *, stage = 'unknown', engine = 'unknown')

.. py:function:: discover_all_plugins(stages, group_prefix = 'marketmind')

.. py:function:: load_stage_plugins(stage, group_prefix = 'marketmind')

.. py:class:: StepRegistry

   step registry class.


   .. py:method:: register(*args, override = False)
      :classmethod:



   .. py:method:: get(stage, name)
      :classmethod:



   .. py:method:: load_plugins(entry_point_group, stage)
      :classmethod:



