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
  
  It supports both Python 3 and Python 2 environments.
  
.. _v4: https://developers.linode.com/v4/introduction
.. _v3: https://www.linode.com/api  


+ **LinodeTool**

  LinodeTool is a command-line tool that uses LCT to provision and configure
  clusters and single nodes. 


Installation
============
Both the toolkit library and LinodeTool are part of the same Python package.

Until this package is published to PyPI, install it using ``pip`` to pull 
from this GitHub repo:

.. code:: bash

    # Python 3
    $ pip3 install git+https://github.com/pathbreak/linode-cluster-toolkit.git

    # Python 2
    $ pip install git+https://github.com/pathbreak/linode-cluster-toolkit.git
    
After code


Features
========





Basic Toolkit API usage
=======================
1. 


LinodeTool usage
=======================

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


Architecture
============
 
Guide to reading and understanding this code
============================================

+ The Toolkit class should be your starting point.

+ Toolkit provides a number of *_service() methods that return an appropriate *Service instance.
  For example, ClusterService provides cluster management services. 
  InventoryService provides inventory storage and querying services.
