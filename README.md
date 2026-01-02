flowchart LR
    User[Client / Browser / curl]
    APIGW[Amazon API Gateway<br/>REST API]
    Lambda[AWS Lambda<br/>Python Function]
    DynamoDB[(Amazon DynamoDB<br/>resumes table)]
    CloudWatch[Amazon CloudWatch<br/>Logs]

    User -->|HTTP GET /resume/id| APIGW
    APIGW -->|Invoke| Lambda
    Lambda -->|GetItem| DynamoDB
    Lambda --> CloudWatch
    Lambda -->|JSON Response| APIGW
    APIGW -->|HTTP 200| User

