srcPy.utils.stat_tests
======================

.. py:module:: srcPy.utils.stat_tests


Classes
-------

.. autoapisummary::

   srcPy.utils.stat_tests.StatTest
   srcPy.utils.stat_tests.StatTestFactory


Functions
---------

.. autoapisummary::

   srcPy.utils.stat_tests.register_test
   srcPy.utils.stat_tests.run_tests
   srcPy.utils.stat_tests.adf_test
   srcPy.utils.stat_tests.kpss_test
   srcPy.utils.stat_tests.ljung_box_test
   srcPy.utils.stat_tests.granger_causality_test
   srcPy.utils.stat_tests.johansen_cointegration_test


Module Contents
---------------

.. py:function:: register_test(name = None)

.. py:class:: StatTest

   Bases: :py:obj:`abc.ABC`


   stat test class.


   .. py:method:: run(data, **kwargs)
      :abstractmethod:



.. py:class:: StatTestFactory

   Factory for creating stat test instances.


   .. py:method:: get_test(test_name)
      :classmethod:



   .. py:method:: run_test(test_name, data, **kwargs)
      :classmethod:



.. py:function:: run_tests(tests, data, parallel = False, max_workers = None)

.. py:function:: adf_test(series, **kwargs)

.. py:function:: kpss_test(series, **kwargs)

.. py:function:: ljung_box_test(series, **kwargs)

.. py:function:: granger_causality_test(x, y, **kwargs)

.. py:function:: johansen_cointegration_test(data, **kwargs)

