srcPy.preprocessor.graph.executor
=================================

.. py:module:: srcPy.preprocessor.graph.executor


Attributes
----------

.. autoapisummary::

   srcPy.preprocessor.graph.executor.logger
   srcPy.preprocessor.graph.executor.Engine


Classes
-------

.. autoapisummary::

   srcPy.preprocessor.graph.executor.Executor
   srcPy.preprocessor.graph.executor.PolarsExecutor
   srcPy.preprocessor.graph.executor.CuDFExecutor
   srcPy.preprocessor.graph.executor.ExecutorFactory


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:data:: Engine
   :type:  Any
   :value: Ellipsis


.. py:class:: Executor(backend, cache_size = 128)

   Bases: :py:obj:`abc.ABC`


   executor class.


   .. py:attribute:: backend
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: cache
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: lru_cache
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: execution_history
      :type:  list[dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: planner
      :type:  Any
      :value: Ellipsis



   .. py:method:: execute(plan, data, group_by)
      :abstractmethod:



   .. py:method:: evolve(threshold = 1.0)


.. py:class:: PolarsExecutor(engine_pref = 'auto')

   Bases: :py:obj:`Executor`


   polars executor class.


   .. py:attribute:: engine_pref
      :type:  Any
      :value: Ellipsis



   .. py:method:: execute(plan, data, group_by)


.. py:class:: CuDFExecutor(pool_size = '4GB')

   Bases: :py:obj:`Executor`


   cu df executor class.


   .. py:method:: execute(plan, data, group_by)


.. py:class:: ExecutorFactory

   Factory for creating executor instances.


   .. py:method:: register(backend, executor_cls)
      :classmethod:



   .. py:method:: create(backend = 'auto', **kwargs)
      :classmethod:



