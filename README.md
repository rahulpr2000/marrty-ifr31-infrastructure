# Marrty IFR31 - Infrastructure

AWS SAM Template defining the serverless architecture for the Student Face Attendance System.

## Stack Resources
- **API Gateway:** Entry point for all REST APIs.
- **Cognito:** User authentication and authorization.
- **DynamoDB:** `Students`, `Faculty`, `Attendance`, `Devices` tables.
- **S3:** `face-images` storage and `web` hosting.
- **Lambda:** 5 microservices.
- **IoT Core:** MQTT broker for ESP32.
- **CloudFront:** CDN for frontend hosting.

## Deployment
```bash
sam deploy --guided
```
