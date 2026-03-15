srcPy.pipeline.stages.preprocessing
===================================

.. py:module:: srcPy.pipeline.stages.preprocessing


Submodules
----------

.. toctree::
   :maxdepth: 1

   /reference/srcPy/pipeline/stages/preprocessing/aliases/index
   /reference/srcPy/pipeline/stages/preprocessing/explainability_step/index
   /reference/srcPy/pipeline/stages/preprocessing/scaling_step/index
   /reference/srcPy/pipeline/stages/preprocessing/sentiment_step/index
   /reference/srcPy/pipeline/stages/preprocessing/sequence_step/index
   /reference/srcPy/pipeline/stages/preprocessing/technical_step/index
   /reference/srcPy/pipeline/stages/preprocessing/temporal_step/index
   /reference/srcPy/pipeline/stages/preprocessing/text_embedding_step/index
   /reference/srcPy/pipeline/stages/preprocessing/topic_modeling_step/index


Attributes
----------

.. autoapisummary::

   srcPy.pipeline.stages.preprocessing.new_step
   srcPy.pipeline.stages.preprocessing.AVAILABLE_STEPS


Classes
-------

.. autoapisummary::

   srcPy.pipeline.stages.preprocessing.StepFactory


Package Contents
----------------

.. py:class:: StepFactory

   Factory for creating step instances.


   .. py:method:: register(name, step_cls)
      :classmethod:



   .. py:method:: get(name)
      :classmethod:



   .. py:method:: create(name, cfg)
      :classmethod:



.. py:data:: new_step
   :type:  Any
   :value: Ellipsis


.. py:data:: AVAILABLE_STEPS
   :type:  Any
   :value: Ellipsis


