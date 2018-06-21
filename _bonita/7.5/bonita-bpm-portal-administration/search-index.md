---
layout : doc
title : "Search keys"
version : "7.5"
categories:
  - Bonita BPM Portal Administration
order : 165
---
# Search keys

{% alert info %}
**Note:** For Performance and Efficiency editions only.
{% endalert %}

The search field in Bonita BPM Portal can be used to search for particular values in cases, filter them, and display the result.

Note: the search in Bonita BPM Portal is dependent on the search keys configured in Bonita BPM Studio. If nothing has been entered as a value for the task during the design of the process, then no results come up.

How to get results from the search in Bonita BPM Portal <!--{.h2}-->

Only cases which have been given values will be filtered.

Technical note: A search key is translated by a database index in Bonita BPM Engine. Currently, when designing in Bonita BPM Studio, you cannot create more than 5 keys/indexes per process.

In addition, search keys are now displayed in the case list and in the case more details view. In this way, you can use search keys for adding dynamic and business information to your cases.

See also [Define a search key]({{"bonita/7.5/application-and-process-design/data/define-a-search-index" | relative_url}}).
