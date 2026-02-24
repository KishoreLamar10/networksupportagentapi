# Ethernet Troubleshooting Guide

## Symptoms
- No internet when connected via Ethernet cable
- Ethernet connection drops intermittently
- Slow speeds on wired connection
- "Network cable unplugged" error

## Steps

1. **Check Physical Connections:**
   - Ensure Ethernet cable is firmly plugged into both the device and router/switch
   - Check for a solid green/amber light on the Ethernet port
   - No light = no physical connection

2. **Test the Cable:**
   - Try a different Ethernet cable
   - Check for visible damage (bent pins, frayed wires)
   - Cat5e supports up to 1 Gbps; Cat6 supports up to 10 Gbps
   - Replace cables older than 5+ years

3. **Check Network Adapter:**
   - Windows: Device Manager → Network adapters
   - Ensure Ethernet adapter is enabled and no yellow warning icon
   - Right-click → Disable, then Enable
   - Update driver if available

4. **Reset Network Settings:**
   - Windows: `netsh winsock reset` and `netsh int ip reset` then restart
   - macOS: Remove and re-add Ethernet in Network Preferences
   - Linux: `sudo systemctl restart NetworkManager`

5. **Check Speed and Duplex Settings:**
   - Open adapter properties
   - Set Speed & Duplex to "Auto Negotiation"
   - Mismatched settings cause slow speeds or drops

6. **Test Router Port:**
   - Try a different LAN port on the router
   - A failed port gives no light and no connection
   - If all ports fail, router may need replacement

## When to Replace Hardware
- Cable: Damaged, old Cat5 or below
- Router: Multiple dead ports
- Adapter: Persistent driver issues, physical damage
- Switch: Overheating, intermittent connectivity
