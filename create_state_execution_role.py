from __future__ import division, print_function, unicode_literals
from datetime import datetime
import logging
import json
import sys
import boto3
import botocore
import time

cf = boto3.client('cloudformation')

log = logging.getLogger('deploy.cf.create_or_update')

response = cf.create_stack(
  StackName = 'executionlambdarole',
  TemplateURL = 'https://anillohar.s3.ap-south-1.amazonaws.com/states_execution_role_lambda.yaml',
  Capabilities=[
        'CAPABILITY_IAM','CAPABILITY_NAMED_IAM','CAPABILITY_AUTO_EXPAND',
    ],
        )
print(response)
time.sleep(10)