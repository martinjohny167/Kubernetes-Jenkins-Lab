<<<<<<< HEAD
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
=======
# cdevops-gitea
k8s gitea lab to take dev (sqlite based) to prod (mysql based)

TLDR;

```bash
cd dev && ansible-playbook up.yaml
```

If that fails you may need some pre-requisites

1. Make sure that docker is running by doing `docker ps` until it shows 

```
CONTAINER ID   IMAGE                            COMMAND                  CREATED         STATUS         PORTS                             NAMES

```

2. run `ansible-playbook --version` to see if you have ansible. If not run:

```bash
bash <(curl -Ls https://raw.githubusercontent.com/conestogac-acsit/cdevops-bootstrap/refs/heads/main/bootstrap.sh)
```

3. run `kubectl get ns default` to see if you have a cluster. The expected result is:

```
NAME      STATUS   AGE
default   Active   29m
```

If you have another result try installing a k8s cluster:

```bash
bash <(curl -Ls https://raw.githubusercontent.com//conestogac-acsit/cdevops-bootstrap/refs/heads/main/k8s.sh)
```

Once you have made it through the `up.yaml` playbook you can forward the port:

```bash
kubectl port-forward svc/gitea-http 3000:3000
```

Now you should be able to access gitea in development mode.

The challenge is to run this in production mode from a prod folder at the same level as the dev folder with it's own up, down and values.yaml.

### Points to Cover

## Marking

|Item|Out Of|
|--|--:|
|use [the gitea helm](https://gitea.com/gitea/helm-gitea) to make the repository data persistent|2|
|change the root password for the provided mysql service|2|
|make gitea use the provided mysql service|2|
|Use [this article](https://blog.techiescamp.com/using-ngrok-with-kubernetes/) to expose your gitea instance publically|2|
|create a public clone of your finished work, based on this template on your gitea|1|
|make sure that your instance is running for marking and submit a link to the repository from the previous step|1|
|||
|total|10|
>>>>>>> 526649ca58967d96c952914c5310378adad0ad4b
