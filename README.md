# QR Code Generator — AWS Lambda + S3

A serverless QR code generator that turns any text or link into a scannable QR code — generated and stored entirely in the cloud, with no signup required for end users.

## Live Demo
https://d2uko7csallknv.cloudfront.net/qrgen.html

## Tech Stack
- AWS Lambda
- Amazon S3
- API Gateway
- Python
- CloudFront

## How It Works
1. User enters any text or link
2. API Gateway receives the POST request
3. Lambda generates the QR code
4. Image is stored in S3
5. Public URL is returned instantly

## Author
Ahmad Waheed — https://www.linkedin.com/in/ahmadwaheed2002/
