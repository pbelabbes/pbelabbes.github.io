---
layout : doc
title : "Log in and log out"
version : "7.6"
categories:
  - Bonita Portal Administration
  - Bonita Portal interface
order : 132
---
# Log in and log out

This page tells you how to log in as a user with a profile and rights attached to that profile.

You can also switch between users with different rights,(e.g. user profile and admin profile), to access different management menus.

Note: to avoid login problems, make sure you empty your browser cache [Empty your cache for different browsers](http://www.wikihow.com/Clear-Your-Browser's-Cache)

## How to log in as a user

If for example, you receive an email with a link to start a case or a task in the Bonita Portal, you will need to log in.

* Enter the login page url, `http://`_`hostname:port`_`/bonita/`, to get to the login page as a user. The default port number is 8080\.
* In the user field, enter the **login**, and the **password** for this user.
* Click on the _**Login button**_.

## How to log out and log back in as another user

* Go to the _**Tool bar**_ at the top of the interface.
* Go to **username** menu (your username in the top right of the screen) and choose _**Logout**_.
* This will log you out and then display the **login form**.
* In the user field, enter the **name** of a different user, enter the **password** for this user.
* Click on the _**Login button**_.

Logging out will send the user back to the login page.

Note: in a system that uses CAS to provide single sign-on, the administrator can remove the logout option. In this case, to log out of the portal you must log out of the CAS system or close your browser.

See also [First steps after setup]({{"bonita/7.6/installation/basic-bonita-platform-installation/first-steps-after-setup" | relative_url}})

See also [Active directory/ldap authentication]({{"bonita/7.6/installation/advanced-bonita-platform-installation/security-and-authentication/active-directory-or-ldap-authentication" | relative_url}})

See also [Accessing Bonita Portal and forms by URL]({{"bonita/7.6/development/bonita-bpm-portal-urls" | relative_url}})