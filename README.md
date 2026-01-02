README.md

**Project: AWS Resume API (Manual Deployment)**

**Overview**: This project is a **serverless Resume API** built manually on AWS using **Lambda, API Gateway, and DynamoDB**. It demonstrates a foundational understanding of **AWS core services, serverless architecture, and manual deployment via AWS CLI / Console** before automating infrastructure with Terraform or CI/CD pipelines. 

**Fictitious Company:** NimbusHire Inc. – a recruiting tech company modernizing candidate profiles.

```mermaid
flowchart LR
    User[Client / Browser / curl]
    APIGW[Amazon API Gateway<br/>REST API]
    Lambda[AWS Lambda<br/>Python Function]
    DynamoDB[(Amazon DynamoDB<br/>resumes table)]
    CloudWatch[Amazon CloudWatch<br/>Logs]

    User -->|HTTP GET /resume/:id| APIGW
    APIGW -->|Invoke| Lambda
    Lambda -->|GetItem| DynamoDB
    Lambda --> CloudWatch
    Lambda -->|JSON Response| APIGW
    APIGW -->|HTTP 200| User






