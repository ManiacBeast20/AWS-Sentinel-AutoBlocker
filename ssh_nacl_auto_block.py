import boto3
import os
import re
import gzip
import base64
import json

# Create EC2 client
ec2 = boto3.client('ec2')

# NACL ID from Lambda Environment Variable
NACL_ID = os.environ['NACL_ID']

# Rule number used for blocking
RULE_NUMBER = 50


def extract_ip(message):
    """
    Extract IPv4 address from SSH log message
    """
    match = re.search(r'(\d+\.\d+\.\d+\.\d+)', message)
    if match:
        return match.group(1)
    return None


def block_ip(ip):
    """
    Create DENY rule in Network ACL
    """
    print(f"Attempting to block IP: {ip}")

    ec2.create_network_acl_entry(
        NetworkAclId=NACL_ID,
        RuleNumber=RULE_NUMBER,
        Protocol='6',  # TCP
        RuleAction='deny',
        Egress=False,
        CidrBlock=f"{ip}/32",
        PortRange={
            'From': 22,
            'To': 22
        }
    )

    print(f"Blocked IP successfully: {ip}")


def lambda_handler(event, context):

    print("Lambda triggered NEW VERSION")

    # Decode CloudWatch Logs payload
    compressed_payload = base64.b64decode(event['awslogs']['data'])
    uncompressed_payload = gzip.decompress(compressed_payload)
    payload = json.loads(uncompressed_payload)

    # Process each log entry
    for log_event in payload['logEvents']:
        message = log_event['message']
        print("LOG:", message)

        # Detect SSH attack patterns
        if (
            "Failed password" in message or
            "Invalid user" in message or
            "invalid user" in message or
            "Disconnected from invalid user" in message or
            "authentication failure" in message
        ):
            ip = extract_ip(message)

            if ip:
                print(f"IP FOUND: {ip}")
                block_ip(ip)
            else:
                print("IP NOT FOUND")

    return {
        "statusCode": 200,
        "body": "Logs processed"
    }
