srcPy.pipeline.stages.cleaning.execution.batch
==============================================

.. py:module:: srcPy.pipeline.stages.cleaning.execution.batch


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.execution.batch.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.execution.batch.CleanerPipeline


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: CleanerPipeline(steps, mlflow_logger = None)

   cleaner pipeline class.


   .. py:attribute:: steps
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: config
      :type:  Any
      :value: Ellipsis



   .. py:method:: run(df, distributed = False)


   .. py:method:: close()


