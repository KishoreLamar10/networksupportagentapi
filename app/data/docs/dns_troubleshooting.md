# DNS Troubleshooting Guide

## Symptoms
- Websites not loading but ping to IP addresses works
- "DNS_PROBE_FINISHED_NXDOMAIN" error in browser
- Slow DNS resolution

## Steps

1. **Flush DNS Cache:**
   - Windows: `ipconfig /flushdns`
   - macOS: `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder`
   - Linux: `sudo systemd-resolve --flush-caches`

2. **Change DNS Servers:**
   - Open router admin panel (usually 192.168.1.1)
   - Navigate to WAN/Internet settings
   - Set Primary DNS: `8.8.8.8` (Google)
   - Set Secondary DNS: `1.1.1.1` (Cloudflare)

3. **Test DNS Resolution:**
   - Run `nslookup google.com`
   - If it resolves, DNS is working
   - If not, check firewall or ISP DNS blocking

4. **Check /etc/hosts File:**
   - Ensure no entries are blocking the target domain
   - Remove any suspicious entries

5. **Contact ISP:**
   - If all else fails, your ISP's DNS may be down
   - Use public DNS servers as a workaround
