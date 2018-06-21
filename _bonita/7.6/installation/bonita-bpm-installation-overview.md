---
layout : doc
title : "Bonita installation overview"
version : "7.6"
categories:
  - Installation
order : 94
---
# Bonita installation overview

Bonita exists in several [editions](http://www.bonitasoft.com/bonita-editions): Performance, Efficiency, Teamwork, and Community.

For the Bonita Subscription editions: Performance, Efficiency, and Teamwork, you need to [install a license]({{"bonita/7.6/installation/basic-bonita-platform-installation/licenses" | relative_url}}) during the installation procedure. This license depends on the edition, the deployment environment, the number of cases purchased or the number of cores. 

For the Bonita Community edition, no license is needed.

Bonita Studio <!--{.h2}-->

Bonita Studio contains an embedded test platform that includes an Apache Tomcat application server, an h2 database and the Bonita web application (that itself includes Bonita Engine).

To install Bonita Studio you can either use:

* The installer for your operating system (Windows, Mac OS, Linux).
Used to install Bonita Studio (using a wizard) on your computer. No configuration necessary.
* The OS independent package. Used to manually set up Bonita Studio.
The package contains the individual launchers in one .zip file, and creates the same installation environment as the installers.

To know more, go to [Bonita Studio installation]({{"bonita/7.6/installation/bonita-bpm-studio-installation" | relative_url}}).

<a id="platform"/>

Bonita Platform  <!--{.h2}-->

Bonita Platform can be installed in several ways:

* If you want to migrate an existing installation to the latest version follow the [migration guide]({{"bonita/7.6/installation/migration/migrate-from-an-earlier-version-of-bonita-bpm" | relative_url}}).
* If you want to do a fresh install, get one of our prepackaged bundles that include an Application Server
    * [Tomcat + Bonita]({{"bonita/7.6/installation/basic-bonita-platform-installation/tomcat-bundle" | relative_url}})
    * [WildFly + Bonita]({{"bonita/7.6/installation/basic-bonita-platform-installation/wildfly-bundle" | relative_url}})
* If you want to do a custom installation, use the [Deploy bundle]({{"bonita/7.6/installation/basic-bonita-platform-installation/deploy-bundle" | relative_url}}).


For all options, you will need to [configure]({{"bonita/7.6/installation/basic-bonita-platform-installation/database-configuration" | relative_url}}) Bonita Engine to work with the database of your choice (e.g. PostgreSQL or Oracle).


{% alert warning %}
Starting from Bonita 7.3.0, there is no more bonita home to store the configuration, all the configuration is in the database. For more information, take a look at [Bonita Platform configuration]({{"bonita/7.6/installation/basic-bonita-platform-installation/BonitaBPM_platform_setup" | relative_url}})
{% endalert %}


For detailed information on the Supported Environment Matrix, see the [Support Guide](https://customer.bonitasoft.com/support-policies) or [ask to be contacted by our commercial team](http://www.bonitasoft.com/contact-us).
