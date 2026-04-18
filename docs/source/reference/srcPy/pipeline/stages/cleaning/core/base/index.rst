srcPy.pipeline.stages.cleaning.core.base
========================================

.. py:module:: srcPy.pipeline.stages.cleaning.core.base


Exceptions
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.core.base.DataValidationError


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.core.base.PolarsDataFrame
   srcPy.pipeline.stages.cleaning.core.base.CleaningStep
   srcPy.pipeline.stages.cleaning.core.base.StepRegistry


Module Contents
---------------

.. py:class:: PolarsDataFrame

.. py:class:: CleaningStep

   Bases: :py:obj:`abc.ABC`


   cleaning step class.


   .. py:method:: apply(df)
      :abstractmethod:



.. py:class:: StepRegistry

   step registry class.


   .. py:method:: register(name, step_cls)
      :classmethod:



   .. py:method:: get(name)
      :classmethod:



   .. py:method:: freeze()
      :classmethod:



   .. py:method:: thaw()
      :classmethod:



   .. py:method:: list_registered()
      :classmethod:



.. py:exception:: DataValidationError(message, details = None)

   Bases: :py:obj:`Exception`


   Exception raised when data validation occurs.


   .. py:attribute:: message
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: details
      :type:  Any
      :value: Ellipsis



