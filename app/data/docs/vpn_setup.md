# VPN Setup & Troubleshooting

## Setting Up a VPN

1. **Choose a VPN Protocol:**
   - OpenVPN: Most secure, widely supported
   - WireGuard: Fastest, modern protocol
   - L2TP/IPSec: Built into most OS, decent security
   - PPTP: Legacy, not recommended (weak encryption)

2. **Router-Level VPN:**
   - Access router admin panel
   - Navigate to VPN settings
   - Enter server address, credentials, and protocol
   - Enable and save

3. **Device-Level VPN:**
   - Install VPN client software
   - Import configuration file or enter server details
   - Connect and verify IP change at whatismyip.com

## Troubleshooting VPN Issues

1. **VPN Won't Connect:**
   - Check internet connection first
   - Verify credentials are correct
   - Try a different VPN server
   - Check if firewall is blocking VPN ports (1194 for OpenVPN, 51820 for WireGuard)

2. **Slow VPN Speeds:**
   - Connect to a closer server
   - Switch protocol (WireGuard is fastest)
   - Disable split tunneling if not needed
   - Check base internet speed without VPN

3. **VPN Drops Frequently:**
   - Enable kill switch in VPN client
   - Switch from UDP to TCP protocol
   - Update VPN client to latest version
   - Check router firmware for VPN passthrough support

4. **Cannot Access Local Network While on VPN:**
   - Enable split tunneling
   - Add local subnet to VPN exclusion list
   - Check VPN client routing table
