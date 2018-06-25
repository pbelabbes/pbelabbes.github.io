---
layout : doc
title : "Log in with CAS"
version : "7.5"
categories:
  - Development
  - Engine API
order : 195
---
# Log in with CAS

{% alert info %}
**Note:** For Performance and Efficiency editions only.
{% endalert %}

Depending on your underlying authentication service, you may need to provide other information with the API in order to log in. A login method with a map enables you to provide the set of credentials that the authentication service requires. 
The following example can be used if you are [using Bonita BPM with CAS]({{"bonita/7.5/installation/advanced-bonita-bpm-platform-installation/security-and-authentication/single-sign-on-with-cas" | relative_url}}):
```java
final LoginAPI loginAPI = TenantAPIAccessor.getLoginAPI();
final Map<String, Serializable> credentials = new HashMap<String, Serializable>();
credentials.put(AuthenticationConstants.CAS_TICKET, ticket);
APISession session = loginAPI.login(credentials);
ProcessAPI processAPI = TenantAPIAccessor.getProcessAPI(session);
```
