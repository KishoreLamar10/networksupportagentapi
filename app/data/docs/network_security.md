# Network Security Best Practices

## Securing Your Home Network

### 1. Change Default Router Credentials
- Default admin passwords are publicly known
- Change both username and password in router admin panel
- Use a strong, unique password (12+ characters)

### 2. Use Strong WiFi Encryption
- **WPA3** is the most secure (use if available)
- **WPA2-AES** is the minimum acceptable standard
- **Never use WEP** — it can be cracked in minutes
- Check encryption type in router WiFi security settings

### 3. Create a Strong WiFi Password
- Minimum 12 characters
- Mix of uppercase, lowercase, numbers, and symbols
- Avoid dictionary words and personal information
- Change password periodically (every 6-12 months)

### 4. Enable Network Segmentation
- Create a separate Guest network for visitors
- IoT devices (smart home) should be on their own network
- This limits damage if one device is compromised

### 5. Disable WPS (WiFi Protected Setup)
- WPS has known security vulnerabilities
- Disable in router admin panel under WiFi settings
- Use manual password entry instead

### 6. Keep Firmware Updated
- Enable automatic updates if available
- Check manufacturer website monthly for security patches
- Outdated firmware is a common attack vector

### 7. Disable Remote Management
- Turn off remote administration in router settings
- Only manage router from within your local network
- If remote access is needed, use VPN instead

### 8. Monitor Connected Devices
- Regularly check router's connected devices list
- Remove any unknown devices
- Enable MAC address filtering for additional control
- Set up alerts for new device connections if supported

### 9. Use a Firewall
- Enable router's built-in firewall
- Configure SPI (Stateful Packet Inspection)
- Block incoming connections by default
- Only allow specific ports as needed

### 10. Consider Additional Security
- Use DNS filtering (e.g., OpenDNS, NextDNS) to block malicious sites
- Enable DoH (DNS over HTTPS) for privacy
- Use a VPN for sensitive activities
- Regularly scan devices for malware
