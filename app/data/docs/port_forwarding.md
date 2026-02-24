# Port Forwarding Guide

## When You Need Port Forwarding
- Hosting a game server
- Running a web server from home
- Remote desktop access
- Security camera remote viewing
- NAS access from outside your network

## Setup Steps

1. **Find Your Device's Local IP:**
   - Windows: `ipconfig` → look for IPv4 Address
   - macOS: `ifconfig en0` → look for inet
   - Linux: `ip addr show`
   - Assign a static IP to avoid changes

2. **Access Router Admin Panel:**
   - Open browser and go to 192.168.1.1 or 192.168.0.1
   - Log in with admin credentials
   - Navigate to Port Forwarding / Virtual Server section

3. **Create Port Forwarding Rule:**
   - Service Name: Descriptive name (e.g., "Minecraft Server")
   - External Port: The port others will connect to
   - Internal Port: Usually the same as external
   - Internal IP: Your device's local IP
   - Protocol: TCP, UDP, or Both
   - Enable the rule and save

4. **Common Ports to Forward:**
   | Service | Port | Protocol |
   |---------|------|----------|
   | Web Server (HTTP) | 80 | TCP |
   | Web Server (HTTPS) | 443 | TCP |
   | Minecraft | 25565 | TCP |
   | SSH | 22 | TCP |
   | FTP | 21 | TCP |
   | Remote Desktop | 3389 | TCP |
   | Plex Media | 32400 | TCP |

5. **Verify Port is Open:**
   - Visit canyouseeme.org
   - Enter the forwarded port
   - If closed, check firewall and ISP restrictions

## Security Considerations
- Only forward ports you actively need
- Use non-standard ports when possible
- Enable firewall rules alongside port forwarding
- Consider using a VPN instead for remote access
