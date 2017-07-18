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
integrating with. Depending on your particular application's requirements
or depending on the infrastructure already available to you, 
you can **optionally** install one or more of the following software that
LCT is capable of integrating with:

+ **HashiCorp Vault** for enterprise grade secrets management

  See `Install Vault`_ for installation procedure.
  
+ **Celery** for distributed task execution

  Cluster creation can be a time consuming task. LCT can integrate with
  Celery's concurrent task execution capabilities to make the process
  faster, perform retries with exponential back-offs in case of failures,
  and store a list of failed tasks for later retries.
  
  See `Install Celery`_ for installation.
  
+ A **database** for cluster inventory and state storage, and querying

  LCT can integrate with any of the following databases:
  
  - **TinyDB**
    A simple document database. See `TinyDB Installation`_. LCT uses this
    database for its storage needs by default.
    
  - **MongoDB**
    Popular, highly scalable document database. See `MongoDB Installation`_.
    
  - **MySQL / MariaDB**
    See `MySQL Installation`_ or `MariaDB Installation`_.
    
  - **PostgreSQL**
    See `PostgreSQL Installation`_.
    
  - **SQLite**
    There is no installation required for the database itself, but 
    see `SQLite Installation`_ for some useful tools and utilities.


Features
========





Basic Toolkit API usage
=======================
1. Basic cluster creation

.. code:: python
    from lct import Toolkit, ToolkitContext
    from lct.clusters.clusterplan import ClusterPlan

    # Create a toolkit configuration to configure the 
    # providers the toolkit uses for providing its services.
    # An empty configuration makes the toolkit select the simplest behavior
    # for all services - secrets are handled by the simple secrets provider,
    # cluster state and inventories are stored to local filesystem as JSON files
    # via TinyDB, tasks are executed by a simple sequential or multithreaded
    # queue.
    tkconf = {}
    tk = Toolkit(tkconf)

    # Create a ToolkitContext to specify the application and customer context
    # for any cluster operaiton. This is primarily stored as the context for
    # storing cluster state and inventory information.
    tkctx = ToolkitContext('testapp', 'me')

    # Specify a cluster plan. This can be a simple dict or loaded from a YAML or JSON file. 
    plandict = {
        'name' : 'testcluster',
        'regions': [
            {
                'region' : 'us-east-1a',
                'nodes' : [
                    {
                        'name': 'nodeplan1',
                        'type': 'Linode 1024',
                        'count': 2,
                        'distribution' : 'linode/ubuntu16.04lts'
                    }
                ]
            }
        ]
    }
    plan = ClusterPlan(plandict)

    tk.cluster_service().create_cluster(tkctx, plan, 'My First Cluster', 'mycluster1')



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
.. _`Install Celery`: http://www.celeryproject.org/install/
.. _`TinyDB Installation`: https://tinydb.readthedocs.io/en/latest/getting-started.html#installing-tinydb
.. _`MongoDB Installation`: https://docs.mongodb.com/manual/installation/
.. _`MySQL Installation`: https://dev.mysql.com/downloads/
.. _`MariaDB Installation`: https://mariadb.com/kb/en/mariadb/getting-installing-and-upgrading-mariadb/
.. _`PostgreSQL Installation`: https://www.postgresql.org/download/
.. _`SQLite Installation`: https://www.sqlite.org/download.html
