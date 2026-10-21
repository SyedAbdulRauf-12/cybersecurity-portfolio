# pfSense Lab Setup: Configuring the Network and Interface

This is a guide/ walkthrough for configuring pfSense network interfaces, static IP addressing, and DHCP services inside Oracle VM VirtualBox for an isolated cybersecurity testing topology.

## Network Topology Overview

Before configuring interfaces inside the firewall, we should verify the logical network design:

```
[ Kali Linux ]  (WAN Segment)
      │
      │ Internal Network: WAN_NET
      ▼
┌──────────────┐
│   pfSense    │ ── WAN Interface (em0): 192.168.10.1/24 (DHCP Scope: .100 - .200)
│   Firewall   │ ── LAN Interface (em1): 192.168.20.1/24 (DHCP Scope: .100 - .200)
└──────────────┘
      ▲
      │ Internal Network: LAN_NET
      │
[ Fedora Workstation ] (LAN Segment)
```

## VirtualBox Network Adapter Pre-Check

If pfSense does not detect or display interfaces, verify VirtualBox adapter bindings before starting the VM.

### pfSense VM Settings
1. Power down the pfsense VM (`Machine` > `Close` > `Power off the machine`).
2. Navigate to **Settings** --> **Network**.
3. **Adapter 1 (Mapped to WAN / em0):**
   * **Enable Network Adapter:** Checked
   * **Attached to:** `Internal Network`
   * **Name:** `WAN_NET`
   * **Advanced > Promiscuous Mode:** `Allow All`
   * **Cable Connected:** Checked
<img width="584" height="386" alt="image" src="https://github.com/user-attachments/assets/19749356-65b9-47aa-9951-2862bb5f49da" />  

4. **Adapter 2 (Mapped to LAN / em1):**
   * **Enable Network Adapter:** Checked
   * **Attached to:** `Internal Network`
   * **Name:** `LAN_NET`
   * **Advanced > Promiscuous Mode:** `Allow All`
   * **Cable Connected:** Checked
   
<img width="586" height="389" alt="image" src="https://github.com/user-attachments/assets/9aec7fa7-53f5-4c2c-bcc0-4e38af46e626" />

5. Click **OK**.

### Client VM Settings
These VMs can be of any flavor but since I already have Kali and Fedora installed on my system, I didn't bother with downloading any other.
* **Kali Linux VM:** **Adapter 1** set to `Internal Network`, Name: `WAN_NET`, Promiscuous: `Allow All`.
<img width="587" height="431" alt="image" src="https://github.com/user-attachments/assets/a54bd075-8dd7-4e88-90e6-4a6dfccd3e66" />

* **Fedora VM:** **Adapter 1** set to `Internal Network`, Name: `LAN_NET`, Promiscuous: `Allow All`.
<img width="589" height="413" alt="image" src="https://github.com/user-attachments/assets/d326f6e0-5491-4a3a-8a0c-ef6b7f62ceed" />



## Assigning Physical Interfaces
Boot up pfSense now. When pfSense boots to the 16-option console menu without interfaces assigned (the LAN and WAN) (or interfaces are unassigned/unmapped), start here.

```text
*** Welcome to pfSense ***

 0) Logout (SSH only)                  9) pfTop
 1) Assign Interfaces                 10) Filter Logs
 2) Set interface(s) IP address       11) Restart webConfigurator
 3) Reset webConfigurator password    12) PHP shell
 4) Reset to factory defaults         13) Retrieve DHCP Lease
 5) Reboot system                     14) Enable Secure Shell (sshd)
 6) Halt system                       15) Restore recent configuration
 7) Ping host                         16) Restart PHP-FPM
 8) Shell
```

1. Enter `1` and press `Enter`.
2. **VLAN Setup:**
   ```text
   Should VLANs be set up now [y|n]? n
   ```
   * Type `n` and press `Enter`.
3. **WAN Interface Assignment:**
   ```text
   Enter the WAN interface name or 'a' for auto-detection: em0
   ```
   * Type `em0` (or `vtnet0` depending on VirtualBox NIC type) and press `Enter`.
4. **LAN Interface Assignment:**
   ```text
   Enter the LAN interface name or 'a' for auto-detection: em1
   ```
   * Type `em1` (or `vtnet1`) and press `Enter`.
5. **Optional Interfaces:**
   ```text
   Enter the Optional 1 interface name or 'a' for auto-detection: [Press ENTER]
   ```
   * Leave blank and press `Enter`.
6. **Confirm Assignments:**
   The screen will summarize:
   ```text
   WAN -> em0
   LAN -> em1

   Do you want to proceed [y|n]? y
   ```
   * Type `y` and press `Enter`.
   * *Verification:* pfSense will reload interface drivers and return to the main console menu.


## Configuring LAN IP address and DHCP 

Lets configure the internal protected interface first so that the management workstation (Fedora) can connect.

1. At the main console menu, enter `2` and press `Enter`.
2. **Select Interface:**
   ```text
   Available interfaces:
   1 - WAN (em0)
   2 - LAN (em1)

   Enter the number of the interface you wish to configure: 2
   ```
   * Type `2` and press `Enter`.
3. **IPv4 Address:**
   ```text
   Enter the new LAN IPv4 address: 192.168.20.1
   ```
4. **Subnet Bit Count:**
   ```text
   Enter the new LAN IPv4 subnet bit count (1 to 31): 24
   ```
5. **Upstream Gateway:**
   ```text
   For a WAN, enter the new LAN IPv4 upstream gateway address: [Press ENTER]
   ```
   * Leave blank (LAN has no upstream gateway) and press `Enter`.
6. **IPv6 Address:**
   ```text
   Enter the new LAN IPv6 address: [Press ENTER]
   ```
   * Leave blank and press `Enter`.
7. **Enable DHCP Server:**
   ```text
   Do you want to enable the DHCP server on LAN [y|n]? y
   ```
   * Type `y` and press `Enter`.
8. **DHCP Range Start:**
   ```text
   Enter the start address of the IPv4 client address range: 192.168.20.100
   ```
9. **DHCP Range End:**
   ```text
   Enter the end address of the IPv4 client address range: 192.168.20.200
   ```
10. **Revert webConfigurator to HTTP:**
    ```text
    Do you want to revert to HTTP as the webConfigurator protocol [y|n]? y
    ```
    * Type `y` and press `Enter` (avoids SSL certificate re-binding issues during initial setup).
11. Press `Enter` to complete configuration and return to the main menu.

## Configuring WAN IP Address & DHCP

Now, lets Configure the untrusted/external side for Kali Linux.

1. At the main console menu, enter `2` and press `Enter`.
2. **Select Interface:**
   ```text
   Enter the number of the interface you wish to configure: 1
   ```
   * Type `1` and press `Enter`.
3. **Disable WAN DHCP Client:**
   ```text
   Configure IPv4 address WAN interface via DHCP [y|n]? n
   ```
   * Type `n` and press `Enter`.
4. **IPv4 Address:**
   ```text
   Enter the new WAN IPv4 address: 192.168.10.1
   ```
5. **Subnet Bit Count:**
   ```text
   Enter the new WAN IPv4 subnet bit count (1 to 31): 24
   ```
6. **Upstream Gateway:**
   ```text
   For a WAN, enter the new WAN IPv4 upstream gateway address: [Press ENTER]
   ```
   * Leave blank and press `Enter`.
7. **IPv6 Address:**
   ```text
   Enter the new WAN IPv6 address: [Press ENTER]
   ```
   * Leave blank and press `Enter`.
8. **Enable DHCP Server on WAN:**
   ```text
   Do you want to enable the DHCP server on WAN [y|n]? y
   ```
   * Type `y` and press `Enter` (allows Kali to automatically receive an IP on `WAN_NET`).
9. **DHCP Range Start:**
   ```text
   Enter the start address of the IPv4 client address range: 192.168.10.100
   ```
10. **DHCP Range End:**
    ```text
    Enter the end address of the IPv4 client address range: 192.168.10.200
    ```
11. **webConfigurator Protocol:**
    ```text
    Do you want to revert to HTTP as the webConfigurator protocol [y|n]? y
    ```
    * Type `y` and press `Enter`.
12. Press `Enter` to return to the main menu.

## Verifying our work on the Main Console Screen

VWe verify the console banner displays both assigned interfaces and their configured addresses:

```text
*** Welcome to pfSense 2.X.X-RELEASE (amd64) on pfSense ***

 WAN (wan)       -> em0        -> v4: 192.168.10.1/24
 LAN (lan)       -> em1        -> v4: 192.168.20.1/24
```
It should look like what I have here:  
<img width="366" height="206" alt="Screenshot 2026-10-21 125536" src="https://github.com/user-attachments/assets/820dfa0c-6ea7-48f0-a2e2-93e34af82934" />

## Client Verification & Web Access
Now we are going to do something fun! We will be verifying if our local network is working or not.

### On Fedora (LAN Client)
1. Verify IP assignment via terminal:
   ```bash
   ip -br a
   ```
   *Output must show `192.168.20.x` on interface `enp0s3`.*
<img width="727" height="433" alt="image" src="https://github.com/user-attachments/assets/5570d988-9d04-48e6-80e2-707c46277f25" />

3. Test gateway connectivity:
   ```bash
   ping -c 3 192.168.20.1
   ```
4. Open browser and access the WebGUI:
   ```text
   http://192.168.20.1
   ```
   * **Username:** `admin`
   * **Password:** `pfsense`
<img width="470" height="243" alt="Screenshot 2026-10-18 144940" src="https://github.com/user-attachments/assets/a69cba79-55d2-4cf7-a497-76a5875de25e" />

* After accessing the WebGUI it will show you this screen. Click on Next. Again click Next on the 2nd screen.
  
<img width="481" height="239" alt="Screenshot 2026-10-18 145205" src="https://github.com/user-attachments/assets/031edac2-f362-4fd2-8c01-f4c631acb460" />  
<img width="478" height="251" alt="Screenshot 2026-10-18 145249" src="https://github.com/user-attachments/assets/360152af-6f1c-427b-b08d-8fa350ca53f8" />  


* Leave this page as it is, Do not change anything and click Next.
  <img width="582" height="401" alt="Screenshot 2026-10-18 145510" src="https://github.com/user-attachments/assets/09f845d1-4f34-48a7-8cca-57cb06e0774e" />
* It will open a new screen with Time Server information. Leave the name as it is and change your time zone to your respective ones. Click Next
  <img width="1164" height="393" alt="image" src="https://github.com/user-attachments/assets/985077d8-5b9e-48d3-a286-c2346966839b" />

* It will open a new screen for WAN configuration, again leave it as it is and click next.
  <img width="577" height="385" alt="Screenshot 2026-10-18 150357" src="https://github.com/user-attachments/assets/87a2c483-01b8-442b-9931-84eda1a1f33a" />
  <img width="679" height="393" alt="Screenshot 2026-10-18 150457" src="https://github.com/user-attachments/assets/e48d910a-72bb-44b2-b7f3-0b1c88ffd7b6" />
* It will open a LAN configuration page. Make sure the information is correct. Set the subnet mask to 24.
  <img width="692" height="401" alt="Screenshot 2026-10-18 150656" src="https://github.com/user-attachments/assets/13cf339a-27fb-4efe-ae87-de0293f68876" />
* Set your new admin password and click Next.
  <img width="620" height="401" alt="Screenshot 2026-10-18 150739" src="https://github.com/user-attachments/assets/e1047575-e79e-40c3-95e5-686db6696224" />
* Click Reload.
  
  <img width="601" height="398" alt="Screenshot 2026-10-18 150922" src="https://github.com/user-attachments/assets/ecdb1513-4e20-45cc-b71a-9f64cbca1480" />
* Click Finish.
  
  <img width="617" height="402" alt="Screenshot 2026-10-18 151003" src="https://github.com/user-attachments/assets/cd4520a6-2914-494e-99f9-0d225ec6c21c" />
* Click Accept.
  
  <img width="602" height="423" alt="Screenshot 2026-10-18 151026" src="https://github.com/user-attachments/assets/1d5b9930-b7de-410b-8a6f-e71f21cd13a6" />

### On Kali Linux (WAN Client)
1. Verify IP assignment via terminal:
   ```bash
   ip -br a
   ```
   *Output must show `192.168.10.x` on interface `eth0`.*
   
<img width="320" height="255" alt="image" src="https://github.com/user-attachments/assets/2b34747e-391b-4b88-bc04-e8ef8f2bc162" />

3. Test WAN gateway reachability:
   ```bash
   ping -c 3 192.168.10.1
   ```
<img width="323" height="257" alt="Screenshot 2026-10-21 141320" src="https://github.com/user-attachments/assets/09d7e414-1d2e-46d7-a24b-7a20e150012a" />


## Common Troubleshooting
This time I added a few issues that I faced and how to troubleshoot them if you face the same issues.

| Issue | Root Cause | Resolution |
|---|---|---|
| **Console shows no LAN interface** | Adapter 2 disabled in VirtualBox | Power off pfSense, enable Adapter 2 under VM Settings > Network, attached to `LAN_NET`. |
| **Fedora shows only link-local IPv6 (`fe80::`)** | Internal Network name mismatch or Promiscuous mode set to Deny | Ensure both pfSense Adapter 2 and Fedora Adapter 1 use identical case `LAN_NET` with Promiscuous Mode set to `Allow All`. |
| **Traffic from Kali blocked before rules run** | RFC1918 Private Network filter active on WAN | In pfSense WebGUI: `Interfaces` > `WAN` > scroll to bottom > uncheck `Block RFC1918 Private Networks` > Save & Apply. |

  
That is all for this guide/walkthrough. If you faced any issues or problems that I dont have then listed here, then please do not shy away to google those problems and troubleshoot them.  

Googling and Troubleshooting problems are underrated skills that will make your cybersecurity journey much much easier.  

Stay curious, learn and explore!  



-Syed Abdul Rauf, 2026
