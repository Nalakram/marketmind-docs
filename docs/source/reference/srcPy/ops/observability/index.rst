srcPy.ops.observability
=======================

.. py:module:: srcPy.ops.observability


Attributes
----------

.. autoapisummary::

   srcPy.ops.observability.OTLPMetricExporter
   srcPy.ops.observability.OTLPSpanExporter
   srcPy.ops.observability.SamplingResult
   srcPy.ops.observability.TraceBasedExemplarFilter
   srcPy.ops.observability.ExponentialBucketHistogramAggregation
   srcPy.ops.observability.ExplicitBucketHistogramAggregation
   srcPy.ops.observability.T
   srcPy.ops.observability.F


Exceptions
----------

.. autoapisummary::

   srcPy.ops.observability.GrpcError
   srcPy.ops.observability.ObservabilityError
   srcPy.ops.observability.ExporterEgressError
   srcPy.ops.observability.ExporterTransientError
   srcPy.ops.observability.MetricsEmitError
   srcPy.ops.observability.PiiRedactionError
   srcPy.ops.observability.TracingInitError


Classes
-------

.. autoapisummary::

   srcPy.ops.observability.TraceContextTextMapPropagator
   srcPy.ops.observability.NoOpMetricsManager
   srcPy.ops.observability.NoOpTracingManager
   srcPy.ops.observability.CircuitBreaker
   srcPy.ops.observability.CardinalityLimiter
   srcPy.ops.observability.PIIRedactor
   srcPy.ops.observability.BoundedEventQueue
   srcPy.ops.observability.MetricConfig
   srcPy.ops.observability.SafeOTLPMetricExporter
   srcPy.ops.observability.MetricsManager
   srcPy.ops.observability.TracingConfig
   srcPy.ops.observability.SafeOTLPSpanExporter
   srcPy.ops.observability.AdaptiveRatioSampler
   srcPy.ops.observability.PiiRedactionSpanProcessor
   srcPy.ops.observability.TracingManager
   srcPy.ops.observability.TraceEnrichedLogger
   srcPy.ops.observability.LoggingManager
   srcPy.ops.observability.AdaptiveThreshold
   srcPy.ops.observability.SLOBurnRate
   srcPy.ops.observability.FastAPIMiddleware
   srcPy.ops.observability.KafkaInstrumentor


Functions
---------

.. autoapisummary::

   srcPy.ops.observability.set_tenant
   srcPy.ops.observability.get_tenant
   srcPy.ops.observability.set_strategy
   srcPy.ops.observability.get_strategy
   srcPy.ops.observability.instrument
   srcPy.ops.observability.register_cache_hit_rate_gauges
   srcPy.ops.observability.register_cache_hit_rate_gauges_for
   srcPy.ops.observability.get_metrics
   srcPy.ops.observability.get_tracing
   srcPy.ops.observability.get_logging
   srcPy.ops.observability.get_logger
   srcPy.ops.observability.init_observability


Module Contents
---------------

.. py:exception:: GrpcError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: ObservabilityError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: ExporterEgressError

   Bases: :py:obj:`ObservabilityError`


   Common base class for all non-exit exceptions.


.. py:exception:: ExporterTransientError

   Bases: :py:obj:`ObservabilityError`


   Common base class for all non-exit exceptions.


.. py:exception:: MetricsEmitError

   Bases: :py:obj:`ObservabilityError`


   Common base class for all non-exit exceptions.


.. py:exception:: PiiRedactionError

   Bases: :py:obj:`ObservabilityError`


   Common base class for all non-exit exceptions.


.. py:exception:: TracingInitError

   Bases: :py:obj:`ObservabilityError`


   Common base class for all non-exit exceptions.


.. py:data:: OTLPMetricExporter

.. py:data:: OTLPSpanExporter

.. py:data:: SamplingResult

.. py:class:: TraceContextTextMapPropagator

   trace context text map propagator class.


   .. py:method:: inject(_)


   .. py:method:: extract(_)


.. py:data:: TraceBasedExemplarFilter
   :type:  Any
   :value: Ellipsis


.. py:data:: ExponentialBucketHistogramAggregation
   :type:  Any
   :value: Ellipsis


.. py:data:: ExplicitBucketHistogramAggregation
   :type:  Any
   :value: Ellipsis


.. py:class:: NoOpMetricsManager(*_a, **_k)

   Manages no op metrics resources and operations.


   .. py:attribute:: meter
      :type:  Any
      :value: Ellipsis



   .. py:method:: counter(*_a, **_k)


   .. py:method:: histogram(*_a, **_k)


   .. py:method:: record_counter(*_a, **_k)


   .. py:method:: record_histogram(*_a, **_k)


   .. py:method:: shutdown()


.. py:class:: NoOpTracingManager(*_a, **_k)

   Manages no op tracing resources and operations.


   .. py:method:: set_sample_rate(*_a, **_k)


   .. py:method:: start_span(*_a, **_k)


   .. py:method:: start_span_with_links(*_a, **_k)


   .. py:method:: inject_context(carrier)


   .. py:method:: extract_context(carrier)


.. py:data:: T

.. py:data:: F

.. py:function:: set_tenant(tenant_id)

.. py:function:: get_tenant()

.. py:function:: set_strategy(strategy_id)

.. py:function:: get_strategy()

.. py:class:: CircuitBreaker(fail_threshold = 5, reset_after_sec = 30)

   circuit breaker class.


   .. py:attribute:: fail_threshold
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: reset_after_sec
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: fail_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: opened_at
      :type:  float | None
      :value: Ellipsis



   .. py:method:: on_success()


   .. py:method:: on_failure()


   .. py:method:: is_open()


.. py:class:: CardinalityLimiter(max_keys_per_label = 1000)

   cardinality limiter class.


   .. py:attribute:: max_keys
      :type:  Any
      :value: Ellipsis



   .. py:method:: sanitize(label_key, label_value)


   .. py:method:: overflow_count()


   .. py:method:: stats()


.. py:class:: PIIRedactor(patterns = None, fast_keys_allowlist = None)

   pii redactor class.


   .. py:attribute:: DEFAULT_PATTERNS
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: patterns
      :type:  Any
      :value: Ellipsis



   .. py:method:: redact_text(text)


   .. py:method:: redact_dict(data)


.. py:class:: BoundedEventQueue(maxsize = 65536)

   bounded event queue class.


   .. py:method:: put_nowait(ev)


   .. py:method:: get_batch(n = 2048)


   .. py:method:: dropped()


   .. py:method:: size()


.. py:class:: MetricConfig

   Configuration for metric.


   .. py:attribute:: prometheus_port
      :type:  int
      :value: Ellipsis



   .. py:attribute:: otlp_endpoint
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: export_interval_millis
      :type:  int
      :value: Ellipsis



   .. py:attribute:: delta_temporality
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: enable_exemplars
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: buffered_emit
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: queue_max_events
      :type:  int
      :value: Ellipsis



   .. py:attribute:: flush_every_ms
      :type:  int
      :value: Ellipsis



   .. py:attribute:: labels_max_keys_per_label
      :type:  int
      :value: Ellipsis



   .. py:attribute:: endpoint_allowlist
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: exporter_timeout_sec
      :type:  float
      :value: Ellipsis



   .. py:attribute:: breaker_fail_threshold
      :type:  int
      :value: Ellipsis



   .. py:attribute:: breaker_reset_seconds
      :type:  int
      :value: Ellipsis



.. py:class:: SafeOTLPMetricExporter(allowlist, breaker, timeout, *args, **kwargs)

   safe otlp metric exporter class.


   .. py:method:: export(metrics_data)


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


.. py:class:: TracingConfig

   Configuration for tracing.


   .. py:attribute:: otlp_endpoint
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: sample_rate
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_queue_size
      :type:  int
      :value: Ellipsis



   .. py:attribute:: max_export_batch_size
      :type:  int
      :value: Ellipsis



   .. py:attribute:: schedule_delay_millis
      :type:  int
      :value: Ellipsis



   .. py:attribute:: enable_console_export
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: endpoint_allowlist
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: exporter_timeout_sec
      :type:  float
      :value: Ellipsis



.. py:class:: SafeOTLPSpanExporter(allowlist, breaker, timeout, *args, **kwargs)

   safe otlp span exporter class.


   .. py:method:: export(spans)


.. py:class:: AdaptiveRatioSampler(initial_rate)

   Bases: :py:obj:`opentelemetry.sdk.trace.sampling.Sampler`


   adaptive ratio sampler class.


   .. py:method:: should_sample(parent_context, trace_id, name, kind, attributes, links)


   .. py:method:: get_description()


   .. py:method:: set_rate(new_rate)


.. py:class:: PiiRedactionSpanProcessor

   Bases: :py:obj:`_SpanProcessorBase`


   Processes pii redaction span data.


   .. py:attribute:: redactor
      :type:  Any
      :value: Ellipsis



   .. py:method:: on_start(span, parent_context = None)


   .. py:method:: on_end(span)


   .. py:method:: shutdown()


   .. py:method:: force_flush(timeout_millis = 30000)


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


.. py:class:: TraceEnrichedLogger(base_logger, service_name)

   trace enriched logger class.


   .. py:method:: info(msg, **kwargs)


   .. py:method:: error(msg, **kwargs)


   .. py:method:: warning(msg, **kwargs)


   .. py:method:: debug(msg, **kwargs)


.. py:class:: LoggingManager(service_name = 'financial-ml', mm_config = None)

   Manages logging resources and operations.


   .. py:attribute:: service_name
      :type:  Any
      :value: Ellipsis



   .. py:method:: get_logger()


.. py:class:: AdaptiveThreshold(alpha = 0.1, sensitivity = 3.0, window_size = 1024)

   adaptive threshold class.


   .. py:attribute:: alpha
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: sensitivity
      :type:  Any
      :value: Ellipsis



   .. py:method:: update(value)


   .. py:method:: threshold()


.. py:class:: SLOBurnRate(minutes = (1, 5, 30))

   slo burn rate class.


   .. py:attribute:: windows
      :type:  Any
      :value: Ellipsis



   .. py:method:: record(ok)


   .. py:method:: burn_rates(slo_error_budget)


.. py:function:: instrument(name = None, labels = None, record_exceptions = True, measure_latency = True)

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


.. py:function:: register_cache_hit_rate_gauges(cache_client, metric_name = 'cache_hit_rate')

.. py:function:: register_cache_hit_rate_gauges_for(func_or_client, metric_name = 'cache_hit_rate')

.. py:function:: get_metrics()

.. py:function:: get_tracing()

.. py:function:: get_logging()

.. py:function:: get_logger()

.. py:function:: init_observability(service_name = 'financial-ml', metrics_config = None, tracing_config = None, enable_metrics = True, enable_tracing = True, enable_logging = True)

