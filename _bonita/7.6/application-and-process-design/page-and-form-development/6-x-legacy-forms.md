---
layout : doc
title : "6.x legacy forms"
version : "7.6"
categories:
  - Application and Process Design
  - Page and form development
order : 55
---
# 6.x legacy forms

{% alert warning %}
**Attention**: By the end of 2018, V6 GWT forms won't be available for modeling or execution.
We strongly advise you to switch to forms created with Bonita UI Designer to benefit from technologies like html/AngularJS and use contracts in tasks and process instantiation.
{% endalert %}

## Continue to use 6.x forms in Bonita 7.x

From the **Execution** tab, in the **Form**, **Instantiation form**, and **Overview page** panes, you can choose the **_6.x_** option.   
This enables you to continue to use the 6.x forms in a Bonita 7.x platform. You need to apply this configuration at each form, and each overview page. This means that a process can work with a mix of 6.x and 7.x forms/overview pages to make it easier to [migrate forms from 6.x]({{"bonita/7.6/application-and-process-design/page-and-form-development/ui-designer/migrate-a-form-from-6-x" | relative_url}}).

## Hide/Show 6.x specific features

When you no longer need access to the 6.x features, you can hide them to simplify the Bonita Studio UI.

1. Go to **Preferences**.
2. In the **Other** category, click **6.x legacy**.
3. Uncheck the checkbox to hide some 6.x-only features.
