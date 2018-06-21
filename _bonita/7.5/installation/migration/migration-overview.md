---
layout : doc
title : "Migration overview"
version : "7.5"
categories:
  - Installation
  - Migration
order : 126
---
# Migration overview

## Migrating your platform to the new version

You can automatically [migrate the platform from an earlier version of Bonita BPM]({{"bonita/7.5/installation/migration/migrate-from-an-earlier-version-of-bonita-bpm" | relative_url}}). You cannot migrate your platform from a version earlier than 6.0.2\. 
After migration, a process continues to run unchanged. You can modify the process definition later to take advantage of the new features in this version of Bonita BPM.

## Migrating your Bonita BPM Studio

To migrate to a newer version of Bonita BPM Studio, install the new version using the [Studio installer wizard]({{"bonita/7.5/installation/bonita-bpm-studio-installation" | relative_url}}) for your operating system.
If you want to keep the artifacts in your workspace, select the option to migrate your workspace. 

**Warning:** if you do not migrate your workspace, or if you use the OS-independent archive to install the new Bonita BPM Studio, 
your workspace is not automatically migrated. In this case, you must manually export each item from the older Bonita BPM Studio and import it into the newer version. 

## Migrating your process definitions

A process definition created using Bonita BPM 6.x can be run on this version after the [platform migration]({{"bonita/7.5/installation/migration/migrate-from-an-earlier-version-of-bonita-bpm" | relative_url}}). 
However, you might choose to update the process definition to take advantage of new features. 
To update a process definition, export it from the older version of Bonita BPM Studio as a `.bos` file, then import it into the 
newer version and update it.

Note: you cannot import a process definition `.bos` file into a version of Bonita BPM Studio that is older than the version 
that was used to create it.

You can import a .bos file containing a process definiiton from a Bonita BPM 6.x or Bonita Open Solution 5.x. 
The [guided migration]({{"bonita/7.5/application-and-process-design/process-modeling/diagrams/migrate-a-process-from-bonita-open-solution-5-x" | relative_url}}) converts the 5.x process definition to use the legacy 6.x tooling so that the process can run on a Bonita BPM 7.x platform. 
You can modify the process definition later to take advantage of the new features in this version of Bonita BPM.
