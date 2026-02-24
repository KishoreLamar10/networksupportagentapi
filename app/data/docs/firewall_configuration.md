# Firewall Configuration Guide

## Common Firewall Issues
- Applications unable to connect to the internet
- Certain ports blocked unexpectedly
- VPN or remote desktop not working

## Steps

1. **Check Firewall Status:**
   - Windows: `netsh advfirewall show allprofiles`
   - macOS: System Preferences → Security & Privacy → Firewall
   - Linux: `sudo ufw status` or `sudo iptables -L`

2. **Allow an Application Through Firewall:**
   - Windows: Control Panel → Windows Defender Firewall → Allow an app
   - macOS: System Preferences → Security → Firewall Options → Add app
   - Linux: `sudo ufw allow <port>/tcp`

3. **Open Specific Ports:**
   - Common ports: 80 (HTTP), 443 (HTTPS), 22 (SSH), 3389 (RDP)
   - Router: Forward ports in admin panel under Port Forwarding
   - OS: Add inbound/outbound rules for the port

4. **Temporarily Disable Firewall (Testing Only):**
   - Windows: `netsh advfirewall set allprofiles state off`
   - macOS: `sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate off`
   - Linux: `sudo ufw disable`
   - **Re-enable immediately after testing**

5. **Reset Firewall to Defaults:**
   - Windows: `netsh advfirewall reset`
   - macOS: Remove `/Library/Preferences/com.apple.alf.plist` and restart
   - Linux: `sudo ufw reset`
