---
layout : doc
title : "Release notes"
version : "2.0"
categories:

order : 0
---
# Release notes

## Breaking changes

The following changes introduce incompatibility with BCD 1.0:

* For security reasons, pushing AWS user credentials to EC2 instances (as done with BCD 1.0) for cluster autodiscovery is no longer supported. It is replaced by an [IAM role]({{"bcd/2.0/howtos/manage-bonita-stacks/aws_prerequisites" | relative_url}}) assignment on EC2 instances. See `ec2_discovery_iam_role` in the [Scenarios documentation]({{"bcd/2.0/bcd-services-and-scenarios/scenarios" | relative_url}}).
* `bonita_http_api` variable is now set to `false` by default.
* For a better understanding, the `on-premises` value for `bcd_provider` variable has been replaced with `static_inventory`. You may have to update your [BCD scenarios]({{"bcd/2.0/bcd-services-and-scenarios/scenarios" | relative_url}}) accordingly.
* Bonita Docker images have been moved from `roles/bonita/files/docker` directory to `dependencies` directory.
* BCD commands for Provisioning are invoked with `bcd stack` parent command.

## Limitations and known issues

* The same BCD stack cannot be managed with multiple BCD controller instances due to the use of Terraform "local" backend.
* Due to [Ansible issue #35255](https://github.com/ansible/ansible/issues/35255) the warning message "could not match supplied host pattern" is displayed when there is no load balancer required for a noncluster deployment:
```
[WARNING]: Could not match supplied host pattern, ignoring: load_balancer
```


## What's new in 2.0.0 (2018-06-07)

:fa-info-circle: This version is compatible with Bonita 7.7.0.

### New features

* BCD commands for [Living Application Management](_manage_living_application) (`bcd livingapp`)
* Add [Google G Suite Single Sign-On]({{"bcd/2.0/howtos/manage-bonita-stacks/aws_sso" | relative_url}}) (SSO) support
* BCD command to show BCD environment version (`bcd version`)
* [Jenkins standalone example]({{"bcd/2.0/howtos/jenkins_example" | relative_url}}) with sample BCD pipeline
* Scenario [encryption capability]({{"bcd/2.0/howtos/how_to_use_bcd_with_data_encrypted" | relative_url}})

### Enhancements

* Handle `REST_API_DYN_AUTH_CHECKS` environment variable of Bonita Docker image
* Deactivate by default [Bonita HTTP API](https://documentation.bonitasoft.com/bonita/${bonitaDocVersion}/rest-api-authorization#toc9)
* Ports published by the Bonita stack are configurable

### Technology updates

* Upgrade BCD controller with Terraform v0.11.3
* Upgrade BCD controller with Ansible 2.5.0
* Support Provisioning of Ubuntu 16.04 hosts in addition to Ubuntu 14.04

### Bugfixes

* BCD-199 Stack undeploy command fails when Docker is not yet installed on target hosts
