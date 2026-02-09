# 🚨 AWS SSH Brute Force Auto-Block System

## 📌 Project Summary

This project implements an automated cloud-native security response system that detects SSH brute-force attempts on a Bastion host and automatically blocks attacker IP addresses using AWS Network ACL rules.

The system is built using an event-driven serverless architecture powered by CloudWatch Logs and AWS Lambda.

---

## 🛡️ Key Features

- Detects failed SSH authentication attempts
- Extracts attacker IP addresses from logs
- Automatically creates NACL deny rules
- Blocks attackers at network layer
- Fully serverless detection pipeline
- Real-time automated response

---

## ☁️ AWS Services Used

- Amazon EC2 (Bastion + Private Web Server)
- VPC (Custom Networking)
- Network ACL (Dynamic IP Blocking)
- Application Load Balancer
- CloudWatch Logs
- CloudWatch Agent
- AWS Lambda
- IAM Roles & Policies

---

## 🏗️ Architecture Overview

# 🚨 AWS SSH Brute Force Auto-Block System

## 📌 Project Summary

This project implements an automated cloud-native security response system that detects SSH brute-force attempts on a Bastion host and automatically blocks attacker IP addresses using AWS Network ACL rules.

The system is built using an event-driven serverless architecture powered by CloudWatch Logs and AWS Lambda.

---

## 🛡️ Key Features

- Detects failed SSH authentication attempts
- Extracts attacker IP addresses from logs
- Automatically creates NACL deny rules
- Blocks attackers at network layer
- Fully serverless detection pipeline
- Real-time automated response

---

## ☁️ AWS Services Used

- Amazon EC2 (Bastion + Private Web Server)
- VPC (Custom Networking)
- Network ACL (Dynamic IP Blocking)
- Application Load Balancer
- CloudWatch Logs
- CloudWatch Agent
- AWS Lambda
- IAM Roles & Policies

---

## 🏗️ Architecture Overview

Internet Attacker
│
▼
Bastion Host (Amazon Linux 2023)
│
▼
rsyslog → /var/log/secure
│
▼
CloudWatch Agent
│
▼
CloudWatch Log Group (Bastion-SSH-Logs)
│
▼
CloudWatch Trigger
│
▼
AWS Lambda
│
▼
Network ACL Auto DENY Rule
│
▼
Attacker Blocked

---

## ⚙️ How It Works

1. Attacker attempts SSH login to Bastion host
2. Failed authentication logged in `/var/log/secure`
3. CloudWatch Agent ships logs to CloudWatch
4. CloudWatch triggers Lambda function
5. Lambda extracts attacker IP using regex
6. Lambda creates DENY rule in Network ACL
7. Attacker IP is blocked at network layer

---

## 🔐 Bastion Host Configuration

OS:
Amazon Linux 2023

Installed Components:
rsyslog
CloudWatch Agent

Log File Used:
/var/log/secure

---

## 🧠 Lambda Detection Logic

Detects multiple SSH failure patterns:

- Failed password
- Invalid user
- Disconnected from invalid user
- Authentication failure

Extracts IPv4 using regex and blocks using:
ec2.create_network_acl_entry()

---

## 🧪 Attack Simulation

Simulated by:

- Attempting SSH login without private key
- Using invalid usernames
- Repeating login attempts

Example log captured:
Invalid user admin from 1xx.xxx.xxx.xxx
Disconnected from invalid user admin 1xx.xxx.xxx.xxx

---

## 📊 Verification Steps

### CloudWatch Logs
Check log group:
Bastion-SSH-Logs

---

### Lambda Logs
Look for:
Lambda triggered
IP FOUND
Blocking IP

---

### Network ACL
New rule should appear:
DENY <Attacker IP>/32 → Port 22

---

## 📂 Repository Structure

/lambda
ssh_nacl_auto_block.py

/README.md

---

## ⚠️ Current Limitations

- Uses fixed NACL rule number
- No automatic unblock timer
- No failure threshold before blocking
- No attacker history storage

---

## 🚀 Future Improvements

- DynamoDB attacker tracking
- Auto unblock after timeout
- Failure threshold detection
- Security dashboard
- Slack / Email alerts
- Terraform Infrastructure as Code version

---

## 🎯 Learning Outcomes

- Event-driven cloud security automation
- AWS networking security controls
- CloudWatch log monitoring pipelines
- Serverless security response design
- Real-time threat detection architecture

---

## 👨‍💻 Author

AWS Cloud Security Hands-On Project

---

## ⭐ If You Like This Project

Consider starring ⭐ the repository.
