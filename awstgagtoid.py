"""
@author: avale
"""

import boto3

ec2 = boto3.resource('ec2', region_name='eu-west-1',
           aws_access_key_id='XXXXXXXXXXXXXXXXX',
            aws_secret_access_key='XXXXXXXXXXXXXXXXXX')
       
machine_names = []

for instance in ec2.instances.all():
    name = ''
    tags = {}
    for tag in instance.tags:
        if tag['Key'] == 'KEY_A_BUSCAR':
            name = tag['Value']
    if name == 'VALOR_A_BUSCAR':
         machine_names.append(instance.instance_id)
        
print(*machine_names)
