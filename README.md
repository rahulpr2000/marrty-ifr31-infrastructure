# Marrty IFR31 — Infrastructure

AWS SAM/CloudFormation template for the **Marrty IFR31 Student Face Attendance System**.

**Holy Grace Polytechnic College, Mala** · Computer Engineering

## Architecture

Fully serverless, Zero Trust, end-to-end encrypted:

| Service | Purpose |
|---------|---------|
| **KMS** | Customer-managed key for all encryption |
| **S3** | Face images (SSE-KMS) |
| **DynamoDB** | Students, Faculty, Attendance, Devices (KMS encrypted) |
| **Rekognition** | Face collection for matching |
| **Cognito** | User auth (MFA, Advanced Security) |
| **API Gateway** | REST API with Cognito authorizer |
| **WAF** | Rate limiting, SQLi/XSS protection |
| **IoT Core** | MQTT with X.509 mutual TLS for devices |
| **Lambda** | 5 microservices (Python 3.12, ARM64) |

## Deploy

```bash
sam build
sam deploy --guided
```

## Environments

| Parameter | Default |
|-----------|---------|
| `Environment` | `dev` |
| `ProjectName` | `marrty-ifr31` |

## Related Repos

| Repo | Purpose |
|------|---------|
| [marrty-ifr31-web](https://github.com/rahulpr2000/marrty-ifr31-web) | Next.js Admin Portal |
| [marrty-ifr31-recognize](https://github.com/rahulpr2000/marrty-ifr31-recognize) | Face Recognition Lambda |
| [marrty-ifr31-enroll](https://github.com/rahulpr2000/marrty-ifr31-enroll) | Face Enrollment Lambda |
| [marrty-ifr31-attendance](https://github.com/rahulpr2000/marrty-ifr31-attendance) | Attendance API Lambda |
| [marrty-ifr31-student-api](https://github.com/rahulpr2000/marrty-ifr31-student-api) | Student CRUD Lambda |
| [marrty-ifr31-faculty-api](https://github.com/rahulpr2000/marrty-ifr31-faculty-api) | Faculty CRUD Lambda |
| [marrty-ifr31-firmware](https://github.com/rahulpr2000/marrty-ifr31-firmware) | ESP32S3 Firmware |
