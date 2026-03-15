srcPy.utils.dataset_builders
============================

.. py:module:: srcPy.utils.dataset_builders


Attributes
----------

.. autoapisummary::

   srcPy.utils.dataset_builders.TargetType


Classes
-------

.. autoapisummary::

   srcPy.utils.dataset_builders.TimeSeriesDataset


Functions
---------

.. autoapisummary::

   srcPy.utils.dataset_builders.build_loader
   srcPy.utils.dataset_builders.build_train_val_loaders


Module Contents
---------------

.. py:data:: TargetType
   :type:  Any
   :value: Ellipsis


.. py:class:: TimeSeriesDataset(df, *, seq_len, horizon, target_col = 'close', ticker_col = 'ticker', target_type = 'regression', transform = None, target_transform = None, dtype = ..., device = None)

   Bases: :py:obj:`torch.utils.data.Dataset`


   time series dataset class.


   .. py:attribute:: data
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: target
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: seq_len
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: horizon
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: target_type
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: transform
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: target_transform
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: starts
      :type:  list[int]
      :value: Ellipsis



   .. py:method:: __len__()


   .. py:method:: __getitem__(idx)


.. py:function:: build_loader(df, *, seq_len, horizon, batch_size = 128, shuffle = True, num_workers = 4, pin_memory = True, drop_last = True, target_col = 'close', ticker_col = 'ticker', target_type = 'regression', distributed = False, rank = None, world_size = None, transform = None, target_transform = None, dtype = ..., device = None, **loader_kwargs)

.. py:function:: build_train_val_loaders(train_df, val_df, *, seq_len, horizon, batch_size = 128, num_workers = 4, **common_kwargs)

