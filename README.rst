======================
Linode Cluster Toolkit
======================

The Linode Cluster Toolkit project's goal is to make provisioning and
configuration of large secure clusters on Linode cloud simple for users and 
applications. 

The project consists of two main components:

+ **Linode Cluster Toolkit** or **LCT**
  
  LCT is a Python library that provides interfaces for provisioning,  
  configuring and querying clusters. See the `Architecture`_ diagram for
  a list of interfaces it supports.
  
  LCT's interfaces and functionality are designed to be useful for a wide spectrum
  of client applications - from simple command-line tools and scripts to 
  multi-tenant SaaS systems and web applications. 
  
  This is achieved by providing multiple implementations for every service - 
  while one implementation can be extremely simple and suitable for a single user 
  to use on their personal computer, another implementation may integrate
  with complex software which provide production grade services making it suitable
  for large multi-tenant web applications and SaaS systems.
  
  LCT uses and integrates with Linode's v4_ and v3_ APIs, StackScripts_,
  optionally with well-known tools like cloud-init_ and Ansible, 
  purpose-built software like HashiCorp Vault for secrets management and 
  Celery for task queuing, and SQL databases for cluster information 
  storage and querying.  

  It supports both Python 3 and Python 2 environments.
  

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
    
    
LCT does not install any of the other 3rd party software it's capable of 
integrating with. Depending on your particular application's requirements, 
you can **optionally** install one or more of the following software that
LCT is capable of integrating with:

+ **HashiCorp Vault** for enterprise grade secrets management

  See `Install Vault`_ for installation procedure.
  
+ **Celery** for distributed task execution

  Cluster creation can be a time consuming task. LCT can integrate with
  Celery's concurrent task execution capabilities to make the process
  faster, perform retries with exponential back-offs in case of failures,
  and store a list of failed tasks for later retries.
  
+ A **database** for cluster inventory and state storage, and querying

  LCT can integrate with any of the following databases:
  
  - **TinyDB**
    A simple document database. See `TinyDB Installation`_.
    
  - 


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



.. _v4: https://developers.linode.com/v4/introduction
.. _v3: https://www.linode.com/api  
.. _StackScripts: https://www.linode.com/stackscripts
.. _cloud-init: https://cloud-init.io/
.. _`Install Vault`: https://www.vaultproject.io/docs/install/index.html
.. _`TinyDB Installation`: https://tinydb.readthedocs.io/en/latest/getting-started.html#installing-tinydb
