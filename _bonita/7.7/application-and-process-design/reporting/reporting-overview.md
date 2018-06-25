---
layout : doc
title : "Reporting overview"
version : "7.7"
categories:
  - Application and Process Design
  - Reporting
order : 77
---
# Reporting overview

{% alert info %}
**Note:** For Enterprise, Performance, Efficiency, and Teamwork editions only.
{% endalert %}

This page presents an overview of reporting with Bonita.

## Terminology

Reporting is the act of collecting and aggregating Key Performance Indicators (KPIs) to present them in reports.  
KPIs are defined as a set of measures that are used to assess the operational success of a business process.

Reporting is also know as Business Intelligence (BI) or Business Activity Monitoring (BAM).

## Reporting dependencies

Reporting involves Bonita and two other third-party software components:

* A reporting database of your choice.
* A BI tool of your choice.

## Reporting main steps

Reporting is composed in several ordered steps.

At design time:

1. [Reporting database setup]({{"bonita/7.7/application-and-process-design/reporting/set-up-a-reporting-database" | relative_url}})
2. [KPI definition in Bonita Studio]({{"bonita/7.7/application-and-process-design/reporting/set-up-kpis" | relative_url}})
3. [Report creation in the BI tool]({{"bonita/7.7/application-and-process-design/reporting/create-a-report" | relative_url}})

At execution time:

1. KPI collection in Bonita Engine and storage in the reporting database (this is performed automatically based on KPI definitions)
2. Report generation using the BI tool or Bonita Portal
