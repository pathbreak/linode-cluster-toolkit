  
  **Note**: This project is still under active feature development and a production-ready 
  release is expected around July 26 2017. Until then, please expect bugs and
  use caution while using it.

======================
Linode Cluster Toolkit
======================

The Linode Cluster Toolkit project's goal is to make provisioning and
configuration of large secure clusters on Linode cloud simple for users and 
applications. 

.. contents:: :local:

Overview
--------

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



Features
========

+ Cluster Provisioning

  + all cluster resources and configurations are described in `Cluster Plans`_
  
  + cross-region clusters
  
  + can provision Linodes, NodeBalancers, Disks, Block Stores

  + private cloud [Under implementation]
  
  + create clusters from cluster plans using Ansible module [Planned]

  + create clusters from shell scripts using shell scripts wrapper [Planned]
  
+ Cluster Configuration 

  + oriented towards making big data deployments on Linode easy

  + configure using cloud-init [Under implementation]

  + configure using Ansible module

  + configure using StackScripts

  + Hostnames [Under implementation]

  + dynamic firewall configuration across multiple nodes based on deployed software [Planned]

  + advanced DNS topologies, split-horizon DNS provisioning [Planned]

  + bundled cluster plan templates for big data stacks [Planned]

+ Security

  + secure by default configurations for all provisioned nodes

  + all nodes configured with tight firewall rules - drop all incoming and outgoing traffic by default (except SSH)

  + all nodes have SSH password authentication disabled

  + integrate with secrets management providers like HashiCorp Vault [Under implementation]
  
  
+ Cluster Operations

  + clusters are treated first-level concepts 

  + start cluster, stop cluster

  + support cluster orchestration (such as shutting down in particular order) [Under implementation]
    
+ Inventory Operations

  + cluster state and node information are persisted to storage backends

  + support for multiple storage backends

  + tagging and querying support
  
+ Single Node Operations

  + one-liners to create and delete node


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
    

Installation of 3rd party integrations
--------------------------------------
    
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




Basic Toolkit API usage
=======================

Basic cluster creation
^^^^^^^^^^^^^^^^^^^^^^

An important concept of LCT project is a *Cluster Plan*. A Cluster Plan
is a description of all the nodes, nodebalancers, other resources and 
configurations to apply to them.

See `Cluster Plans`_ for examples and details of cluster plans.

The snippet below creates a simple cluster plan consisting of just 2 
nodes in 1 region.

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
    
    tk.initialize()

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

    # Create the cluster.
    tk.cluster_service().create_cluster(tkctx, plan, 'My First Cluster', 'mycluster1')



LinodeTool usage
================

Basic cluster creation
^^^^^^^^^^^^^^^^^^^^^^
.. code:: bash

    $ linodetool cluster create 'ha-wordpress' ha-wordpress-plan.yaml



Single node creation
^^^^^^^^^^^^^^^^^^^^
Creation of a secure node is as simple as:

.. code:: bash

    $ linodetool node create newark '1gb' 'ubuntu 16.04 lts'
    
But before that can work, LinodeTool requires a one-time entry of two 
pieces of credentials:

+ A personal access token to use Linode's API
  
  You can obtain a personal access token by logging into 
  https://cloud.linode.com with your Linode username and 
  password, navigating to `My Profile > Integrations > Personal Access Tokens`
  `> Create a Personal Access Token`, setting `Linodes` access to one of
  Create/Modify/Delete, and press Create.

  The web application displays a personal access token. Copy that and store
  it in LinodeTool's secrets storage using this command:

  .. code:: bash

      $ linodetool secret set personal-token <YOUR PERSONAL ACCESS TOKEN>
    
  Note that LinodeTool's default secrets
  store is an unencrypted insecure one. If you want to store more securely,
  create a toolkit configuration and specify a more secure secrets provider.
  
+ An SSH public key.

  If you don't have a SSH public key (usually named as ``~/.ssh/id_rsa.pub``, create one:

  .. code:: bash
  
      $ ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ''
  
  Then add it to LinodeTool's secrets store:
  
  .. code:: bash
  
      $ linodetool secret set default-root-ssh-public-key ~/.ssh/id_rsa


Cluster Plans
=============

Examples
^^^^^^^^
Two example cluster plans for large clusters:

1. https://gist.github.com/pathbreak/59c638db0fd95c84c0f655df145ba0ac

   This is a cluster plan for a cross-region, highly-available, disaster-recoverable 
   82-node WordPress setup involving Apache web servers with WordPress, Memcached, 
   MySQL cluster with NDB, Block Stores and NodeBalancers.
   
2. https://gist.github.com/pathbreak/eb7242a48024b54101b432049116ae7e

   This is a cluster plan for a 52-node big data IoT system involving Spark Streaming, 
   Kafka input pipelines in multiple regions, a PostgreSQL cluster, 
   high memory instances and block stores.
   
More details about cluster plans are in the subsections below.

Regions and Nodes
^^^^^^^^^^^^^^^^^
TODO

Storage Plans
^^^^^^^^^^^^^
TODO



Cardinality models
==================

<TODO describe Toolkit, ToolkitConfiguration and ToolkitContext cardinalities with examples, such
 as how to share the same database or same task queues, etc>


Architecture
============

.. image:: https://github.com/pathbreak/linode-cluster-toolkit/blob/master/docs/images/toolkit_architecture.png
 
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
