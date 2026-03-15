srcPy.pipeline.core.pipeline_core_registry
==========================================

.. py:module:: srcPy.pipeline.core.pipeline_core_registry


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.core.pipeline_core_registry.logger


Classes
-------

.. autoapisummary::

   srcPy.pipeline.core.pipeline_core_registry.StepRegistry


Module Contents
---------------

.. py:data:: logger
   :type:  Any
   :value: Ellipsis


.. py:class:: StepRegistry

   step registry class.


   .. py:method:: register(*args, override = False)
      :classmethod:



   .. py:method:: get(stage, name)
      :classmethod:



   .. py:method:: load_plugins(entry_point_group, stage)
      :classmethod:



