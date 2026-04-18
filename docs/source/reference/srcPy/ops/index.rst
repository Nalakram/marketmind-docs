srcPy.ops
=========

.. py:module:: srcPy.ops


Submodules
----------

.. toctree::
   :maxdepth: 1

   /reference/srcPy/ops/caching/index
   /reference/srcPy/ops/mm_logkit/index
   /reference/srcPy/ops/multi_tier_cache/index
   /reference/srcPy/ops/observability/index


Classes
-------

.. autoapisummary::

   srcPy.ops.EnhancedCacheManager
   srcPy.ops.HashAlgorithm
   srcPy.ops.PersistentCache
   srcPy.ops.BoundLogger
   srcPy.ops.JSONFormatter
   srcPy.ops.MultiTierClient
   srcPy.ops.FastAPIMiddleware
   srcPy.ops.KafkaInstrumentor
   srcPy.ops.LoggingManager
   srcPy.ops.MetricsManager
   srcPy.ops.TracingManager


Functions
---------

.. autoapisummary::

   srcPy.ops.enhanced_cache
   srcPy.ops.hash_config
   srcPy.ops.hash_dataframe_deterministic
   srcPy.ops.versioned_key
   srcPy.ops.configure_logger
   srcPy.ops.get_logger
   srcPy.ops.get_logging
   srcPy.ops.get_metrics
   srcPy.ops.get_strategy
   srcPy.ops.get_tenant
   srcPy.ops.get_tracing
   srcPy.ops.init_observability
   srcPy.ops.instrument
   srcPy.ops.register_cache_hit_rate_gauges
   srcPy.ops.set_strategy
   srcPy.ops.set_tenant


Package Contents
----------------

.. py:class:: EnhancedCacheManager(max_size = 128, ttl = None, eviction_policy = 'lru', enable_compression = True, enable_metrics = True)

   Manages enhanced cache resources and operations.


   .. py:attribute:: max_size
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: base_ttl
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: eviction_policy
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: enable_compression
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: compression
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: ttl_manager
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: metrics
      :type:  Any
      :value: Ellipsis



   .. py:method:: get(key, version = 0)


   .. py:method:: set(key, value, ttl = None, version = 0, volatility = 0.0)


   .. py:method:: invalidate(key)


   .. py:method:: invalidate_pattern(prefix)


   .. py:method:: get_async(key, version = 0)
      :async:



   .. py:method:: set_async(key, value, **kwargs)
      :async:



.. py:class:: HashAlgorithm(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   hash algorithm class.


   .. py:attribute:: XXHASH
      :value: 'xxhash'



   .. py:attribute:: BLAKE3
      :value: 'blake3'



   .. py:attribute:: SIPHASH
      :value: 'siphash'



   .. py:attribute:: SHA256
      :value: 'sha256'



.. py:class:: PersistentCache(cache_dir = '.cache', enable_compression = True)

   persistent cache class.


   .. py:attribute:: cache_dir
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: compression
      :type:  Any
      :value: Ellipsis



   .. py:method:: exists(key)


   .. py:method:: save_df(key, df, version = 'v1')


   .. py:method:: load_df(key, expected_version = None)


   .. py:method:: invalidate(key)


.. py:function:: enhanced_cache(max_size = 128, ttl = None, key_fn = None, version = 'v1', enable_metrics = True)

.. py:function:: hash_config(cfg_obj, algo = ...)

.. py:function:: hash_dataframe_deterministic(df, cols=None, algo = ...)

.. py:function:: versioned_key(*parts, version = 'v1')

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



.. py:function:: configure_logger(config = None, /, **legacy_kwargs)

.. py:class:: MultiTierClient(l1_size = 128, l1_ttl = 60, l2_type = 'memfd', l2_path = None, redis_client=None, l3_key_prefix = 'l3:', l4_cache_dir = '.cache', enable_singleflight = True, ttl_jitter = 0.1, check_l4_on_miss = False, enable_invalidation_listener = True)

   Client for interacting with multi tier service.


   .. py:attribute:: l1
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: l2
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: l3
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: l4
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: singleflight
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: ttl_jitter
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: check_l4_on_miss
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: metrics
      :type:  Any
      :value: Ellipsis



   .. py:method:: get(key, version = 0)


   .. py:method:: set(key, value, ttl = None, version = 0, write_through = True, persist_to_l4 = False)


   .. py:method:: compute_or_get(key, compute_fn, ttl = None, version = 0, persist_to_l4 = False)


   .. py:method:: compute_or_get_async(key, compute_fn, ttl = None, version = 0, persist_to_l4 = False)
      :async:



   .. py:method:: invalidate(key, broadcast = True)


   .. py:method:: invalidate_pattern(prefix, broadcast = True)


   .. py:method:: close()


.. py:function:: multi_tier_cache(ttl = 60, version = 'v1', persist_large_objects = False, key_fn = None, redis_client=None, l2_type = 'memfd', check_l4_on_miss = False)
   :no-index:

.. py:class:: FastAPIMiddleware(app, service_name = 'api', slo_error_budget = 0.01)

   fast api middleware class.


   .. py:attribute:: app
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: service_name
      :type:  Any
      :value: Ellipsis



   .. py:method:: __call__(scope, receive, send)
      :async:



.. py:class:: KafkaInstrumentor

   kafka instrumentor class.


   .. py:attribute:: propagator
      :type:  Any
      :value: Ellipsis



   .. py:method:: inject_context(headers)


   .. py:method:: extract_context(headers)


   .. py:method:: instrument_producer(producer)


   .. py:method:: instrument_consumer(consumer)


.. py:class:: LoggingManager(service_name = 'financial-ml', mm_config = None)

   Manages logging resources and operations.


   .. py:attribute:: service_name
      :type:  Any
      :value: Ellipsis



   .. py:method:: get_logger()


.. py:class:: MetricsManager(service_name = 'financial-ml', config = None)

   Manages metrics resources and operations.


   .. py:attribute:: service_name
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: card
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: redactor
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: provider
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: meter
      :type:  Any
      :value: Ellipsis



   .. py:method:: counter(name, description = '', unit = '1')


   .. py:method:: histogram(name, description = '', unit = 'ms')


   .. py:method:: record_counter(counter, value = 1, labels = None)


   .. py:method:: record_histogram(histogram, value, labels = None)


   .. py:method:: shutdown()


.. py:class:: TracingManager(service_name = 'financial-ml', config = None)

   Manages tracing resources and operations.


   .. py:attribute:: service_name
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: provider
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: tracer
      :type:  Any
      :value: Ellipsis



   .. py:method:: set_sample_rate(rate)


   .. py:method:: start_span(name, kind = ..., attributes = None, links = None)


   .. py:method:: start_span_with_links(name, linked_spans, **kwargs)


   .. py:method:: inject_context(carrier)


   .. py:method:: extract_context(carrier)


.. py:function:: get_logger()

.. py:function:: get_logging()

.. py:function:: get_metrics()

.. py:function:: get_strategy()

.. py:function:: get_tenant()

.. py:function:: get_tracing()

.. py:function:: init_observability(service_name = 'financial-ml', metrics_config = None, tracing_config = None, enable_metrics = True, enable_tracing = True, enable_logging = True)

.. py:function:: instrument(name = None, labels = None, record_exceptions = True, measure_latency = True)

.. py:function:: register_cache_hit_rate_gauges(cache_client, metric_name = 'cache_hit_rate')

.. py:function:: set_strategy(strategy_id)

.. py:function:: set_tenant(tenant_id)

