import boto3

kinesis = boto3.client('kinesis')

response = kinesis.create_stream(
    StreamName='assignment',
    ShardCount=1,
    StreamModeDetails={
        'StreamMode': 'PROVISIONED'
    }
)
print(response)

response = kinesis.describe_stream(
    StreamName='assignment2',
    Limit=100
)
print(response)
StreamName = response['StreamDescription']['StreamName']
StreamARN = response['StreamDescription']['StreamARN']
ShardId =response['StreamDescription']['Shards'][0]['ShardId']
print( ShardId )


