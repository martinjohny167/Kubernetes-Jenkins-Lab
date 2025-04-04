# Python Calculator with Jenkins Pipeline

This is a simple Python calculator application set up with Jenkins CI/CD integration.

## Overview

This repository contains:
- A simple Python calculator application
- Unit tests for the application
- A Jenkinsfile for CI/CD pipeline

## Jenkins Integration

This repository is configured to work with Jenkins using the Jenkinsfile in the root directory. The pipeline:

1. Builds the application and installs dependencies
2. Runs tests and generates coverage reports
3. Creates an executable using PyInstaller

## Webhook Configuration

The Jenkins webhook is configured to use the following URL:
```
https://ff2c-172-191-151-61.ngrok-free.app/github-webhook/
```

To configure the webhook in GitHub:
1. Go to your repository Settings
2. Click on Webhooks
3. Add webhook
4. Set the Payload URL to the ngrok URL above
5. Content type: application/json
6. Select "Just the push event"
7. Ensure "Active" is checked
8. Click "Add webhook"

## Setup Instructions

### Local Development

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run tests: `python -m pytest`

### Jenkins Job Configuration

1. In Jenkins, create a new Pipeline job
2. Configure it to use your GitHub repository
3. Set the branch specifier to `*/main`
4. Save and build the job 