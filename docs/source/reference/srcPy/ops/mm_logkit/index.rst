srcPy.ops.mm_logkit
===================

.. py:module:: srcPy.ops.mm_logkit


Classes
-------

.. autoapisummary::

   srcPy.ops.mm_logkit.RedactFilter
   srcPy.ops.mm_logkit.JSONFormatter
   srcPy.ops.mm_logkit.KVFormatter
   srcPy.ops.mm_logkit.BoundLogger
   srcPy.ops.mm_logkit.InfluxDBHandler


Functions
---------

.. autoapisummary::

   srcPy.ops.mm_logkit.redact_processor
   srcPy.ops.mm_logkit.redact_sensitive_info
   srcPy.ops.mm_logkit.timestamp_processor
   srcPy.ops.mm_logkit.safe_filter_by_level
   srcPy.ops.mm_logkit.build_console_handler
   srcPy.ops.mm_logkit.build_file_handler
   srcPy.ops.mm_logkit.build_syslog_handler
   srcPy.ops.mm_logkit.build_http_handler
   srcPy.ops.mm_logkit.build_influx_handler
   srcPy.ops.mm_logkit.configure_logger
   srcPy.ops.mm_logkit.get_logger
   srcPy.ops.mm_logkit.log_drift_warning


Module Contents
---------------

.. py:class:: RedactFilter(keys = ...)

   Bases: :py:obj:`logging.Filter`


   redact filter class.


   .. py:method:: filter(record)

      Determine if the specified record is to be logged.

      Returns True if the record should be logged, or False otherwise.
      If deemed appropriate, the record may be modified in-place.



.. py:function:: redact_processor(_, __, event_dict)

.. py:function:: redact_sensitive_info(keys)

.. py:function:: timestamp_processor(_, __, event_dict)

.. py:function:: safe_filter_by_level(logger, level, event_dict)

.. py:class:: JSONFormatter(fmt=None, datefmt=None, style='%', validate=True, *, defaults=None)

   Bases: :py:obj:`logging.Formatter`


   json formatter class.


   .. py:method:: format(record)

      Format the specified record as text.

      The record's attribute dictionary is used as the operand to a
      string formatting operation which yields the returned string.
      Before formatting the dictionary, a couple of preparatory steps
      are carried out. The message attribute of the record is computed
      using LogRecord.getMessage(). If the formatting string uses the
      time (as determined by a call to usesTime(), formatTime() is
      called to format the event time. If there is exception information,
      it is formatted using formatException() and appended to the message.



.. py:class:: KVFormatter(fmt=None, datefmt=None, style='%', validate=True, *, defaults=None)

   Bases: :py:obj:`logging.Formatter`


   kv formatter class.


   .. py:method:: format(record)

      Format the specified record as text.

      The record's attribute dictionary is used as the operand to a
      string formatting operation which yields the returned string.
      Before formatting the dictionary, a couple of preparatory steps
      are carried out. The message attribute of the record is computed
      using LogRecord.getMessage(). If the formatting string uses the
      time (as determined by a call to usesTime(), formatTime() is
      called to format the event time. If there is exception information,
      it is formatted using formatException() and appended to the message.



.. py:class:: BoundLogger(logger, processors = None, context = None)

   Bases: :py:obj:`_StdBoundLogger`


   bound logger class.


   .. py:property:: name
      :type: str



   .. py:method:: setLevel(level)


   .. py:method:: bind(**context)


   .. py:method:: debug(msg, *a, **k)


   .. py:method:: info(msg, *a, **k)


   .. py:method:: warning(msg, *a, **k)


   .. py:method:: error(msg, *a, **k)


   .. py:method:: critical(msg, *a, **k)


   .. py:method:: exception(msg, *a, **k)


   .. py:method:: DEBUG(*args, **kwargs)


   .. py:method:: INFO(*args, **kwargs)


   .. py:method:: WARNING(*args, **kwargs)


   .. py:method:: ERROR(*args, **kwargs)


   .. py:method:: CRITICAL(*args, **kwargs)


   .. py:method:: EXCEPTION(*args, **kwargs)


.. py:function:: build_console_handler(cfg)

.. py:function:: build_file_handler(cfg)

.. py:function:: build_syslog_handler(cfg)

.. py:function:: build_http_handler(cfg)

.. py:function:: build_influx_handler(cfg)

.. py:function:: configure_logger(config = None, /, **legacy_kwargs)

.. py:function:: get_logger(name = None)

.. py:function:: log_drift_warning(*args, **kwargs)

.. py:class:: InfluxDBHandler(client, bucket, org)

   Bases: :py:obj:`logging.Handler`


   Handles influx db events and requests.


   .. py:attribute:: client
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: write_api
      :type:  Any
      :value: Ellipsis



   .. py:method:: emit(record)

      Do whatever it takes to actually log the specified logging record.

      This version is intended to be implemented by subclasses and so
      raises a NotImplementedError.



   .. py:method:: handleError(record)

      Handle errors which occur during an emit() call.

      This method should be called from handlers when an exception is
      encountered during an emit() call. If raiseExceptions is false,
      exceptions get silently ignored. This is what is mostly wanted
      for a logging system - most users will not care about errors in
      the logging system, they are more interested in application errors.
      You could, however, replace this with a custom handler if you wish.
      The record which was being processed is passed in to this method.



