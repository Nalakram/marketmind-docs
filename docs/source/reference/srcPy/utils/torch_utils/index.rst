srcPy.utils.torch_utils
=======================

.. py:module:: srcPy.utils.torch_utils


Functions
---------

.. autoapisummary::

   srcPy.utils.torch_utils.set_logging_level
   srcPy.utils.torch_utils.set_perf_flags
   srcPy.utils.torch_utils.seed_everything
   srcPy.utils.torch_utils.init_weights
   srcPy.utils.torch_utils.get_device
   srcPy.utils.torch_utils.autocast


Module Contents
---------------

.. py:function:: set_logging_level(level)

.. py:function:: set_perf_flags(precision_flags = None)

.. py:function:: seed_everything(seed = 42, *, deterministic = True, warn_only = False, precision_flags = None, return_generator = False)

.. py:function:: init_weights(module, mode = 'xavier_uniform', generator = None)

.. py:function:: get_device(preferred_idx = None)

.. py:function:: autocast(enabled = True, dtype = ..., device_type = None)

