import boto3
from botocore.exceptions import ClientError

def manage_ec2_instance(instance_id, action):
    ec2 = boto3.client('ec2')
    try:
        if action == 'start':
            response = ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
            print(f'Starting instance {instance_id}...')
        elif action == 'stop':
            response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
            print(f'Stopping instance {instance_id}...')
    except ClientError as e:
        if 'DryRunOperation' in str(e):
            try:
                if action == 'start':
                    response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
                    print(f'Instance {instance_id} started successfully.')
                elif action == 'stop':
                    response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
                    print(f'Instance {instance_id} stopped successfully.')
            except ClientError as e:
                print(f"Failed to {action} instance {instance_id}: {e}")
        else:
            print(f"Error: {e}")

# Example usage:
# manage_ec2_instance('your-instance-id', 'start')  # To start an EC2 instance
# manage_ec2_instance('your-instance-id', 'stop')   # To stop an EC2 instance
