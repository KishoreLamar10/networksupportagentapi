# IP Conflict Resolution Guide

## Symptoms
- "IP address conflict detected" warning
- Devices intermittently losing connection
- Unable to connect to network
- Two devices fighting for the same IP

## Steps

1. **Identify the Conflict:**
   - Windows: You'll see "Windows has detected an IP address conflict"
   - Check which devices have the same IP using router admin panel
   - Run `arp -a` to see all IP-to-MAC mappings on the network

2. **Release and Renew IP:**
   - Windows: `ipconfig /release` then `ipconfig /renew`
   - macOS: Network Preferences → Renew DHCP Lease
   - This requests a new, unique IP from the router

3. **Remove Static IP Assignments:**
   - If a device has a static IP that conflicts with DHCP range, change it
   - Either set the device to DHCP (automatic)
   - Or assign a static IP outside the DHCP pool range

4. **Configure DHCP Reservations:**
   - In router admin panel, find DHCP Reservation
   - Assign specific IPs to device MAC addresses
   - This prevents future conflicts while keeping static-like assignments

5. **Expand DHCP Pool:**
   - If many devices are connected, DHCP pool may be exhausted
   - Expand range (e.g., 192.168.1.10 to 192.168.1.250)
   - Reduce lease time to free up unused IPs faster

6. **Restart Router:**
   - Power cycle clears the DHCP lease table
   - All devices will request fresh IPs
   - Resolves most conflict issues immediately
