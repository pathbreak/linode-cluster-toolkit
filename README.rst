======================
Linode Cluster Toolkit
======================



Features
========



Installation
============



Basic Usage
===========

Single node

Basic cluster


Cluster Plans
=============

Regions and Nodes
^^^^^^^^^^^^^^^^^

Storage Plans
^^^^^^^^^^^^^


Cardinality models
==================

<TODO describe Toolkit, ToolkitConfiguration and ToolkitContext cardinalities with examples, such
 as how to share the same database or same task queues, etc>



 
Guide to reading and understanding this code
============================================

+ The Toolkit class should be your starting point.

+ Toolkit provides a number of *_service() methods that return an appropriate *Service instance.
  For example, ClusterService provides cluster management services. 
  InventoryService provides inventory storage and querying services.
