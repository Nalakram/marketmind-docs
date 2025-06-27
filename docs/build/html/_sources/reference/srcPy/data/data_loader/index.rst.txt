srcPy.data.data_loader
======================

.. py:module:: srcPy.data.data_loader


Attributes
----------

.. autoapisummary::

   srcPy.data.data_loader.logger


Classes
-------

.. autoapisummary::

   srcPy.data.data_loader.BaseDataLoader
   srcPy.data.data_loader.APIDataLoader
   srcPy.data.data_loader.CSVLoader
   srcPy.data.data_loader.TwitterLoader
   srcPy.data.data_loader.ESGLoader
   srcPy.data.data_loader.FREDLoader
   srcPy.data.data_loader.BloombergLoader
   srcPy.data.data_loader.WeatherLoader
   srcPy.data.data_loader.AlpacaStreamLoader
   srcPy.data.data_loader.InfluxDBLoader


Functions
---------

.. autoapisummary::

   srcPy.data.data_loader.get_runtime_config
   srcPy.data.data_loader.build_loader


Module Contents
---------------

.. py:data:: logger
   :type:  _typeshed.Incomplete

.. py:function:: get_runtime_config()

.. py:class:: BaseDataLoader(config)

   Bases: :py:obj:`abc.ABC`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: config
      :type:  _typeshed.Incomplete


   .. py:method:: load_data(*args, **kwargs)
      :abstractmethod:

      :async:



.. py:class:: APIDataLoader(config)

   Bases: :py:obj:`BaseDataLoader`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: max_attempts
      :type:  _typeshed.Incomplete


   .. py:attribute:: initial_backoff_seconds
      :type:  _typeshed.Incomplete


   .. py:attribute:: max_backoff_seconds
      :type:  _typeshed.Incomplete


   .. py:attribute:: retry_strategy
      :type:  _typeshed.Incomplete


   .. py:attribute:: fallback
      :type:  _typeshed.Incomplete


   .. py:attribute:: fallback_timeout_seconds
      :type:  _typeshed.Incomplete


.. py:class:: CSVLoader(config)

   Bases: :py:obj:`BaseDataLoader`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: load_data()


   .. py:method:: stream_data()
      :async:



.. py:class:: TwitterLoader(config)

   Bases: :py:obj:`APIDataLoader`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: base_url
      :type:  _typeshed.Incomplete


   .. py:attribute:: endpoints
      :type:  _typeshed.Incomplete


   .. py:attribute:: bearer_token
      :type:  _typeshed.Incomplete


   .. py:attribute:: retry_after_header
      :type:  _typeshed.Incomplete


   .. py:attribute:: timeout
      :type:  _typeshed.Incomplete


   .. py:attribute:: api_key
      :type:  _typeshed.Incomplete


   .. py:method:: load_data(query)
      :async:



   .. py:method:: stream_data()
      :async:



.. py:class:: ESGLoader(config)

   Bases: :py:obj:`APIDataLoader`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: load_data(identifiers)
      :async:



.. py:class:: FREDLoader(config)

   Bases: :py:obj:`APIDataLoader`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: api_key
      :type:  _typeshed.Incomplete


   .. py:method:: load_data(series_ids)
      :async:



.. py:class:: BloombergLoader(config)

   Bases: :py:obj:`APIDataLoader`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: api_key
      :type:  _typeshed.Incomplete


   .. py:method:: load_data(topics)
      :async:



.. py:class:: WeatherLoader(config)

   Bases: :py:obj:`APIDataLoader`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: api_key
      :type:  _typeshed.Incomplete


   .. py:method:: load_data(locations)
      :async:



.. py:class:: AlpacaStreamLoader(cfg)

   Bases: :py:obj:`BaseDataLoader`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: api_key
      :type:  _typeshed.Incomplete


   .. py:attribute:: secret_key
      :type:  _typeshed.Incomplete


   .. py:attribute:: endpoint
      :type:  _typeshed.Incomplete


   .. py:method:: stream_data()
      :async:



   .. py:method:: load_data(*args, **kwargs)
      :async:



.. py:class:: InfluxDBLoader(config)

   Bases: :py:obj:`BaseDataLoader`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: load_data(query)
      :async:



.. py:function:: build_loader(config_section)

