---
layout : doc
title : "Bonita Portal overview"
version : "7.7"
categories:
  - Bonita Portal Administration
  - Bonita Portal interface
order : 127
---
# Bonita Portal overview

Most of the Bonita Portal pages are divided into 3 main panes: left, middle and right.

The left pane is for filters, the middle one for lists and the right one for more details about the selected item.

## Default profiles

There are three default profiles available in the Portal: **User**, **Administrator**, and (in the Efficiency, Performance and Enterprise editions) **Process manager**.

The **Administrator** is responsible for the administration of the Portal at tenant level, and particularly for the management of the processes, the organization, the reports, the custom profiles and the Look & Feel.

Example of the Administrator profile interface
![](images/images-6_0/admin_view7.1.png)<!--{.img-responsive}-->

The **Process Manager** shares process management responsibilities with the Administrator for the processes he has been declared as the Process Manager.

The **User** is responsible of performing the tasks for which she is a candidate and also for starting new cases of the processes to which she has access.

Example of the User profile interface
![](images/user_tasklist.png)<!--{.img-responsive}-->

To know more about the use and optimization of the task list, go to [User task list]({{"bonita/7.7/bonita-portal-administration/bonita-portal-interface/user-task-list" | relative_url}}).

## Access to menus

Each profile has access to a different set of single page menus or drop down menus, containing filters and action buttons related to their user rights.

{% alert info %}
**:fa-info-circle:Note**: The tenant administrator, logged as the Technical user, needs to map the Administrator profile with individuals in the company (or groups, or roles) to let the Administrator(s) manage the rest of the organization and other users. See [First steps after setup/Create an Administrator user]({{"bonita/7.7/installation/basic-bonita-platform-installation/first-steps-after-setup" | relative_url}}).
{% endalert %}

See also [Profiles overview]({{"bonita/7.7/application-and-process-design/profiles/profiles-overview" | relative_url}}).  
See also [Custom profiles]({{"bonita/7.7/bonita-portal-administration/user-profiles/custom-profiles" | relative_url}}).
