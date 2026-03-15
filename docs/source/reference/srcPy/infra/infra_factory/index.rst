srcPy.infra.infra_factory
=========================

.. py:module:: srcPy.infra.infra_factory


Attributes
----------

.. autoapisummary::

   srcPy.infra.infra_factory.creator


Classes
-------

.. autoapisummary::

   srcPy.infra.infra_factory.DataSourceFactory


Functions
---------

.. autoapisummary::

   srcPy.infra.infra_factory.register_source
   srcPy.infra.infra_factory.unregister_source
   srcPy.infra.infra_factory.get_creator
   srcPy.infra.infra_factory.list_sources


Module Contents
---------------

.. py:function:: register_source(name, creator)

.. py:function:: unregister_source(name)

.. py:function:: get_creator(source_type)

.. py:function:: list_sources()

.. py:class:: DataSourceFactory

   Factory for creating data source instances.


   .. py:method:: create(source_type, /, **kwargs)
      :staticmethod:



.. py:data:: creator
   :type:  Any
   :value: Ellipsis


