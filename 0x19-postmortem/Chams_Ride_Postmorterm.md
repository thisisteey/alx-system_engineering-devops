# Chams Ride Service Distruption Incident Report
April 8, 2024

![ChamsRide Postmortem](chams_ride_postmorterm_meme.jpeg)

In the wake of the Chams Ride service distruption on April 5, 2024, we present this incident report to shed light on the events leading to the interruption of our patform's functionality. We acknowledge the impact this incident has had on our users and extend our sincere apologies for any inconvenience caused during this time.

## Issue Summary

On Friday, April 5 2024, there was an outage due to a service distruption that lasted from 2:50 PM to 4:30 PM GMT+1. This outage impacted users with intermittent errors and delays in accessing car browsing and searching functionalities, affecting approximately 75% of users due to a misconfiguration in the backend authentication server.

## Timeline (all times GMT+1)

- **2:50 PM: Issue Detected** - The issue was detected by automated monitoring systems, which flagged an unusually high number of failed authentication requests.
- **3:00 PM: Incident Investigation Initiated** - Upon detection, the incident was promptly escalated to the development team for investigation. Initial assumption pointed towards a potential database connectivity issue.
- **3:15 PM: Misleading Investigation Paths** - During the investigation, the team initially focused on database connectivity as the potential root cause. However, further analysis revealed that the issue originated from a misconfiguration in the authentication server.
- **3:45 PM: Incident Escalated to Senior Developers** - Due to the complexity of the issue, the incident was escalated to senior developers for additional troubleshooting and resolution.
- **4:15 PM: Issue Resolved** - After identifying the misconfiguration in the authentication server, corrective measures were implemented, and the server configuration was reverted to its previous state.
- **4:30 PM: 100% of Traffic Restored** - After the server configuration was reverted to its previous state, 100% of users regained access to all the functionalities of the website.

## Root Cause and Resolution

- **Root Cause**: The roort cause of the outage was traced back to an inadvertent misconfiguration in the backend authentication server, which caused it to reject valid user authentication requests.
- **Resolution**: The issue was reslved by identifying and correcting the misconfiguration in the authentication server. The server configuration was reverted to its previous state, restoring normal service functionality.

## Corrective and Preventive Measures:

To prevent similar incidents in the future, the following measures will be implemented:
+ Implement stricter change control processes to prevent inadvertent misconfigurations.
+ Enhance monitoring capabilities to detect and alert on similar issues promptly.
+ Conduct thorough reviews of system configurations before deployment to production.

We at Chams Ride are dedicated to enhancing our systems and processes to minimize future disruptions. Your understanding and support are invaluable to us as we strive to provide a seamless experience. We extend our gratitude for your patience and apologize for any inconvenience caused.

Best regards,

The Chams Ride Team
