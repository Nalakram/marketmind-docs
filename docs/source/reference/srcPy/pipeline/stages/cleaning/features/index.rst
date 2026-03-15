srcPy.pipeline.stages.cleaning.features
=======================================

.. py:module:: srcPy.pipeline.stages.cleaning.features


Submodules
----------

.. toctree::
   :maxdepth: 1

   /reference/srcPy/pipeline/stages/cleaning/features/altdata/index
   /reference/srcPy/pipeline/stages/cleaning/features/calendar/index
   /reference/srcPy/pipeline/stages/cleaning/features/macro/index
   /reference/srcPy/pipeline/stages/cleaning/features/sentiment/index
   /reference/srcPy/pipeline/stages/cleaning/features/technical/index


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.features.logger
   srcPy.pipeline.stages.cleaning.features.feature_steps


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.features.AlternativeDataNormalizerStep
   srcPy.pipeline.stages.cleaning.features.GlobalCalendarNormalizerStep
   srcPy.pipeline.stages.cleaning.features.TimeZoneNormalizerStep
   srcPy.pipeline.stages.cleaning.features.EconomicIndicatorNormalizerStep
   srcPy.pipeline.stages.cleaning.features.AdvancedSentimentExtractor
   srcPy.pipeline.stages.cleaning.features.SentimentExtractor
   srcPy.pipeline.stages.cleaning.features.ATRNormalizerStep
   srcPy.pipeline.stages.cleaning.features.IncrementalMACDStep
   srcPy.pipeline.stages.cleaning.features.IncrementalRSIStep
   srcPy.pipeline.stages.cleaning.features.MACDNormalizerStep
   srcPy.pipeline.stages.cleaning.features.RSINormalizerStep
   srcPy.pipeline.stages.cleaning.features.VWAPNormalizerStep
   srcPy.pipeline.stages.cleaning.features.StepRegistry


Functions
---------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.features.get_logger


Package Contents
----------------

.. py:class:: AlternativeDataNormalizerStep(mlflow_logger, enabled, esg_enabled = False, supply_chain_enabled = False, custom_sources = None)

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.CleaningStep`


   alternative data normalizer step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: enabled
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: esg_enabled
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: supply_chain_enabled
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: custom_sources
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: executor
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


.. py:class:: GlobalCalendarNormalizerStep(mlflow_logger, countries, day_of_week = True, is_holiday = True, timestamp_col = 'timestamp')

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.CleaningStep`


   global calendar normalizer step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: countries
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: day_of_week
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: is_holiday
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: timestamp_col
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


.. py:class:: TimeZoneNormalizerStep(mlflow_logger, target_tz = 'UTC', timestamp_col = 'timestamp')

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.CleaningStep`


   time zone normalizer step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: target_tz
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: timestamp_col
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


.. py:class:: EconomicIndicatorNormalizerStep(mlflow_logger, enabled, indicators, timestamp_col = 'timestamp')

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.CleaningStep`


   economic indicator normalizer step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: enabled
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: indicators
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: timestamp_col
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


.. py:class:: AdvancedSentimentExtractor(mlflow_logger, enabled, text_col = 'text', analyzer = 'finbert')

   Bases: :py:obj:`BaseSentimentExtractor`


   advanced sentiment extractor class.


   .. py:attribute:: model
      :type:  Any
      :value: Ellipsis



.. py:class:: SentimentExtractor(mlflow_logger, enabled, text_col = 'text')

   Bases: :py:obj:`BaseSentimentExtractor`


   sentiment extractor class.


   .. py:attribute:: model
      :type:  Any
      :value: Ellipsis



.. py:class:: ATRNormalizerStep(mlflow_logger, enabled, window, fillna_method = 'ffill')

   Bases: :py:obj:`BaseTechnicalIndicatorStep`


   atr normalizer step class.


.. py:class:: IncrementalMACDStep(mlflow_logger, fast = 12, slow = 26, signal = 9)

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.CleaningStep`


   incremental macd step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: macd
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


.. py:class:: IncrementalRSIStep(mlflow_logger, window)

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.CleaningStep`


   incremental rsi step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: rsi
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


.. py:class:: MACDNormalizerStep(mlflow_logger, enabled, fast = 12, slow = 26, signal = 9, fillna_method = 'ffill')

   Bases: :py:obj:`BaseTechnicalIndicatorStep`


   macd normalizer step class.


   .. py:attribute:: fast
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: slow
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: signal
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


.. py:class:: RSINormalizerStep(mlflow_logger, enabled, window, fillna_method = 'ffill')

   Bases: :py:obj:`BaseTechnicalIndicatorStep`


   rsi normalizer step class.


.. py:class:: VWAPNormalizerStep(mlflow_logger, enabled, window, fillna_method = 'ffill')

   Bases: :py:obj:`BaseTechnicalIndicatorStep`


   vwap normalizer step class.


.. py:function:: get_logger(name = None)

.. py:class:: StepRegistry

   Bases: :py:obj:`dict`


   step registry class.


   .. py:method:: register(name, cls)


.. py:data:: logger
   :type:  _typeshed.Incomplete

.. py:data:: feature_steps
   :type:  _typeshed.Incomplete

