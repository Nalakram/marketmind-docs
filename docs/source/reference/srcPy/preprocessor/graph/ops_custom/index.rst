srcPy.preprocessor.graph.ops_custom
===================================

.. py:module:: srcPy.preprocessor.graph.ops_custom


Classes
-------

.. autoapisummary::

   srcPy.preprocessor.graph.ops_custom.RSI
   srcPy.preprocessor.graph.ops_custom.SMA
   srcPy.preprocessor.graph.ops_custom.Lags
   srcPy.preprocessor.graph.ops_custom.ZScore
   srcPy.preprocessor.graph.ops_custom.RobustScaler
   srcPy.preprocessor.graph.ops_custom.SentimentLexicon
   srcPy.preprocessor.graph.ops_custom.PairBeta
   srcPy.preprocessor.graph.ops_custom.PairSpread
   srcPy.preprocessor.graph.ops_custom.HalfLife
   srcPy.preprocessor.graph.ops_custom.RollingZ
   srcPy.preprocessor.graph.ops_custom.RollingVol


Functions
---------

.. autoapisummary::

   srcPy.preprocessor.graph.ops_custom.lower_pairs_beta_polars
   srcPy.preprocessor.graph.ops_custom.lower_pairs_spread_polars
   srcPy.preprocessor.graph.ops_custom.lower_half_life_polars
   srcPy.preprocessor.graph.ops_custom.lower_zscore_roll_polars
   srcPy.preprocessor.graph.ops_custom.lower_rolling_vol_polars


Module Contents
---------------

.. py:class:: RSI(**params)

   Bases: :py:obj:`srcPy.preprocessor.graph.ops.RollingOp`


   rsi class.


   .. py:attribute:: NAME
      :type:  str
      :value: Ellipsis



   .. py:method:: validate_params()


   .. py:method:: requires()


   .. py:method:: provides()


   .. py:method:: to_ir()


.. py:class:: SMA(**params)

   Bases: :py:obj:`srcPy.preprocessor.graph.ops.RollingOp`


   sma class.


   .. py:attribute:: NAME
      :type:  str
      :value: Ellipsis



   .. py:method:: validate_params()


   .. py:method:: requires()


   .. py:method:: provides()


   .. py:method:: to_ir()


.. py:class:: Lags(**params)

   Bases: :py:obj:`srcPy.preprocessor.graph.ops.SequenceOp`


   lags class.


   .. py:attribute:: NAME
      :type:  str
      :value: Ellipsis



   .. py:method:: validate_params()


   .. py:method:: requires()


   .. py:method:: provides()


.. py:class:: ZScore(**params)

   Bases: :py:obj:`srcPy.preprocessor.graph.ops.ScalingOp`


   z score class.


   .. py:attribute:: NAME
      :type:  str
      :value: Ellipsis



   .. py:method:: validate_params()


   .. py:method:: requires()


   .. py:method:: provides()


   .. py:method:: state_dict()


.. py:class:: RobustScaler(**params)

   Bases: :py:obj:`srcPy.preprocessor.graph.ops.ScalingOp`


   robust scaler class.


   .. py:attribute:: NAME
      :type:  str
      :value: Ellipsis



   .. py:method:: validate_params()


   .. py:method:: requires()


   .. py:method:: provides()


   .. py:method:: state_dict()


.. py:class:: SentimentLexicon(**params)

   Bases: :py:obj:`srcPy.preprocessor.graph.ops.ElementwiseOp`


   sentiment lexicon class.


   .. py:attribute:: NAME
      :type:  str
      :value: Ellipsis



   .. py:method:: validate_params()


   .. py:method:: requires()


   .. py:method:: provides()


.. py:class:: PairBeta(**params)

   Bases: :py:obj:`srcPy.preprocessor.graph.ops.RollingOp`


   pair beta class.


   .. py:attribute:: NAME
      :type:  str
      :value: Ellipsis



   .. py:method:: validate_params()


   .. py:method:: requires()


   .. py:method:: provides()


.. py:class:: PairSpread(**params)

   Bases: :py:obj:`srcPy.preprocessor.graph.ops.ElementwiseOp`


   pair spread class.


   .. py:attribute:: NAME
      :type:  str
      :value: Ellipsis



   .. py:method:: validate_params()


   .. py:method:: requires()


   .. py:method:: provides()


.. py:class:: HalfLife(**params)

   Bases: :py:obj:`srcPy.preprocessor.graph.ops.RollingOp`


   half life class.


   .. py:attribute:: NAME
      :type:  str
      :value: Ellipsis



   .. py:method:: validate_params()


   .. py:method:: requires()


   .. py:method:: provides()


.. py:class:: RollingZ(**params)

   Bases: :py:obj:`srcPy.preprocessor.graph.ops.ScalingOp`


   rolling z class.


   .. py:attribute:: NAME
      :type:  str
      :value: Ellipsis



   .. py:method:: validate_params()


   .. py:method:: requires()


   .. py:method:: provides()


.. py:class:: RollingVol(**params)

   Bases: :py:obj:`srcPy.preprocessor.graph.ops.RollingOp`


   rolling vol class.


   .. py:attribute:: NAME
      :type:  str
      :value: Ellipsis



   .. py:method:: validate_params()


   .. py:method:: requires()


   .. py:method:: provides()


.. py:function:: lower_pairs_beta_polars(*args, **kwargs)

.. py:function:: lower_pairs_spread_polars(*args, **kwargs)

.. py:function:: lower_half_life_polars(*args, **kwargs)

.. py:function:: lower_zscore_roll_polars(*args, **kwargs)

.. py:function:: lower_rolling_vol_polars(*args, **kwargs)

