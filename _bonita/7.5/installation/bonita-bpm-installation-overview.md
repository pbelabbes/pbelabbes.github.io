---
layout : doc
title : "Bonita BPM installation overview"
version : "7.5"
categories:
  - Installation
order : 94
---
# Bonita BPM installation overview

Bonita BPM exists in several [editions](http://www.bonitasoft.com/products#versions): Performance, Efficiency, Teamwork, and Community.

For the Bonita BPM Subscription editions: Performance, Efficiency, and Teamwork, you need to [install a license]({{"bonita/7.5/installation/basic-bonita-bpm-platform-installation/licenses" | relative_url}}) during the installation procedure. This license depends on the edition, the deployment environment, the number of cases purchased or the number of cores. 

For the Bonita BPM Community edition, no license is needed.

Bonita BPM Studio <!--{.h2}-->

Bonita BPM Studio contains an embedded test platform that includes an Apache Tomcat application server, an h2 database and the Bonita web application (that itself includes Bonita BPM Engine).

To install Bonita BPM Studio you can either use:

* The installer for your operating system (Windows, Mac OS, Linux).
Used to install Bonita BPM Studio (using a wizard) on your computer. No configuration necessary.
* The OS independent package. Used to manually set up Bonita BPM Studio.
The package contains the individual launchers in one .zip file, and creates the same installation environment as the installers.

To know more, go to [Bonita BPM Studio installation]({{"bonita/7.5/installation/bonita-bpm-studio-installation" | relative_url}}).

<a id="platform"/>

Bonita BPM Platform  <!--{.h2}-->

Bonita BPM Platform can be installed in several ways:

* If you want to migrate an existing installation to the latest version follow the [migration guide]({{"bonita/7.5/installation/migration/migrate-from-an-earlier-version-of-bonita-bpm" | relative_url}}).
* If you want to do a fresh install, get one of our prepackaged bundles that include an Application Server
    * [Tomcat + Bonita BPM]({{"bonita/7.5/installation/basic-bonita-bpm-platform-installation/tomcat-bundle" | relative_url}})
    * [WildFly + Bonita BPM]({{"bonita/7.5/installation/basic-bonita-bpm-platform-installation/wildfly-bundle" | relative_url}})
* If you want to do a custom installation, use the [Deploy bundle]({{"bonita/7.5/installation/basic-bonita-bpm-platform-installation/deploy-bundle" | relative_url}}).


For all options, you will need to [configure]({{"bonita/7.5/installation/basic-bonita-bpm-platform-installation/database-configuration" | relative_url}}) Bonita BPM Engine to work with the database of your choice (e.g. PostgreSQL or Oracle).


{% alert warning %}
Starting from Bonita BPM 7.3.0, there is no more bonita home to store the configuration, all the configuration is in the database. For more information, take a look at [Bonita BPM Platform configuration]({{"bonita/7.5/installation/basic-bonita-bpm-platform-installation/BonitaBPM_platform_setup" | relative_url}})
{% endalert %}


For detailed information on the Supported Environment Matrix, see the [Support Guide](https://customer.bonitasoft.com/support-policies) or [ask to be contacted by our commercial team](http://www.bonitasoft.com/contact-us).
