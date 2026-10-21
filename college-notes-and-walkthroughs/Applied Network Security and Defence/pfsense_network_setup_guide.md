# pfSense Lab Setup: Network & Interface Configuration Guide

A step-by-step technical guide for configuring pfSense network interfaces, static IP addressing, and DHCP services inside Oracle VM VirtualBox for an isolated cybersecurity testing topology.

---

## 1. Network Topology Overview

Before configuring interfaces inside the firewall, verify the logical network design:

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

---

## 2. VirtualBox Network Adapter Pre-Check

If pfSense does not detect or display interfaces, verify VirtualBox adapter bindings before starting the VM.

### pfSense VM Settings
1. Power down the **pfSense** VM (`Machine` > `Close` > `Power off the machine`).
2. Navigate to **Settings** > **Network**.
3. **Adapter 1 (Mapped to WAN / em0):**
   * **Enable Network Adapter:** Checked
   * **Attached to:** `Internal Network`
   * **Name:** `WAN_NET`
   * **Advanced > Promiscuous Mode:** `Allow All`
   * **Cable Connected:** Checked
4. **Adapter 2 (Mapped to LAN / em1):**
   * **Enable Network Adapter:** Checked
   * **Attached to:** `Internal Network`
   * **Name:** `LAN_NET`
   * **Advanced > Promiscuous Mode:** `Allow All`
   * **Cable Connected:** Checked
5. Click **OK**.

### Client VM Settings
* **Kali Linux VM:** **Adapter 1** set to `Internal Network`, Name: `WAN_NET`, Promiscuous: `Allow All`.
* **Fedora VM:** **Adapter 1** set to `Internal Network`, Name: `LAN_NET`, Promiscuous: `Allow All`.

---

## 3. Step 1: Assign Physical Interfaces (Console Option 1)

When pfSense boots to the 16-option console menu without interfaces assigned (or interfaces are unassigned/unmapped), start here.

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

---

## 4. Step 2: Configure LAN IP Address & DHCP (Console Option 2)

Configure the internal protected interface first so the management workstation (Fedora) can connect.

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

---

## 5. Step 3: Configure WAN IP Address & DHCP (Console Option 2)

Configure the untrusted/external side for Kali Linux.

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

---

## 6. Step 4: Verification of Main Console Screen

Verify the console banner displays both assigned interfaces and their configured addresses:

```text
*** Welcome to pfSense 2.7.2-RELEASE (amd64) on pfSense ***

 WAN (wan)       -> em0        -> v4: 192.168.10.1/24
 LAN (lan)       -> em1        -> v4: 192.168.20.1/24
```

---

## 7. Step 5: Client Verification & Web Access

### On Fedora (LAN Client)
1. Verify IP assignment via terminal:
   ```bash
   ip -br a
   ```
   *Output must show `192.168.20.x` on interface `enp0s3`.*
2. Test gateway connectivity:
   ```bash
   ping -c 3 192.168.20.1
   ```
3. Open browser and access the WebGUI:
   ```text
   http://192.168.20.1
   ```
   * **Username:** `admin`
   * **Password:** `pfsense`

### On Kali Linux (WAN Client)
1. Verify IP assignment via terminal:
   ```bash
   ip -br a
   ```
   *Output must show `192.168.10.x` on interface `eth0`.*
2. Test WAN gateway reachability:
   ```bash
   ping -c 3 192.168.10.1
   ```

---

## 8. Common Troubleshooting

| Issue | Root Cause | Resolution |
|---|---|---|
| **Console shows no LAN interface** | Adapter 2 disabled in VirtualBox | Power off pfSense, enable Adapter 2 under VM Settings > Network, attached to `LAN_NET`. |
| **Fedora shows only link-local IPv6 (`fe80::`)** | Internal Network name mismatch or Promiscuous mode set to Deny | Ensure both pfSense Adapter 2 and Fedora Adapter 1 use identical case `LAN_NET` with Promiscuous Mode set to `Allow All`. |
| **Traffic from Kali blocked before rules run** | RFC1918 Private Network filter active on WAN | In pfSense WebGUI: `Interfaces` > `WAN` > scroll to bottom > uncheck `Block RFC1918 Private Networks` > Save & Apply. |