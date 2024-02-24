import boto3
from botocore.exceptions import ClientError

# Initialize a boto3 client
iam_client = boto3.client('iam')

def rotate_iam_keys(user_name):
    # Get the current access keys for the user
    try:
        keys = iam_client.list_access_keys(UserName=user_name)['AccessKeyMetadata']
    except ClientError as e:
        print(f"Error fetching access keys for user {user_name}: {e}")
        return

    # Rotate each key
    for key in keys:
        access_key_id = key['AccessKeyId']
        # Deactivate the current key
        try:
            iam_client.update_access_key(UserName=user_name, AccessKeyId=access_key_id, Status='Inactive')
            print(f"Deactivated key: {access_key_id} for user {user_name}")
        except ClientError as e:
            print(f"Error deactivating key {access_key_id}: {e}")
            continue

        # Create a new key
        try:
            new_key = iam_client.create_access_key(UserName=user_name)
            print(f"Created new access key for user {user_name}")
            print(f"Access Key ID: {new_key['AccessKey']['AccessKeyId']}")
            # Ideally, securely store the new key and secret here
        except ClientError as e:
            print(f"Error creating new access key for user {user_name}: {e}")
            continue

        # Delete the old key
        try:
            iam_client.delete_access_key(UserName=user_name, AccessKeyId=access_key_id)
            print(f"Deleted old key: {access_key_id}")
        except ClientError as e:
            print(f"Error deleting key {access_key_id}: {e}")

def main():
    user_name = 'your-iam-user-name'
    rotate_iam_keys(user_name)

if __name__ == "__main__":
    main()
