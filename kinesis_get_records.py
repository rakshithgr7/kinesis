import boto3
import json

kinesis = boto3.client('kinesis')

response = kinesis.describe_stream(
    StreamName='assignment',
    Limit=100
)
StreamName = response['StreamDescription']['StreamName']
StreamARN = response['StreamDescription']['StreamARN']
ShardId =response['StreamDescription']['Shards'][0]['ShardId']

response = kinesis.get_shard_iterator(
    StreamName=StreamName,
    ShardId=ShardId,
    ShardIteratorType='TRIM_HORIZON',
    StreamARN=StreamARN
)
Shard_Iterator=response['ShardIterator']




while Shard_Iterator is not None:
    records = kinesis.get_records(
    ShardIterator=Shard_Iterator,
    Limit=30,
    StreamARN=StreamARN,)
    Shard_Iterator=records['NextShardIterator']
    result = records["Records"]
    # print(result['Data'])
    for record in result:
            print(record["Data"])

