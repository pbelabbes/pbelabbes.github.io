---
layout : doc
title : "Pools and lanes"
version : "7.7"
categories:
  - Application and Process Design
  - Process modeling
  - Diagrams
order : 17
---
# Pools and lanes

A pool is a container for a process in a diagram.   
A lane is a division of a pool (think of swimlanes in a swimming pool).   
You can use lanes to group elements of a pool that are functionally related.   
Typically, a lane contains all the tasks assigned to an actor.

When you create a new diagram it contains one pool, which contains one lane. You can add other lanes to the pool, and you can add other pools.

For a pool, you can configure the following:

* Name, description, and version number: This information identifies the pool. The name must be unique withing a repository. The pool version number is really the process version number. Update the version number when you make major changes to the process. There is no link between the pool version number and the diagram version number.
* Actors: An actor represents the user who will carry out tasks in the pool. [Configure the actors]({{"bonita/7.7/application-and-process-design/process-modeling/actors" | relative_url}}) that participate in the process. An actor must be defined at pool level before it can be assigned to a lane or task.
* Data: A variable is a container for data used in the process. [Create the variables]({{"bonita/7.7/application-and-process-design/define-access-control-on-business-objects/specify-data-in-a-process-definition" | relative_url}}) that will be used in your process. You can also create variables at task or form level.
* Connectors: A connector links a process to an external information source. [Specify the connectors]({{"bonita/7.7/application-and-process-design/connectivity/connectivity-overview" | relative_url}}) used in the process. You can also specify a connector at lane or task level, but if a connector is used more than once it is better to define it at pool level.
* Parameters: A parameter is like a variable but has a value that is fixed for a deployment of a process. [Define the parameters]({{"bonita/7.7/application-and-process-design/define-access-control-on-business-objects/parameters" | relative_url}}) of your process. 
* Documents: You can attach [documents]({{"bonita/7.7/application-and-process-design/define-access-control-on-business-objects/documents" | relative_url}}) to a process. List the documents that attached to the process.
* Search: A search index is used in the Portal to find a specific instance of a process. [Specify the search indexes]({{"bonita/7.7/bonita-portal-administration/search-index" | relative_url}}) associated with the process.

The items configured for a lane supplement or override those defined for the pool. You only need to configure something at lane level if is not already defined at pool level, or if you want to override the definition. Note that nested lanes are not supported.  

For a lane, you can configure the following:

* Name and description
* Actors: From the actors defined for the pool, [specify the actors]({{"bonita/7.7/application-and-process-design/process-modeling/actors" | relative_url}}) assigned to this lane. You can also [configure an actor filter]({{"bonita/7.7/application-and-process-design/process-modeling/actors" | relative_url}}) to make the actor assignment more specific.
* Data: [Define the variables]({{"bonita/7.7/application-and-process-design/define-access-control-on-business-objects/specify-data-in-a-process-definition" | relative_url}}) needed in the lane. You can also define variables as task level.
* Connectors: [Specify the connectors]({{"bonita/7.7/application-and-process-design/connectivity/connectivity-overview" | relative_url}}) used in the lane. You can also specify a connector at task level, but if a connector is used more than once it is better to define it at pool or lane level.
* Parameters (Enterprise, Performance, Efficiency, and Teamwork editions): [Define the parameters]({{"bonita/7.7/application-and-process-design/define-access-control-on-business-objects/parameters" | relative_url}}) of the lane. A parameter is like a variable but has a value that is fixed for a deployment of a process.
* Documents: List the [documents]({{"bonita/7.7/application-and-process-design/define-access-control-on-business-objects/documents" | relative_url}}) that are attached to the process.
