srcPy.data.base
===============

.. py:module:: srcPy.data.base


Attributes
----------

.. autoapisummary::

   srcPy.data.base.logger


Classes
-------

.. autoapisummary::

   srcPy.data.base.AbstractAPIDataManager


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: AbstractAPIDataManager(config)

   Manages abstract api data resources and operations.


   .. py:attribute:: registry
      :type:  dict[str, type[srcPy.pipeline.stages.market_data.sources.base.APIDataSource]]
      :value: Ellipsis



   .. py:method:: __init_subclass__(**kwargs)
      :classmethod:



   .. py:method:: register(source_type)
      :classmethod:



   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: sources
      :type:  dict[str, srcPy.pipeline.stages.market_data.sources.base.APIDataSource]
      :value: Ellipsis



   .. py:method:: add_source(source_type, source)


   .. py:method:: load_data(query, source_name = None)
      :async:



