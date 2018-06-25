---
layout : doc
title : "Build a process for deployment"
version : "7.5"
categories:
  - Application and Process Design
order : 92
---
# Build a process for deployment

When a process is ready for deployment, build an archive file in Bonita BPM Studio that can be installed in Bonita BPM Portal.
You also need to initialize the organization information needed in Bonita BPM Portal.

## Build a process for deployment

A process is deployed by installing a business archive (.bar) file in Bonita BPM Portal.
To create the business archive:

1. Choose **Build...** from the **Server** menu.
2. Select the process to be exported.
3. Specify whether you want to export a configuration with the process. 
Exporting a configuration will export all the information and other items that you configured, including connectors and dependencies.
4. Specify the location where the .bar file will be created. The filename is determined by the process name and cannot be changed at this stage.
5. Click **Finish**. The business archive is created.

You can now [install the process in Bonita BPM Portal]({{"bonita/7.5/bonita-bpm-portal-administration/process-maintenance/processes" | relative_url}}).

## Initialize the organization in Bonita BPM Portal

To prepare your production system (unless you are using a Subscription editions and the LDAP synchronizer), 
you must create the organization that you need for all the processes that will be deployed, export it from Bonita BPM Studio,
and import it into Bonita BPM Portal. 

To export the organization, go to the **Organization** menu and choose **Export...**. You
can then [import the organization into Bonita BPM Portal]({{"bonita/7.5/bonita-bpm-portal-administration/organization-in-bonita-bpm-portal/organization-maintenance/import-export-an-organization" | relative_url}}). After the organization is imported into Bonita BPM Portal, 
you can [manage the groups]({{"bonita/7.5/bonita-bpm-portal-administration/organization-in-bonita-bpm-portal/organization-maintenance/group" | relative_url}}), [roles]({{"bonita/7.5/bonita-bpm-portal-administration/organization-in-bonita-bpm-portal/organization-maintenance/role" | relative_url}}), and [users]({{"bonita/7.5/bonita-bpm-portal-administration/organization-in-bonita-bpm-portal/organization-maintenance/manage-users/manage-a-user" | relative_url}}) in the organization.
