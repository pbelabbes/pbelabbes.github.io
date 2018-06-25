---
layout : doc
title : "Organization in Bonita Portal overview"
version : "7.6"
categories:
  - Bonita Portal Administration
  - Organization in Bonita Portal
order : 150
---
# Organization in Bonita Portal overview

In Bonita Portal, a user with the Administrator profile active can view all the parts of an organization including:

* the parent groups
* child groups
* the number and list of users in a group
* the manager of each user
* the email address of a user
* the date and time of the user's last login
* the roles created and the number of users with that role

The Administrator has the right to:

* [import an organization exported from Bonita Studio]({{"bonita/7.6/bonita-portal-administration/organization-in-bonita-portal/organization-maintenance/import-export-an-organization" | relative_url}})
* [export an organization from Bonita Portal]({{"bonita/7.6/bonita-portal-administration/organization-in-bonita-portal/organization-maintenance/import-export-an-organization" | relative_url}})
* [create and delete groups]({{"bonita/7.6/bonita-portal-administration/organization-in-bonita-portal/organization-maintenance/group" | relative_url}})
* [create and delete roles]({{"bonita/7.6/bonita-portal-administration/organization-in-bonita-portal/organization-maintenance/role" | relative_url}})
* [create and manage users]({{"bonita/7.6/bonita-portal-administration/organization-in-bonita-portal/organization-maintenance/manage-users/manage-a-user" | relative_url}}) and manage memberships

**Developer environment:** When you are testing a process locally by running it from Bonita Studio, the default organization defined in the Studio is **automatically published** to the Bonita Portal.

**Production environment:** When you first launch Bonita Portal in a Production environment, there is **no default organization**.
You must [create a user with the Administrator profile]({{"bonita/7.6/installation/basic-bonita-platform-installation/first-steps-after-setup" | relative_url}}). This user can than create and manage the organization.
