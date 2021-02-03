# ptt-title-crawler
This project will crawl ptt gossiping board and analyze post title by google-cloud-language library. Finally output popular post chart and popular word chart.

## Getting Started
### Prerequisites
- Python 3.9
- Pipenv

### In order to use google-cloud-language library, need to go through the following steps:
1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)
2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)
3. [Enable the Google Cloud Language API.](https://cloud.google.com/natural-language)
4. [Setup Authentication.](https://googleapis.dev/python/google-api-core/latest/auth.html)

## Usage
```
pipenv sync
pipenv run python -m src
```

## Authors
Rex Wu <rexwu.1123@gmail.com>
