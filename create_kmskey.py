from __future__ import division, print_function, unicode_literals
from datetime import datetime
import logging
import json
import sys
import boto3
import botocore

cf = boto3.client('cloudformation')

log = logging.getLogger('deploy.cf.create_or_update')

print('Creating KMS Key for you')

response = cf.create_stack(
  StackName = 'awscloudformation1',
  TemplateURL = 'https://anillohar.s3.ap-south-1.amazonaws.com/kmskey.yaml',
  Capabilities=[
        'CAPABILITY_IAM','CAPABILITY_NAMED_IAM','CAPABILITY_AUTO_EXPAND',
    ],
        )

print(response)
