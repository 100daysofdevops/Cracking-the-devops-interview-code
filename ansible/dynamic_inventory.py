#!/usr/bin/env python
import json
import boto3

def fetch_ec2_instances():
    # Use boto3 to query AWS EC2 instances
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    inventory = {}
    for instance in instances:
        group_name = 'dynamic_group' 
        if group_name not in inventory:
            inventory[group_name] = {"hosts": []}
        inventory[group_name]["hosts"].append(instance.public_dns_name)
    return inventory

if __name__ == '__main__':
    print(json.dumps(fetch_ec2_instances()))
