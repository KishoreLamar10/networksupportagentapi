# DHCP Troubleshooting Guide

## Symptoms
- Device gets "169.254.x.x" IP address (APIPA)
- "Unable to obtain IP address" error
- Multiple devices with the same IP address
- Device connects to WiFi but has no internet

## Steps

1. **Release and Renew IP Address:**
   - Windows: `ipconfig /release` then `ipconfig /renew`
   - macOS: System Preferences → Network → Advanced → TCP/IP → Renew DHCP Lease
   - Linux: `sudo dhclient -r` then `sudo dhclient`

2. **Check DHCP Server on Router:**
   - Access router admin panel
   - Navigate to LAN/DHCP settings
   - Ensure DHCP server is enabled
   - Check IP pool range (e.g., 192.168.1.100 - 192.168.1.254)
   - Verify lease time is reasonable (24 hours default)

3. **Check for IP Conflicts:**
   - Two devices may have the same static IP
   - Remove static IPs and let DHCP assign automatically
   - Or assign unique static IPs outside the DHCP pool range

4. **Verify Subnet Mask:**
   - Most home networks use 255.255.255.0
   - Incorrect subnet mask prevents communication
   - Check router and device settings match

5. **Restart DHCP Service:**
   - Restart the router (power cycle for 30 seconds)
   - This resets the DHCP lease table
   - Devices will request new IPs on reconnection

6. **Check for Rogue DHCP Servers:**
   - Multiple DHCP servers on a network cause conflicts
   - Disable DHCP on any secondary routers or access points
   - Only one device should serve DHCP per network
