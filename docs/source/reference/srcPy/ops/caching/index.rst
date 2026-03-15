srcPy.ops.caching
=================

.. py:module:: srcPy.ops.caching


Attributes
----------

.. autoapisummary::

   srcPy.ops.caching.T


Classes
-------

.. autoapisummary::

   srcPy.ops.caching.HashAlgorithm
   srcPy.ops.caching.CompressionLevel
   srcPy.ops.caching.CompressionStrategy
   srcPy.ops.caching.CacheEntry
   srcPy.ops.caching.CacheMetrics
   srcPy.ops.caching.AdaptiveTTLManager
   srcPy.ops.caching.EnhancedCacheManager
   srcPy.ops.caching.DistributedCacheCoordinator
   srcPy.ops.caching.PersistentCache


Functions
---------

.. autoapisummary::

   srcPy.ops.caching.hash_bytes
   srcPy.ops.caching.hash_config
   srcPy.ops.caching.hash_dataframe_deterministic
   srcPy.ops.caching.versioned_key
   srcPy.ops.caching.enhanced_cache


Module Contents
---------------

.. py:data:: T

.. py:class:: HashAlgorithm

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



.. py:function:: hash_bytes(data, algo = ...)

.. py:function:: hash_config(cfg_obj, algo = ...)

.. py:function:: hash_dataframe_deterministic(df, cols=None, algo = ...)

.. py:function:: versioned_key(*parts, version = 'v1')

.. py:class:: CompressionLevel

   Bases: :py:obj:`enum.Enum`


   compression level class.


   .. py:attribute:: NONE
      :value: 0



   .. py:attribute:: FAST
      :value: 1



   .. py:attribute:: HIGH
      :value: 2



.. py:class:: CompressionStrategy

   Strategy for compression behavior.


   .. py:attribute:: small_threshold
      :type:  int
      :value: Ellipsis



   .. py:attribute:: fast_threshold
      :type:  int
      :value: Ellipsis



   .. py:method:: compress(data, level = None)


   .. py:method:: decompress(data, level)


.. py:class:: CacheEntry

   cache entry class.


   .. py:attribute:: value
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: expiry
      :type:  float
      :value: Ellipsis



   .. py:attribute:: version
      :type:  int
      :value: Ellipsis



   .. py:attribute:: access_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: last_access
      :type:  float


   .. py:attribute:: compression
      :type:  CompressionLevel
      :value: Ellipsis



.. py:class:: CacheMetrics

   cache metrics class.


   .. py:attribute:: hits
      :type:  int
      :value: Ellipsis



   .. py:attribute:: misses
      :type:  int
      :value: Ellipsis



   .. py:attribute:: evictions
      :type:  int
      :value: Ellipsis



   .. py:attribute:: sets
      :type:  int
      :value: Ellipsis



   .. py:attribute:: total_latency_ns
      :type:  int
      :value: Ellipsis



   .. py:property:: hit_rate
      :type: float



   .. py:property:: avg_latency_us
      :type: float



.. py:class:: AdaptiveTTLManager(base_ttl = 300)

   Manages adaptive ttl resources and operations.


   .. py:attribute:: base_ttl
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: volatility_multiplier
      :type:  float
      :value: Ellipsis



   .. py:method:: get_ttl(key, volatility = 0.0)


   .. py:method:: update_volatility(volatility)


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



.. py:class:: DistributedCacheCoordinator(redis_client=None)

   distributed cache coordinator class.


   .. py:attribute:: CAS_SCRIPT
      :type:  str
      :value: Ellipsis



   .. py:attribute:: redis
      :type:  Any
      :value: Ellipsis



   .. py:method:: cas_update(key, value, timestamp)
      :async:



   .. py:method:: invalidate_broadcast(channel, key)
      :async:



.. py:function:: enhanced_cache(max_size = 128, ttl = None, key_fn = None, version = 'v1', enable_metrics = True)

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


