srcPy.pipeline.stages.market_data.sources.influxdb
==================================================

.. py:module:: srcPy.pipeline.stages.market_data.sources.influxdb


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.sources.influxdb.InfluxDBSource


Module Contents
---------------

.. py:class:: InfluxDBSource(config)

   Bases: :py:obj:`DataSource`


   influx db source class.


   .. py:attribute:: client
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: query_api
      :type:  influxdb_client.client.query_api.QueryApi
      :value: Ellipsis



   .. py:attribute:: bucket
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: measurement
      :type:  Any
      :value: Ellipsis



   .. py:method:: get_historical(symbol, start, end, *, eager = False)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = 60.0)
      :async:



   .. py:method:: __aexit__(exc_type, exc_val, exc_tb)
      :async:



