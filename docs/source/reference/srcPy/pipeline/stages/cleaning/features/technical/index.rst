srcPy.pipeline.stages.cleaning.features.technical
=================================================

.. py:module:: srcPy.pipeline.stages.cleaning.features.technical


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.features.technical.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.features.technical.BaseTechnicalIndicatorStep
   srcPy.pipeline.stages.cleaning.features.technical.RSINormalizerStep
   srcPy.pipeline.stages.cleaning.features.technical.MACDNormalizerStep
   srcPy.pipeline.stages.cleaning.features.technical.ATRNormalizerStep
   srcPy.pipeline.stages.cleaning.features.technical.VWAPNormalizerStep
   srcPy.pipeline.stages.cleaning.features.technical.IncrementalRSI
   srcPy.pipeline.stages.cleaning.features.technical.IncrementalRSIStep
   srcPy.pipeline.stages.cleaning.features.technical.IncrementalMACD
   srcPy.pipeline.stages.cleaning.features.technical.IncrementalMACDStep


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: BaseTechnicalIndicatorStep(mlflow_logger, enabled, window, fillna_method = 'ffill', indicator_name = 'indicator')

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.CleaningStep`


   base technical indicator step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: enabled
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: window
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: fillna_method
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: indicator_name
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


.. py:class:: RSINormalizerStep(mlflow_logger, enabled, window, fillna_method = 'ffill')

   Bases: :py:obj:`BaseTechnicalIndicatorStep`


   rsi normalizer step class.


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


.. py:class:: ATRNormalizerStep(mlflow_logger, enabled, window, fillna_method = 'ffill')

   Bases: :py:obj:`BaseTechnicalIndicatorStep`


   atr normalizer step class.


.. py:class:: VWAPNormalizerStep(mlflow_logger, enabled, window, fillna_method = 'ffill')

   Bases: :py:obj:`BaseTechnicalIndicatorStep`


   vwap normalizer step class.


.. py:class:: IncrementalRSI(window)

   incremental rsi class.


   .. py:attribute:: window
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: gains
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: losses
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: prev_price
      :type:  float | None
      :value: Ellipsis



   .. py:method:: update(price)


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


.. py:class:: IncrementalMACD(fast, slow, signal)

   incremental macd class.


   .. py:attribute:: fast
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: slow
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: signal
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: ema_fast
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: ema_slow
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: macd
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: macd_signal
      :type:  float | None
      :value: Ellipsis



   .. py:method:: update(price)


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


