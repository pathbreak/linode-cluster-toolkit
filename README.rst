======================
Linode Cluster Toolkit
======================

Linode Cluster Toolkit's goal is to make provisioning and
configuration of large secure clusters on Linode cloud simple for users and 
applications.

The project consists of two main components:

+ **Linode Cluster Toolkit** or **LCT**
  
  LCT is a Python library that provides interfaces for provisioning and 
  configuring clusters using Linode's v4_ and v3_ APIs.
  
.. v4: https://developers.linode.com/v4/introduction
.. v3: https://www.linode.com/api  



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
