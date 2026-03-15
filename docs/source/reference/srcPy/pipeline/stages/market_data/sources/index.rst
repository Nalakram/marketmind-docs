srcPy.pipeline.stages.market_data.sources
=========================================

.. py:module:: srcPy.pipeline.stages.market_data.sources


Submodules
----------

.. toctree::
   :maxdepth: 1

   /reference/srcPy/pipeline/stages/market_data/sources/alpha_vantage/index
   /reference/srcPy/pipeline/stages/market_data/sources/base/index
   /reference/srcPy/pipeline/stages/market_data/sources/coingecko/index
   /reference/srcPy/pipeline/stages/market_data/sources/file/index
   /reference/srcPy/pipeline/stages/market_data/sources/fred/index
   /reference/srcPy/pipeline/stages/market_data/sources/ibkr/index
   /reference/srcPy/pipeline/stages/market_data/sources/influxdb/index
   /reference/srcPy/pipeline/stages/market_data/sources/quandl/index


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.sources.DataSource


Functions
---------

.. autoapisummary::

   srcPy.pipeline.stages.market_data.sources.register_source
   srcPy.pipeline.stages.market_data.sources.get_registry


Package Contents
----------------

.. py:function:: register_source(name)

.. py:function:: get_registry()

.. py:class:: DataSource

   data source class.


   .. py:method:: get_historical(*args, **kwargs)
      :async:



