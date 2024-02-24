import paramiko

# Set up the SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote server
ssh_client.connect('remote_server_address', username='your_username', key_filename='/path/to/your/private/key')

# Execute a command (e.g., 'ls' to list directory contents)
stdin, stdout, stderr = ssh_client.exec_command('ls')

# Read and print the command output
print(stdout.read().decode())

# Close the connection
ssh_client.close()
