import os
import json
import boto3
import pandas as pd

from typing import Dict
from dotenv import load_dotenv
from moto import mock_sqs
from snowflake import connector

load_dotenv()

class Snowflake(object):
    """Snowflake Interaction Class

    This class helps to interact with Snowflake. Providing methods to
    connect to Snowflake, and query Snowflake results into a Pandas
    DataFrame.
    """

    def __init__(self):
        """Construct

        Connect to Snowflake using the parameters SNOWFLAKE_USER,
        SNOWFLAKE_ACCOUNT, and SNOWFLAKE_PASSWORD from the .env file.
        """

        self.ctx = connector.connect(
            user=os.environ['SNOWFLAKE_USER'],
            account=os.environ['SNOWFLAKE_ACCOUNT'],
            password=os.environ['SNOWFLAKE_PASSWORD']
        )

        self.cur = self.ctx.cursor()

    def exec_query(self, sql: str) -> pd.DataFrame:
        """Execute Snowflake Synchronous Query

        Pass the specified SQL query to Snowflake to execute,
        return the results in a Pandas DataFrame.
        """

        self.cur.execute(sql)
        return self.cur.fetch_pandas_all()

@mock_sqs
def send_sqs_message(message: str, queue_name:str = 'sqs-messages'):
    """Send SQS Message

    Mock sending an SQS message to an SQS Queue. Instead of sending to
    an SQS queue, this method appends the message to a file with the
    same name as the SQS queue.
    """

    sqs_resource = boto3.resource('sqs')
    queue = sqs_resource.create_queue(QueueName=queue_name)
    sqs_client = boto3.client('sqs')
    sqs_client.send_message(QueueUrl=queue.url, MessageBody=(message))

    sqs_messages = queue.receive_messages()

    with open(f"{queue_name}.txt", 'a') as file:
        for message in sqs_messages:
            file.write(message.body + '\r\n')

if __name__ == '__main__':
    snow = Snowflake()

    send_sqs_message('{"addressee": "john.smith@sainsburys.co.uk", "message": "test1"}')
    send_sqs_message('{"addressee": "jane.doe@sainsburys.co.uk", "message": "test2"}')
    send_sqs_message('{"addressee": "jane.smith@sainsburys.co.uk", "message": "test3"}')

