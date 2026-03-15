srcPy.pipeline.stages.cleaning.features.sentiment
=================================================

.. py:module:: srcPy.pipeline.stages.cleaning.features.sentiment


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.features.sentiment.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.features.sentiment.BaseSentimentExtractor
   srcPy.pipeline.stages.cleaning.features.sentiment.SentimentExtractor
   srcPy.pipeline.stages.cleaning.features.sentiment.AdvancedSentimentExtractor


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: BaseSentimentExtractor(mlflow_logger, enabled, text_col = 'text', analyzer = 'vader')

   Bases: :py:obj:`srcPy.pipeline.core.pipeline_core_base.CleaningStep`


   base sentiment extractor class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: enabled
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: text_col
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: analyzer
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


.. py:class:: SentimentExtractor(mlflow_logger, enabled, text_col = 'text')

   Bases: :py:obj:`BaseSentimentExtractor`


   sentiment extractor class.


   .. py:attribute:: model
      :type:  Any
      :value: Ellipsis



.. py:class:: AdvancedSentimentExtractor(mlflow_logger, enabled, text_col = 'text', analyzer = 'finbert')

   Bases: :py:obj:`BaseSentimentExtractor`


   advanced sentiment extractor class.


   .. py:attribute:: model
      :type:  Any
      :value: Ellipsis



