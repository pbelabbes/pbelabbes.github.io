---
layout : doc
title : "Organization in Bonita BPM Portal overview"
version : "7.5"
categories:
  - Bonita BPM Portal Administration
  - Organization in Bonita BPM Portal
order : 150
---
# Organization in Bonita BPM Portal overview

In Bonita BPM Portal, a user with the Administrator profile active can view all the parts of an organization including:

* the parent groups
* child groups
* the number and list of users in a group
* the manager of each user
* the email address of a user
* the date and time of the user's last login
* the roles created and the number of users with that role

The Administrator has the right to:

* [import an organization exported from Bonita BPM Studio]({{"bonita/7.5/bonita-bpm-portal-administration/organization-in-bonita-bpm-portal/organization-maintenance/import-export-an-organization" | relative_url}})
* [export an organization from Bonita BPM Portal]({{"bonita/7.5/bonita-bpm-portal-administration/organization-in-bonita-bpm-portal/organization-maintenance/import-export-an-organization" | relative_url}})
* [create and delete groups]({{"bonita/7.5/bonita-bpm-portal-administration/organization-in-bonita-bpm-portal/organization-maintenance/group" | relative_url}})
* [create and delete roles]({{"bonita/7.5/bonita-bpm-portal-administration/organization-in-bonita-bpm-portal/organization-maintenance/role" | relative_url}})
* [create and manage users]({{"bonita/7.5/bonita-bpm-portal-administration/organization-in-bonita-bpm-portal/organization-maintenance/manage-users/manage-a-user" | relative_url}}) and manage memberships

**Developer environment:** When you are testing a process locally by running it from Bonita BPM Studio, the default organization defined in the Studio is **automatically published** to the Bonita BPM Portal.

**Production environment:** When you first launch Bonita BPM Portal in a Production environment, there is **no default organization**.
You must [create a user with the Administrator profile]({{"bonita/7.5/installation/basic-bonita-bpm-platform-installation/first-steps-after-setup" | relative_url}}). This user can than create and manage the organization.
