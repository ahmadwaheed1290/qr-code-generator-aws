# Architecture

## Request Flow

```
User enters text or link
       |
       v
CloudFront CDN (HTTPS)
       |
       v
API Gateway — POST /generate
       |
       v
AWS Lambda (Python 3.12)
       |
       v
QR Code Generation
       |
       v
Amazon S3 — stores PNG image
       |
       v
Public URL returned to frontend
```

## AWS Services Used

| Service | Purpose |
|---------|---------|
| AWS Lambda | Serverless function to process requests |
| Amazon S3 | Storage for generated QR code images |
| API Gateway | REST API endpoint |
| CloudFront | Global CDN delivery |
| IAM | Permissions management |

## Cost

Near-zero monthly cost — Lambda runs only on demand.
S3 storage costs a few cents per thousand QR codes generated.
