---
layout : doc
title : "Log in with CAS"
version : "7.7"
categories:
  - Development
  - Engine API
order : 194
---
# Log in with CAS

{% alert info %}
**Note:** For Enterprise, Performance and Efficiency editions only.
{% endalert %}

Depending on your underlying authentication service, you may need to provide other information with the API in order to log in. A login method with a map enables you to provide the set of credentials that the authentication service requires. 
The following example can be used if you are [using Bonita with CAS]({{"bonita/7.7/installation/advanced-bonita-platform-installation/security-and-authentication/single-sign-on-with-cas" | relative_url}}):
```java
final LoginAPI loginAPI = TenantAPIAccessor.getLoginAPI();
final Map<String, Serializable> credentials = new HashMap<String, Serializable>();
credentials.put(AuthenticationConstants.CAS_TICKET, ticket);
APISession session = loginAPI.login(credentials);
ProcessAPI processAPI = TenantAPIAccessor.getProcessAPI(session);
```
