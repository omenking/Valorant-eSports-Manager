# Valorant-eSports-Manager
This is my public working repo for building my Valorant eSports Manager for the Depost 2024 Fall hackathon.

https://vcthackathon.devpost.com/

## Considerations

I am dyslexic, so please be kind if there are spelling or gramamtical errors.

## Journaling

This is technical documentation and journaling so you can understand my thought process when working building my eSports Manager.

- [Technical Uncertainty](./journal/technical-uncertainty.md)
- [eSports Manager Tasks](./journal/esports-manager-tasks.md)
- [Model Cost Analysis](./journal/model-cost-anaylsis.md)
- [Infrastructure](./journal/model-cost-anaylsis.md)

# Configuration

Set the following AWS Env Vars:

```sh
export AWS_ACCESS_KEY_ID="xxx"
export AWS_SECRET_ACCESS_KEY="xxx"
export AWS_DEFAULT_REGION="us-east-1"
```

```sh
./bin/aws_install_cli.sh
aws sts get-caller-identity
```

> you don't have to install the AWS CLI, but its useful for test your API credentials.


## Setup

```sh
pip install -r requirements.txt
```

### Running

```sh
pyhton chat.py
```