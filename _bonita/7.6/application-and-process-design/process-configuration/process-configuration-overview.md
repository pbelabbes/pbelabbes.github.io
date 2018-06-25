---
layout : doc
title : "Process configuration overview"
version : "7.6"
categories:
  - Application and Process Design
  - Process configuration
order : 83
---
# Process configuration overview

There are two reasons for configuring a process:

* Configuring a process for testing
* Configuring a process before deployment

Before you can run a process from Bonita Studio for testing, you must configure it. The configuration is partly set implicitly by the Deployment and Web 
preferences set as [Bonita Studio preferences]({{"bonita/7.6/application-and-process-design/bonita-bpm-studio-preferences" | relative_url}}) and is partly set explicitly by 
[configuring the process using the configuration wizard]({{"bonita/7.6/application-and-process-design/process-configuration/configuring-a-process" | relative_url}}).

Before you export a process for deployment, you need to set the initial configuration [using the configuration wizard]({{"bonita/7.6/application-and-process-design/process-configuration/configuring-a-process" | relative_url}}). 
This configuration is exported with the process if you check the Configuration option in the export dialog when you 
[build a .bar archive]({{"bonita/7.6/application-and-process-design/import-and-export-a-process" | relative_url}}). 
If you are using the Performance edition, you can [update the configuration after deployment]({{"bonita/7.6/bonita-portal-administration/process-maintenance/processes" | relative_url}}). 
For other editions, you can modify the actor mapping only.
