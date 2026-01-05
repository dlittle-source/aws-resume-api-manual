README.md

**Project: AWS Resume API (Manual Deployment)**

**Overview**: This project is a **serverless Resume API** built manually on AWS using **Lambda, API Gateway, and DynamoDB**. It demonstrates a foundational understanding of **AWS core services, serverless architecture, and manual deployment via AWS CLI / Console** before automating infrastructure with Terraform or CI/CD pipelines. 

**Fictitious Company:** NimbusHire Inc. – a recruiting tech company modernizing candidate profiles.

1. **AWS Lambda:**
   - A serverless compute service that runs your code without provisioning or managing servers.   

2. **API Gateway:**
   - A fully managed service to create, deploy, and manage APIs that act as the “front door” for applications to access backend services.

3. **DynamoDB:**
   - A fully managed NoSQL database that provides fast and predictable performance at any scale.

4. **Programmatic access:**
   - The ability to interact with AWS services using code or scripts instead of the AWS Management Console.
  
5. **AWS CloudWatch:**
   - CloudWatch was activated to provide observability and enhance visibility for both Lambda and API Gateway.
   

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






