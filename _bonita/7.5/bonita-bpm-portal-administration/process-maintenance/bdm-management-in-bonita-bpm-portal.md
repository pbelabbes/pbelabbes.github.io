---
layout : doc
title : "BDM Management in Bonita BPM Portal"
version : "7.5"
categories:
  - Bonita BPM Portal Administration
  - Process maintenance
order : 141
---
# BDM Management in Bonita BPM Portal

Processes using Business Objects with persisted data need to run with a Business Data Model deployed in the Bonita BPM Portal.
Only one model can be deployed at a time in the Portal, so make sure it contains the Business object definition used in all processes that will run within this tenant.

The Business objects must match the structure used by the deployed processes. Make sure that when modifying the Business Model, the process is modified accordingly.


1. To import the Business Data Model created in Bonita BPM Studio, first [export the Business Data Model]({{"bonita/7.5/application-and-process-design/data/define-and-deploy-the-bdm" | relative_url}}) from Bonita BPM Studio where it was designed.
2. In the Bonita BPM Portal, log in as the technical user (default login 'install', default password 'install').
3. Go to the **BPM Services** menu.
4. Click on **Pause** to [pause]({{"bonita/7.5/bonita-bpm-portal-administration/process-maintenance/pause-and-resume-bpm-services" | relative_url}}) the tenant.

{% alert info %}
**:fa-info-circle: Note:** The deployment of a Business Data Model requires pausing the service during the operation, so that the update can be performed without affecting ongoing processes. 
{% endalert %}

5. When the service is paused, go to the **Business Data Model** menu.
6. A page called **Import and activate a new Business Data Model** is displayed.
7. Choose the file containing the Business Data Model exported from the Bonita BPM Studio, and click on _**Activate**_.
8. A warning is displayed:

{% alert warning %}
**:fa-exclamation-triangle: Warning:** The Business Data Model will now be installed.
{% endalert %}

Please note that existing business database tables will be modified definitively. This action cannot be reversed. It is highly recommended to back up the database before proceeding.
9. The Portal will load the file, retrieve the object definition and enable processes to use them at runtime. The portal will also create or update the database schema (set of tables, columns, indexes...)
in the business database, so as to store business objects appropriately when modified by processes. 
10. The Business Data Model will now be installed.
11. Go to the **BPM Services** menu.
12. Click on **Resume** to [resume tenant activity]({{"bonita/7.5/bonita-bpm-portal-administration/process-maintenance/pause-and-resume-bpm-services" | relative_url}}).

{% alert warning %}
**:fa-exclamation-triangle: Warning:**  Since business continually evolves, you may need to make some changes to a BDM already in production.
Bonita uses Hibernate for data persistence, therefore some changes are handled well, like adding new objects or attributes, but some others, like changing the type of an attribute, we cannot guarantee so far.
In such cases, you will have to implement the change on your own, through careful actions in a staging environment, and after the backup of your database.
This limitation is well known and will be addressed in a future Bonita version.
{% endalert %}
