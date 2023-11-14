## Postmortem: My First Outage — Django Car Auction Application Outage

Issue Summary

From 2:00 PM to 8:00 PM UTC, users attempting to access the Django Car Auction Application encountered login failures and were unable to sign in. This downtime affected 100% of user traffic to the application. The root cause of this outage was an unexpected surge in user traffic, causing the existing infrastructure to struggle with the increased load.

Timeline (all times UTC)

1:45 PM: Increased user activity observed.
2:00 PM: Application servers start experiencing degraded performance.
2:15 PM: Pagers alerted teams as login failures are detected.
2:30 PM: Attempt to scale resources to handle increased load.
3:30 PM: Downtime continues; investigation begins.
4:00 PM: Identified increased traffic as the root cause.
5:00 PM: Initiated load balancer adjustments to handle the surge.
7:00 PM: Load balancer modifications successfully implemented.
8:00 PM: 100% of traffic back online; outage resolved.
Root Cause

At 1:45 PM UTC, a significant influx of users accessing the Django Car Auction Application was observed, exceeding the anticipated load capacity(probably on account of a promo on vehicle inspections ad that was circulated a day before the issue presented). The existing infrastructure, configured to handle regular traffic, struggled to process the sudden increase. This led to a saturation of resources, causing login failures and degraded performance.

Resolution and Recovery

The team’s engineers were alerted at 2:15 PM UTC, initiating an investigation into the cause of the login failures. After identifying the root cause as an unexpected traffic surge, efforts were made to scale the application servers to accommodate the increased load.

At 5:00 PM UTC, load balancer adjustments were initiated to distribute traffic more efficiently among the servers. This measure successfully alleviated the strain on the infrastructure, gradually restoring user access.

Corrective and Preventative Measures

In response to this incident, the following actions are being taken to address the underlying causes and prevent recurrence:

Scaling Infrastructure: Assess and implement an infrastructure scaling strategy to handle sudden increases in user activity.
Automated Load Balancing: Implement automated load balancing mechanisms to dynamically adjust to varying traffic loads.
Real-time Monitoring: Enhance datadog monitoring system to provide real-time insights into application performance and potential issues, load related or otherwise.
Regular Traffic Assessments: Conduct regular assessments of expected user traffic and adjust infrastructure accordingly.
Communication Improvements: Develop better communication channels to notify users promptly during incidents and keep them informed of the status.
We are committed to improving the resilience and performance of the Django Car Auction Application to prevent future outages. We apologize for any inconvenience caused and appreciate your understanding and support.

Sincerely,

The C-hippo Team