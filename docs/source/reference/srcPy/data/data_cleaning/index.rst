srcPy.data.data_cleaning
========================

.. py:module:: srcPy.data.data_cleaning


Attributes
----------

.. autoapisummary::

   srcPy.data.data_cleaning.logger
   srcPy.data.data_cleaning.streaming_latency
   srcPy.data.data_cleaning.buffer_length


Classes
-------

.. autoapisummary::

   srcPy.data.data_cleaning.CleaningStep
   srcPy.data.data_cleaning.MissingImputer
   srcPy.data.data_cleaning.OutlierHandler
   srcPy.data.data_cleaning.Denoiser
   srcPy.data.data_cleaning.IncrementalRSI
   srcPy.data.data_cleaning.IncrementalRSIStep
   srcPy.data.data_cleaning.IncrementalMACD
   srcPy.data.data_cleaning.IncrementalMACDStep
   srcPy.data.data_cleaning.SentimentExtractor
   srcPy.data.data_cleaning.CalendarFeatures
   srcPy.data.data_cleaning.AnomalyDetector
   srcPy.data.data_cleaning.StreamingIsolationForest
   srcPy.data.data_cleaning.StreamingAnomalyStep
   srcPy.data.data_cleaning.CleanerPipeline
   srcPy.data.data_cleaning.StreamingCleanerPipeline
   srcPy.data.data_cleaning.ValidationStep
   srcPy.data.data_cleaning.RSICalculator
   srcPy.data.data_cleaning.DataCleaner


Functions
---------

.. autoapisummary::

   srcPy.data.data_cleaning.get_runtime_config


Module Contents
---------------

.. py:function:: get_runtime_config()

.. py:data:: logger
   :type:  _typeshed.Incomplete

.. py:data:: streaming_latency
   :type:  _typeshed.Incomplete

.. py:data:: buffer_length
   :type:  _typeshed.Incomplete

.. py:class:: CleaningStep

   Bases: :py:obj:`abc.ABC`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: apply(df)
      :abstractmethod:



.. py:class:: MissingImputer(method, params)

   .. py:attribute:: method
      :type:  _typeshed.Incomplete


   .. py:attribute:: params
      :type:  _typeshed.Incomplete


   .. py:method:: apply(df)


.. py:class:: OutlierHandler(method, params)

   Bases: :py:obj:`CleaningStep`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: method
      :type:  _typeshed.Incomplete


   .. py:attribute:: params
      :type:  _typeshed.Incomplete


   .. py:method:: apply(df)


.. py:class:: Denoiser(method, params)

   Bases: :py:obj:`CleaningStep`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: method
      :type:  _typeshed.Incomplete


   .. py:attribute:: params
      :type:  _typeshed.Incomplete


   .. py:method:: apply(df)


.. py:class:: IncrementalRSI(window)

   .. py:attribute:: window
      :type:  _typeshed.Incomplete


   .. py:attribute:: gains
      :type:  _typeshed.Incomplete


   .. py:attribute:: losses
      :type:  _typeshed.Incomplete


   .. py:attribute:: prev_price
      :type:  _typeshed.Incomplete


   .. py:method:: update(price)


.. py:class:: IncrementalRSIStep(window)

   Bases: :py:obj:`CleaningStep`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: rsi
      :type:  _typeshed.Incomplete


   .. py:method:: apply(df)


.. py:class:: IncrementalMACD(fast, slow, signal)

   .. py:attribute:: fast
      :type:  _typeshed.Incomplete


   .. py:attribute:: slow
      :type:  _typeshed.Incomplete


   .. py:attribute:: signal
      :type:  _typeshed.Incomplete


   .. py:attribute:: ema_fast
      :type:  _typeshed.Incomplete


   .. py:attribute:: ema_slow
      :type:  _typeshed.Incomplete


   .. py:attribute:: macd
      :type:  _typeshed.Incomplete


   .. py:attribute:: macd_signal
      :type:  _typeshed.Incomplete


   .. py:method:: update(price)


.. py:class:: IncrementalMACDStep(fast, slow, signal)

   Bases: :py:obj:`CleaningStep`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: macd
      :type:  _typeshed.Incomplete


   .. py:method:: apply(df)


.. py:class:: SentimentExtractor(cfg)

   Bases: :py:obj:`CleaningStep`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: enabled
      :type:  _typeshed.Incomplete


   .. py:attribute:: model
      :type:  _typeshed.Incomplete


   .. py:method:: apply(df)


.. py:class:: CalendarFeatures(cfg)

   Bases: :py:obj:`CleaningStep`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: day
      :type:  _typeshed.Incomplete


   .. py:attribute:: holiday
      :type:  _typeshed.Incomplete


   .. py:attribute:: calendar
      :type:  _typeshed.Incomplete


   .. py:method:: apply(df)


.. py:class:: AnomalyDetector(cfg)

   Bases: :py:obj:`CleaningStep`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: enabled
      :type:  _typeshed.Incomplete


   .. py:attribute:: contamination
      :type:  _typeshed.Incomplete


   .. py:attribute:: refit_interval
      :type:  _typeshed.Incomplete


   .. py:attribute:: method
      :type:  _typeshed.Incomplete


   .. py:attribute:: model
      :type:  _typeshed.Incomplete


   .. py:attribute:: counter
      :type:  int


   .. py:method:: apply(df)


.. py:class:: StreamingIsolationForest(contamination, refit_every, window_size = 1000)

   .. py:attribute:: contamination
      :type:  _typeshed.Incomplete


   .. py:attribute:: refit_every
      :type:  _typeshed.Incomplete


   .. py:attribute:: window_size
      :type:  _typeshed.Incomplete


   .. py:attribute:: buffer
      :type:  _typeshed.Incomplete


   .. py:attribute:: model
      :type:  _typeshed.Incomplete


   .. py:attribute:: counter
      :type:  int


   .. py:method:: fit(data)


   .. py:method:: predict(df)


.. py:class:: StreamingAnomalyStep(contamination = 0.1, refit_every = 100, random_state = 42)

   .. py:attribute:: contamination
      :type:  _typeshed.Incomplete


   .. py:attribute:: refit_every
      :type:  _typeshed.Incomplete


   .. py:attribute:: random_state
      :type:  _typeshed.Incomplete


   .. py:attribute:: model
      :type:  _typeshed.Incomplete


   .. py:method:: apply(df)


.. py:class:: CleanerPipeline(steps)

   .. py:attribute:: steps
      :type:  _typeshed.Incomplete


   .. py:method:: run(df, distributed = False)


.. py:class:: StreamingCleanerPipeline(steps, buffer_size = 100, window = 252)

   Bases: :py:obj:`CleanerPipeline`


   .. py:attribute:: buffer
      :type:  _typeshed.Incomplete


   .. py:attribute:: buffer_size
      :type:  _typeshed.Incomplete


   .. py:attribute:: rsi
      :type:  _typeshed.Incomplete


   .. py:attribute:: macd
      :type:  _typeshed.Incomplete


   .. py:method:: process_stream(stream_gen)
      :async:



.. py:class:: ValidationStep(required_columns = None)

   Bases: :py:obj:`CleaningStep`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: required_columns
      :type:  _typeshed.Incomplete


   .. py:method:: apply(df)


.. py:class:: RSICalculator(cfg)

   Bases: :py:obj:`CleaningStep`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: enabled
      :type:  _typeshed.Incomplete


   .. py:attribute:: window
      :type:  _typeshed.Incomplete


   .. py:attribute:: fillna_method
      :type:  _typeshed.Incomplete


   .. py:method:: apply(df)


.. py:class:: DataCleaner(cfg = None, streaming = False)

   .. py:attribute:: cfg
      :type:  _typeshed.Incomplete


   .. py:attribute:: pipeline
      :type:  _typeshed.Incomplete


   .. py:method:: clean(df)


   .. py:method:: clean_chunk(df)


