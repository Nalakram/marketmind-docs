srcPy.data.dataprep_orchestrator
================================

.. py:module:: srcPy.data.dataprep_orchestrator


Attributes
----------

.. autoapisummary::

   srcPy.data.dataprep_orchestrator.pd
   srcPy.data.dataprep_orchestrator.pl
   srcPy.data.dataprep_orchestrator.dd
   srcPy.data.dataprep_orchestrator.np
   srcPy.data.dataprep_orchestrator.yaml
   srcPy.data.dataprep_orchestrator.pynvml
   srcPy.data.dataprep_orchestrator.psutil
   srcPy.data.dataprep_orchestrator.BackendLiteral
   srcPy.data.dataprep_orchestrator.logger
   srcPy.data.dataprep_orchestrator.run_cfg


Exceptions
----------

.. autoapisummary::

   srcPy.data.dataprep_orchestrator.DataPrepError
   srcPy.data.dataprep_orchestrator.ConfigError
   srcPy.data.dataprep_orchestrator.DataValidationError


Classes
-------

.. autoapisummary::

   srcPy.data.dataprep_orchestrator.DataFrameAdapter
   srcPy.data.dataprep_orchestrator.ConfigProxy
   srcPy.data.dataprep_orchestrator.BackendManager
   srcPy.data.dataprep_orchestrator.Evolver
   srcPy.data.dataprep_orchestrator.OrchestratorConfig
   srcPy.data.dataprep_orchestrator.DataPrepOrchestrator
   srcPy.data.dataprep_orchestrator.Cache


Functions
---------

.. autoapisummary::

   srcPy.data.dataprep_orchestrator.expand_grid
   srcPy.data.dataprep_orchestrator.stage
   srcPy.data.dataprep_orchestrator.run_dataprep
   srcPy.data.dataprep_orchestrator.run_dataprep_from_path


Module Contents
---------------

.. py:data:: pd
   :type:  Any
   :value: Ellipsis


.. py:data:: pl
   :type:  Any
   :value: Ellipsis


.. py:data:: dd
   :type:  Any
   :value: Ellipsis


.. py:data:: np
   :type:  Any
   :value: Ellipsis


.. py:data:: yaml
   :type:  Any
   :value: Ellipsis


.. py:data:: pynvml
   :type:  Any
   :value: Ellipsis


.. py:data:: psutil
   :type:  Any
   :value: Ellipsis


.. py:data:: BackendLiteral
   :type:  Any
   :value: Ellipsis


.. py:function:: expand_grid(base, constraints = None)

.. py:function:: stage(name = None, timeout_s = None)

.. py:class:: DataFrameAdapter(df)

   Adapter for data frame interface.


   .. py:attribute:: df
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: is_polars
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: is_pandas
      :type:  Any
      :value: Ellipsis



   .. py:property:: shape


   .. py:property:: columns


   .. py:method:: hash()


.. py:class:: ConfigProxy(data)

   config proxy class.


   .. py:method:: __getattr__(key)


   .. py:method:: get(path, default=None)


.. py:class:: BackendManager

   Manages backend resources and operations.


   .. py:attribute:: HAS_POLARS
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: HAS_PANDAS
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: HAS_DASK
      :type:  Any
      :value: Ellipsis



   .. py:method:: require_polars()
      :classmethod:



.. py:class:: Evolver(cache, version_tag, code_id)

   evolver class.


   .. py:attribute:: cache
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: version_tag
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: code_id
      :type:  Any
      :value: Ellipsis



   .. py:method:: load(context_hash)


   .. py:method:: save(context_hash, trials)


   .. py:method:: shrink_grid(grid, prior_trials, quantile = 0.4)


.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:data:: run_cfg
   :type:  Any
   :value: Ellipsis


.. py:exception:: DataPrepError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: ConfigError

   Bases: :py:obj:`DataPrepError`


   Common base class for all non-exit exceptions.


.. py:exception:: DataValidationError

   Bases: :py:obj:`DataPrepError`


   Common base class for all non-exit exceptions.


.. py:class:: OrchestratorConfig

   Configuration for orchestrator.


   .. py:attribute:: per_symbol_parallelism
      :type:  int | str
      :value: Ellipsis



   .. py:attribute:: gpu_slots
      :type:  int | str
      :value: Ellipsis



   .. py:attribute:: lazy
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: date_chunk_size
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: cache_version_tag
      :type:  str
      :value: Ellipsis



   .. py:attribute:: cache_checkpoints
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: search_mode
      :type:  str
      :value: Ellipsis



   .. py:attribute:: n_trials
      :type:  int
      :value: Ellipsis



   .. py:attribute:: metric_name
      :type:  str
      :value: Ellipsis



.. py:class:: DataPrepOrchestrator(run_cfg, cache = None, backtest_metric = None, entry_point_groups = None)

   data prep orchestrator class.


   .. py:attribute:: run_id
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: cfg
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: run_cfg
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: run_cfg_raw
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: code_id
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: ocfg
      :type:  OrchestratorConfig
      :value: Ellipsis



   .. py:attribute:: cache
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: backtest_metric
      :type:  Callable[[Any, Any, Mapping[str, Any], Mapping[str, Any]], float] | None
      :value: Ellipsis



   .. py:attribute:: expected_columns
      :type:  Any
      :value: Ellipsis



   .. py:method:: run()


   .. py:method:: preprocess_multi_symbol(clean_df, preset, params)


   .. py:method:: adaptive_map(fn, items, kind = 'auto', max_workers = None)


.. py:function:: run_dataprep(run_cfg, backtest_metric = None)

.. py:function:: run_dataprep_from_path(run_cfg_path, backtest_metric)

.. py:class:: Cache

   cache class.


   .. py:method:: save_df(key, df)


