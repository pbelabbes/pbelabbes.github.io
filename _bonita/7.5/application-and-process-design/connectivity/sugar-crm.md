---
layout : doc
title : "SugarCRM"
version : "7.5"
categories:
  - Application and Process Design
  - Connectivity
order : 67
---
# SugarCRM 

SugarCRM version API v4

Available Sugar connectors are:

* Create Object - Create a SugarCRM object using API v4
* Delete Object - Delete a SugarCRM object using API v4
* Delete Several Objects - Delete several SugarCRM objects by their ids using API v4
* Query Objects - Execute a query on SugarCRM
* Retrieve Object - Retrieve an object from SugarCRM using API v4
* Retrieve Several Objects - Retrieve several objects from a SugarCRM server using API v4
* Update an Object - Update a SugarCRM object using API v4

Parameters are:

* Type of object you want to retrieve (e.g.: Accounts)
* List of objects identifiers
* List of fields of the object (e.g.: Name, Phone)
* Update object - Update a Sugar object.

Parameters are:

* Type of object you want to update (e.g.: Accounts)
* Object identifier
* Map of fields of the object to update (e.g.: Name = MyNewName, Phone = 1234)

All connectors have these required parameters in common:

* Username
* Password
* Sugar address (url server)
