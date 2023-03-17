import boto3
import json

kinesis = boto3.client('kinesis')

response = kinesis.describe_stream(
    StreamName='assignment',
    Limit=100
)

StreamName = response['StreamDescription']['StreamName']
StreamARN = response['StreamDescription']['StreamARN']
print( StreamName , StreamARN )

data1 = {"personId": "uyfuf"}

records = kinesis.put_records(
    Records=[
        {
            'Data': json.dumps(data1),
           
            'PartitionKey': "78"
        },
    ],
    StreamName=StreamName,
    StreamARN=StreamARN
)

print(records)