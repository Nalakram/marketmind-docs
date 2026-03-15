srcPy.ops.multi_tier_cache
==========================

.. py:module:: srcPy.ops.multi_tier_cache


Attributes
----------

.. autoapisummary::

   srcPy.ops.multi_tier_cache.PYARROW_AVAILABLE
   srcPy.ops.multi_tier_cache.redis
   srcPy.ops.multi_tier_cache.REDIS_AVAILABLE
   srcPy.ops.multi_tier_cache.T


Classes
-------

.. autoapisummary::

   srcPy.ops.multi_tier_cache.Call
   srcPy.ops.multi_tier_cache.Singleflight
   srcPy.ops.multi_tier_cache.L2Cache
   srcPy.ops.multi_tier_cache.PlasmaL2Cache
   srcPy.ops.multi_tier_cache.MemfdL2Cache
   srcPy.ops.multi_tier_cache.L3Cache
   srcPy.ops.multi_tier_cache.TierMetrics
   srcPy.ops.multi_tier_cache.MultiTierMetrics
   srcPy.ops.multi_tier_cache.InvalidationListener
   srcPy.ops.multi_tier_cache.MultiTierClient
   srcPy.ops.multi_tier_cache.PrometheusExporter


Functions
---------

.. autoapisummary::

   srcPy.ops.multi_tier_cache.version_to_int
   srcPy.ops.multi_tier_cache.multi_tier_cache


Module Contents
---------------

.. py:data:: PYARROW_AVAILABLE
   :type:  bool
   :value: Ellipsis


.. py:data:: redis
   :type:  Any
   :value: Ellipsis


.. py:data:: REDIS_AVAILABLE
   :type:  Any
   :value: Ellipsis


.. py:data:: T

.. py:function:: version_to_int(version_str)

.. py:class:: Call

   call class.


   .. py:attribute:: future
      :type:  concurrent.futures.Future | asyncio.Future
      :value: Ellipsis



   .. py:attribute:: start_time
      :type:  float
      :value: Ellipsis



   .. py:attribute:: is_async
      :type:  bool
      :value: Ellipsis



.. py:class:: Singleflight

   singleflight class.


   .. py:method:: do(key, fn)


   .. py:method:: do_async(key, fn)
      :async:



.. py:class:: L2Cache

   l2cache class.


   .. py:method:: get(key)


   .. py:method:: set(key, value, ttl = None)


   .. py:method:: invalidate(key)


.. py:class:: PlasmaL2Cache(plasma_path = '/tmp/plasma')

   Bases: :py:obj:`L2Cache`


   plasma l2cache class.


   .. py:attribute:: client
      :type:  Any
      :value: Ellipsis



   .. py:method:: get(key)


   .. py:method:: set(key, value, ttl = None)


   .. py:method:: invalidate(key)


.. py:class:: MemfdL2Cache(cache_dir = '/dev/shm/l2_cache')

   Bases: :py:obj:`L2Cache`


   memfd l2cache class.


   .. py:attribute:: cache_dir
      :type:  Any
      :value: Ellipsis



   .. py:method:: get(key)


   .. py:method:: set(key, value, ttl = 60)


   .. py:method:: invalidate(key)


.. py:class:: L3Cache(redis_client=None, key_prefix = 'l3:')

   l3cache class.


   .. py:attribute:: redis
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: key_prefix
      :type:  Any
      :value: Ellipsis



   .. py:method:: get(key)


   .. py:method:: set(key, value, ttl = None)


   .. py:method:: invalidate(key)


   .. py:method:: publish_invalidation(channel, key)


.. py:class:: TierMetrics

   tier metrics class.


   .. py:attribute:: tier_name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: hits
      :type:  int
      :value: Ellipsis



   .. py:attribute:: misses
      :type:  int
      :value: Ellipsis



   .. py:attribute:: sets
      :type:  int
      :value: Ellipsis



   .. py:attribute:: promotions
      :type:  int
      :value: Ellipsis



   .. py:attribute:: latency_ns
      :type:  int
      :value: Ellipsis



   .. py:property:: hit_rate
      :type: float



   .. py:property:: avg_latency_us
      :type: float



.. py:class:: MultiTierMetrics

   multi tier metrics class.


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



   .. py:attribute:: singleflight_saved
      :type:  int
      :value: Ellipsis



   .. py:method:: summary()


.. py:class:: InvalidationListener(redis_client, channel, callback)

   invalidation listener class.


   .. py:attribute:: redis
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: channel
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: callback
      :type:  Any
      :value: Ellipsis



   .. py:method:: start()


   .. py:method:: stop()


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

.. py:class:: PrometheusExporter(client)

   prometheus exporter class.


   .. py:attribute:: client
      :type:  Any
      :value: Ellipsis



   .. py:method:: export()


