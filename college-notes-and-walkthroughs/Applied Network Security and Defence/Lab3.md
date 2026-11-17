# Lab 3: IDS and IPS
In this lab we will be using Suricata, snort or Wireshark to create detection rules, alert evidence and an investigation report.
The objective is to create a detextion rule, generate an alert, analyze network traffic and prepare a report.

## What is an IDS?
The Intrusion detection system is a security solution that monitors network trafffic or system activities to identify suspicious behaviours.  
When it detects any suspicious activities, it sends an alert to the security team to investigate. It doesnt block the network traffic.  
E.g. Attacker attempts to scan multiple ports on a company's web server. The IDS detects this activity and generates an alert containing the IP source address and the targetted ports.  
Two types of IDS: Network based and Host based.
- Network Based: Its placed on the network and monitors all the traffic that passes through a network. Can check the traffic between
- two systems, monitor port scans and is commonly deployed near dmz's or core network segments.
- Host based: Monitors activites on the host system rather than network. Monitors file changes, unauthorized changes, visibility into activites that cant be seen by network based.

The work flow is as follows:
- Captures network packets or monitors system events.
- Analyzes the collected data for suspicious patterns.
- Identifies potential attacks.
- Generates alerts for security analysts.

## What is an IPS?
The Intrusion Prevention System is another security solution that monitors network traffic the same way an IDS does, but it can take action automatically
to prevent malicious traffic from reaching its destination. Unlike the IDS, which listens to the traffic passively and generates alerts, IPS 
actively blocks malicious traffic.  
The work flow is as follows:
- Inspection of incoming and outgoing packets
- Comparing traffic against detection rules and security policies.
- Identifying the suspicious or malicious activity.
- Blocking all the malicious packets, dropping the connections or taking another configured action.
  
E.g. Attacker sends traffic matching a known exploit signature to company's web server, IPS detects it and drops the malicious
packets before they reach the server.

## How are they different than firewalls?
All the three technologies help to protect the networks they are placed in. They differ in their primary responsibilities.  

| Feature | IDS | IPS | Firewall |
|---|---|---|---|
| Primary purpose | Detect suspicious activity | Detect and Prevent attacks | Control network access |
| Main Operation | Monitor and alert | Inspect and block | Allow or block traffic |
| Deployment | Passive | Inline | Inline or integerated |
| Decision Basis | Detection rules, signatures and anomalies | Same as IDS with addition of Prevention policies | ACL rules, IPs, ports, protocols and app policies |
| Auto Blocks | No | Yes, hen configured | yes, according to policy |
| E.g. | Alerts on port scan | Block malicious traffic | denying entry to traffic to an unauthorized port |

## Lab Activity
1. Let us set up our lab. Lets start our VM's whichever are available (preferably Linux based.) We will use Fedora and Kali.

<img width="400" height="82" alt="image" src="https://github.com/user-attachments/assets/d24b3edd-8bca-4a7a-9020-fe1f6cf66e7e" />

2. We have to make sure both of these VM's are connected to the same Internal Network.

   The Fedora settings:
<img width="583" height="388" alt="image" src="https://github.com/user-attachments/assets/665d1b06-9dfb-4d7a-bf92-ca0b8e4fee07" />

The Kali Linux settings:  

<img width="579" height="387" alt="image" src="https://github.com/user-attachments/assets/4ae93bec-819c-42a6-aeb6-339c886a7e35" />

<img width="940" height="120" alt="image" src="https://github.com/user-attachments/assets/febaf67e-3f40-4455-8864-ac9626a367e7" />
<img width="940" height="146" alt="image" src="https://github.com/user-attachments/assets/27a71d9d-bf10-49a1-95e7-3abadb97815a" />
<img width="602" height="229" alt="image" src="https://github.com/user-attachments/assets/202424b8-a6f5-4de2-98f3-651403323e48" />
<img width="617" height="302" alt="image" src="https://github.com/user-attachments/assets/e2f3427e-365c-435f-a6ea-00e884ff885f" />




