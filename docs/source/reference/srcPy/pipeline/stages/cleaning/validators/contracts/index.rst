srcPy.pipeline.stages.cleaning.validators.contracts
===================================================

.. py:module:: srcPy.pipeline.stages.cleaning.validators.contracts


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.validators.contracts.Bar
   srcPy.pipeline.stages.cleaning.validators.contracts.Tick
   srcPy.pipeline.stages.cleaning.validators.contracts.MarketDataFrameSchema


Module Contents
---------------

.. py:class:: Bar

   bar class.


   .. py:attribute:: timestamp
      :type:  polars.Datetime
      :value: Ellipsis



   .. py:attribute:: open
      :type:  float
      :value: Ellipsis



   .. py:attribute:: high
      :type:  float
      :value: Ellipsis



   .. py:attribute:: low
      :type:  float
      :value: Ellipsis



   .. py:attribute:: close
      :type:  float
      :value: Ellipsis



   .. py:attribute:: volume
      :type:  float
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  dict[str, Any] | None


.. py:class:: Tick

   tick class.


   .. py:attribute:: timestamp
      :type:  polars.Datetime
      :value: Ellipsis



   .. py:attribute:: price
      :type:  float
      :value: Ellipsis



   .. py:attribute:: size
      :type:  float
      :value: Ellipsis



   .. py:attribute:: side
      :type:  str
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  dict[str, Any] | None


.. py:class:: MarketDataFrameSchema

   market data frame schema class.


   .. py:attribute:: required_columns
      :type:  dict[str, polars.DataType]


   .. py:attribute:: optional_columns
      :type:  dict[str, polars.DataType]


   .. py:attribute:: strict
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: unknown_ok
      :type:  bool
      :value: Ellipsis



   .. py:method:: validate(df, strict = None)


