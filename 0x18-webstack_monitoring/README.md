Task webstack_monitoring

This repository contains instructions and configuration files to set up monitoring using Datadog for your web servers.

Prerequisites
A free Datadog account. Sign up here using the US website (https://app.datadoghq.com) and select the US1 region.
Access to the server you want to monitor (referred to as web-01 in this guide).
Installation
Step 0: Sign up for Datadog and Install the Datadog Agent
Sign up for a free Datadog account on the Datadog website.
Follow the instructions to select statistics from your current stack that Datadog can monitor for you.
Once signed up, install the Datadog agent on web-01. Instructions for installation can be found on the Datadog website.
Step 1: Monitor Some Metrics
Set up a monitor that checks the number of read requests issued to the device per second.
Set up a monitor that checks the number of write requests issued to the device per second.
Step 2: Create a Dashboard
Create a new dashboard on the Datadog platform.
Add at least 4 widgets to your dashboard to monitor different metrics.
Obtain the dashboard ID using Datadog's API and create an answer file 2-setup_datadog containing the dashboard ID on the first line.
API Keys
Once you have signed up for Datadog and installed the Datadog agent, obtain your API key and application key. Copy-paste these keys into your Intranet user profile as follows:

DataDog API Key: [YOUR_API_KEY]
DataDog Application Key: [YOUR_APPLICATION_KEY]
Ensure that your server web-01 is visible in Datadog under the hostname XX-web-01. You can validate this using the provided API.

Repository Information
GitHub Repository: alx-system_engineering-devops
Directory: 0x18-webstack_monitoring
Notes
If needed, update the hostname of your server to ensure correct monitoring.
For further details on available metrics and configurations, refer to the Datadog documentation
