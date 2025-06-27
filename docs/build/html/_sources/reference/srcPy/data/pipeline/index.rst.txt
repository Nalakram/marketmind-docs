srcPy.data.pipeline
===================

.. py:module:: srcPy.data.pipeline


Attributes
----------

.. autoapisummary::

   srcPy.data.pipeline.logger


Classes
-------

.. autoapisummary::

   srcPy.data.pipeline.DataPipelineOrchestrator


Module Contents
---------------

.. py:data:: logger
   :type:  _typeshed.Incomplete

.. py:class:: DataPipelineOrchestrator(config = None)

   .. py:attribute:: config
      :type:  _typeshed.Incomplete


   .. py:attribute:: market_manager
      :type:  _typeshed.Incomplete


   .. py:attribute:: cleaner
      :type:  _typeshed.Incomplete


   .. py:attribute:: preprocessor
      :type:  _typeshed.Incomplete


   .. py:method:: fetch_data(source, **kwargs)


   .. py:method:: fetch_multiple_data(symbols, source, cache_dir = None, **kwargs)


   .. py:method:: run_pipeline(df, cache_dir = None)


   .. py:method:: process(source, **kwargs)


   .. py:method:: process_multiple(symbols, source, cache_dir = None, **kwargs)


