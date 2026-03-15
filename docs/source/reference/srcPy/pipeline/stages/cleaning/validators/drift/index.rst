srcPy.pipeline.stages.cleaning.validators.drift
===============================================

.. py:module:: srcPy.pipeline.stages.cleaning.validators.drift


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.validators.drift.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.validators.drift.BaseDriftTest
   srcPy.pipeline.stages.cleaning.validators.drift.KSTest
   srcPy.pipeline.stages.cleaning.validators.drift.DriftDetectionStep


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: BaseDriftTest

   base drift test class.


   .. py:method:: compute(curr, ref)
      :abstractmethod:



.. py:class:: KSTest

   Bases: :py:obj:`BaseDriftTest`


   ks test class.


   .. py:method:: compute(curr, ref)


.. py:class:: DriftDetectionStep(mlflow_logger, enabled = True, reference_data = None, threshold = 0.05, columns = None, test = None, strict = True)

   Bases: :py:obj:`srcPy.pipeline.stages.cleaning.core.base.CleaningStep`


   drift detection step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: enabled
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: reference_data
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: threshold
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: columns
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: test
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: strict
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


