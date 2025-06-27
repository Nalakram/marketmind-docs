srcPy.utils.exceptions
======================

.. py:module:: srcPy.utils.exceptions


Exceptions
----------

.. autoapisummary::

   srcPy.utils.exceptions.IBConnectionError
   srcPy.utils.exceptions.DataFetchError
   srcPy.utils.exceptions.NoDataError
   srcPy.utils.exceptions.DataValidationError
   srcPy.utils.exceptions.ConfigValidationError
   srcPy.utils.exceptions.PreprocessingError
   srcPy.utils.exceptions.ModelTrainingError
   srcPy.utils.exceptions.TradingExecutionError
   srcPy.utils.exceptions.APIConnectionError
   srcPy.utils.exceptions.InvalidInputError
   srcPy.utils.exceptions.StatisticalTestError


Module Contents
---------------

.. py:exception:: IBConnectionError(message = 'Failed to connect to Interactive Brokers', details = None)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


   .. py:attribute:: details
      :type:  _typeshed.Incomplete


.. py:exception:: DataFetchError(message = 'Error fetching data', details = None)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


   .. py:attribute:: details
      :type:  _typeshed.Incomplete


.. py:exception:: NoDataError(symbol, details = None)

   Bases: :py:obj:`DataFetchError`


   Common base class for all non-exit exceptions.


.. py:exception:: DataValidationError(message, details = None)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


   .. py:attribute:: details
      :type:  _typeshed.Incomplete


.. py:exception:: ConfigValidationError(message, validation_errors = None)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


   .. py:attribute:: validation_errors
      :type:  _typeshed.Incomplete


.. py:exception:: PreprocessingError(message, details = None)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


   .. py:attribute:: details
      :type:  _typeshed.Incomplete


.. py:exception:: ModelTrainingError(message, details = None)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


   .. py:attribute:: details
      :type:  _typeshed.Incomplete


.. py:exception:: TradingExecutionError(message, details = None)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


   .. py:attribute:: details
      :type:  _typeshed.Incomplete


.. py:exception:: APIConnectionError(message, details = None)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


   .. py:attribute:: details
      :type:  _typeshed.Incomplete


.. py:exception:: InvalidInputError(message = 'Invalid input provided', details = None)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


   .. py:attribute:: details
      :type:  _typeshed.Incomplete


.. py:exception:: StatisticalTestError(message = 'Statistical test execution failed', details = None)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


   .. py:attribute:: details
      :type:  _typeshed.Incomplete


