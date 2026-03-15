srcPy.pipeline.stages.cleaning.validators.io
============================================

.. py:module:: srcPy.pipeline.stages.cleaning.validators.io


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.validators.io.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.cleaning.validators.io.FSInterface
   srcPy.pipeline.stages.cleaning.validators.io.LocalFS
   srcPy.pipeline.stages.cleaning.validators.io.IOValidationStep


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: FSInterface

   fs interface class.


   .. py:method:: get_size(path)
      :abstractmethod:



.. py:class:: LocalFS

   Bases: :py:obj:`FSInterface`


   local fs class.


   .. py:method:: get_size(path)


.. py:class:: IOValidationStep(mlflow_logger, file_path, format = None, max_size_bytes = ..., fs = None)

   Bases: :py:obj:`srcPy.pipeline.stages.cleaning.core.base.CleaningStep`


   io validation step class.


   .. py:attribute:: mlflow_logger
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: file_path
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: format
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: max_size_bytes
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: fs
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: supported_formats
      :type:  Any
      :value: Ellipsis



   .. py:method:: apply(df)


   .. py:method:: __del__()


