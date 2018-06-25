---
layout : doc
title : "Forms"
version : "7.6"
categories:
  - Bonita Portal Administration
  - Resources
order : 145
---
# Forms

This page explains how to add a form resource to the Bonita Portal and make it available to users. Form resources are intended for use in applications.

Pages are [exported. imported, modified, and deleted]({{"bonita/7.6/bonita-portal-administration/resources/resource-management" | relative_url}}) as resources in the Portal. 

Form definition <!--{.h2}-->

A form is a [page]({{"bonita/7.6/bonita-portal-administration/resources/pages" | relative_url}}) that belongs to a process. It could be a process instantiation form, a human task form, or an overview form. There are some extra things to consider when you are creating a form compared with an ordinary page, concerning how data is passed between the process instance and the form.

A [context]({{"bonita/7.6/application-and-process-design/data/contracts-and-contexts" | relative_url}}) is the set of data provided by the process instance or task instance to the form. 
There is no context for a process instantiation form.

A [contract]({{"bonita/7.6/application-and-process-design/data/contracts-and-contexts" | relative_url}}) is the definition of that data that the form returns to the process instance. There is no contract for an overview form.

Three auto-generated forms are provided by default, for process instantiation, for human task execution, and for the case overview. 

The process instantiation and step execution auto-generated forms are based on the relevant contract and they are a useful tool for testing and debugging your application. 

The overview consists of three main sections:

* List of business data: it shows the content of the business variables used by the case.
* List of documents: it shows the content of each document used by the case.
* Timeline: it shows in chronological order information about all the actions that have been performed in the selected case.

To learn how to manage the link between process and forms, go to the [live update]({{"bonita/7.6/bonita-portal-administration/live-update" | relative_url}}) page.

### Application Theme access

If your forms is viewed in an application, you will have access facilities for [the application theme]({{"bonita/7.6/bonita-portal-administration/applications" | relative_url}}).

The `Theme.css` is directly accessible by adding the following link in `index.html`: `<link href="../theme/theme.css" rel="stylesheet" />`
This link is already inserted in the forms you design with the UI Designer.

{% alert info %}
The `app` URL parameter is used to retrieve the current application related Theme.      
The living application layout inject this `app` URL parameter in the targeted page/form URL, and the value is the application token.                
If you create your own navigation link, you will need to include this `app` URL parameter in the forged form URL, in order to be able to benefit from the application theme. 
{% endalert %}

{% alert info %}
In the portal, the link `../theme/theme.css` will point the file `theme.css` from the portal theme. This portal forms theme is empty, and customizable to fit to the current portal theme. 
{% endalert %}
