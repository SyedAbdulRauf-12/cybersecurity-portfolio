# Implementing Basic Network Access Control using pfSense

This is a lab activity that we will be doing with our existing setup. As you remember we have setup our Kali, Fedora
and Metasploitable VMs on our hypervisor Virtual Box.  
<br>
Before continuing with our lab activity, let us understand,

## What is Network Access Control (NAC)?
Network Access Control is a security mechanism that controls which devices and users can access an internal network i.e.
an organizations network. It is like the guard at the front gate of an organization that checks and monitors who is going to enter, 
where they can go and how much of an authorization they have.  
If the device or user pass the initial checks, they are granted access to the internal network i.e. the organizations network.

## Why NAC?
The company wants to ensure that:
- Only authorized employees can access the internal network.
- Guest users can access the internet but not internal servers.
- Unknown devices are blocked.
- Infected or non-compliant devices are restricted.

NAC helps enforce these requirements. Without the NAC enforcing the requirements or rules:
- Anyone can connect to an open port and gain access.
- Employees may connect their personal laptops.
- Unauthorized devices will be able to access sensitive information or internal resources.
- Infected devices may spread their malware to other devices.
- Guest devices could access confidential accounts or information.



