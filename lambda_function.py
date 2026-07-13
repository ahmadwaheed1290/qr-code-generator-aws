import json
import boto3
import urllib.request
import urllib.parse
import uuid

s3 = boto3.client('s3', region_name='ap-southeast-1')
BUCKET_NAME = 'ahmadwaheed-portfolio'

def lambda_handler(event, context):
    
    if event.get('requestContext', {}).get('http', {}).get('method') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            },
            'body': ''
        }
    
    body = json.loads(event['body'])
    text = body.get('text', '')
    
    encoded_text = urllib.parse.quote(text)
    qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={encoded_text}"
    
    response = urllib.request.urlopen(qr_api_url)
    image_data = response.read()
    
    file_name = f"qrcodes/{uuid.uuid4()}.png"
    
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=image_data,
        ContentType='image/png'
    )
    
    qr_url = f"https://{BUCKET_NAME}.s3.ap-southeast-1.amazonaws.com/{file_name}"
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS'
        },
        'body': json.dumps({'qr_url': qr_url})
    }
