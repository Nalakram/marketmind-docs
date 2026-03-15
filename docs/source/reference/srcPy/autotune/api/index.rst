srcPy.autotune.api
==================

.. py:module:: srcPy.autotune.api


Classes
-------

.. autoapisummary::

   srcPy.autotune.api.AutoTuner


Functions
---------

.. autoapisummary::

   srcPy.autotune.api.autotune


Module Contents
---------------

.. py:function:: autotune(objective_fn, search_space, *, budget = 10, seed = None)

.. py:class:: AutoTuner(search_space = None, *, metric = None, budget = 10, seed = None)

   auto tuner class.


   .. py:attribute:: search_space
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: metric
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: budget
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: seed
      :type:  Any
      :value: Ellipsis



   .. py:method:: run(objective_fn)


   .. py:method:: evaluate(df_prices, preproc_spec, params)


   .. py:method:: tune(df_prices, preproc_spec)


