srcPy.pipeline.stages.cleaning.features.calendar
================================================

.. py:module:: srcPy.pipeline.stages.cleaning.features.calendar


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.features.calendar.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.features.calendar.TimeZoneNormalizerStep
   srcPy.pipeline.stages.cleaning.features.calendar.GlobalCalendarNormalizerStep


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


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


