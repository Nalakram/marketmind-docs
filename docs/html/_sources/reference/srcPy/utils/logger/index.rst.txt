srcPy.utils.logger
==================

.. py:module:: srcPy.utils.logger


Attributes
----------

.. autoapisummary::

   srcPy.utils.logger.logger


Classes
-------

.. autoapisummary::

   srcPy.utils.logger.InfluxDBHandler


Functions
---------

.. autoapisummary::

   srcPy.utils.logger.safe_filter_by_level
   srcPy.utils.logger.redact_sensitive_info
   srcPy.utils.logger.configure_logger
   srcPy.utils.logger.get_logger


Module Contents
---------------

.. py:class:: InfluxDBHandler(url, token, org, bucket, level = ...)

   Bases: :py:obj:`logging.Handler`


   Handler instances dispatch logging events to specific destinations.

   The base handler class. Acts as a placeholder which defines the Handler
   interface. Handlers can optionally use Formatter instances to format
   records as desired. By default, no formatter is specified; in this case,
   the 'raw' message as determined by record.message is logged.


   .. py:attribute:: client
      :type:  _typeshed.Incomplete


   .. py:attribute:: write_api
      :type:  _typeshed.Incomplete


   .. py:attribute:: bucket
      :type:  _typeshed.Incomplete


   .. py:method:: emit(record)

      Do whatever it takes to actually log the specified logging record.

      This version is intended to be implemented by subclasses and so
      raises a NotImplementedError.



.. py:function:: safe_filter_by_level(logger, method_name, event_dict)

.. py:function:: redact_sensitive_info(sensitive_keys)

.. py:function:: configure_logger(config = None)

.. py:function:: get_logger(name = None)

.. py:data:: logger
   :type:  structlog.stdlib.BoundLogger

