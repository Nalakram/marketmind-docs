srcPy.pipeline.stages.market_data.sources.file
==============================================

.. py:module:: srcPy.pipeline.stages.market_data.sources.file


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.sources.file.FileSource


Module Contents
---------------

.. py:class:: FileSource(config)

   Bases: :py:obj:`DataSource`


   file source class.


   .. py:attribute:: file_path
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: format
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: tail
      :type:  bool
      :value: Ellipsis



   .. py:method:: get_historical(symbol, start, end, *, eager = False)


   .. py:method:: get_realtime(symbol, *, interval = 60.0)
      :async:



