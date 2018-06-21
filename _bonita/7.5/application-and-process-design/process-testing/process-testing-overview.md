---
layout : doc
title : "Process testing overview"
version : "7.5"
categories:
  - Application and Process Design
  - Process testing
order : 88
---
# Process testing overview

Bonita BPM Studio contains several features that you can use to verify your process while it is in development.

You can validate a process diagram: choose **_Validate_** from the **_Diagram_** menu, 
or go to the **Details** panel, **Validation status** tab and click **Refresh**. The **Details** panel contains a list
of warnings and errors indicating things to correct in the diagram. Click on a row in the list to highlight the relevant item in the diagram.

You can test some process components individually:

* Connectors: go to **_Test connector..._** in the **_Development_** menu.
* Expressions: use the **_Evaluate_** feature of the Expression editor.

You can run the process in debug mode, with the option to skip connector execution: click **_Debug_** in the Cool bar.

You can run the process locally, launching it from Bonita BPM Studio without first deploying it to Bonita BPM Portal. 
You must [create a test organization]({{"bonita/7.5/application-and-process-design/process-testing/configure-a-test-organization" | relative_url}})
and [configure a process]({{"bonita/7.5/application-and-process-design/process-configuration/configuring-a-process" | relative_url}}) before you can 
[run a process from Bonita BPM Studio]({{"bonita/7.5/application-and-process-design/process-testing/run-a-process-from-bonita-bpm-studio-for-testing" | relative_url}}).

In addition to functional testing during development, we recommend that you monitor the system load. This will help evaluate the performance, so you can make your process efficient.

When you have finished developing your process, we recommend that you perform a load test with the expected number of simultaneous users of the process, and a realistic rate of use of the process. 
This will help you evaluate the size of platform (CPU, RAM, etc.) that you will need when the process goes into production.