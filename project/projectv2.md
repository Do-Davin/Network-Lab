vlan 2 = 10, Staff
    3 = 20, Student
    4 = 90 Management

```
The purpose of this project is to build a centralized and secure wireless network for a university campus using a Wireless LAN Controller (WLC).
The WLC allows all Access Points to be managed from one place and ensures smooth user mobility across the campus.

Two separate wireless networks are created to control access levels:

Staff-Secure uses WPA2-Enterprise with RADIUS for strong authentication.

Student-Guest uses WPA2-PSK for easy student access.

DHCP Snooping is configured on switches to protect the network from rogue devices.

Overall, this project reflects a real enterprise campus Wi-Fi design that focuses on mobility, security, and centralized management.
```

# Router Configuration (R1)
```bash
Router>enable
# Moves from user mode to privileged mode to allow configuration.
R1#configure terminal
# Enters global configuration mode to change device settings.
R1(config)#hostname R1
# Sets the name of the router to "R1".
R1(config)#interface G0/1.2
# Creates a virtual sub-interface to enable "Router-on-a-stick" for VLAN 10.
R1(config-subif)#encapsulation dot1Q 10
# Assigns the sub-interface to handle 802.1Q traffic for VLAN 10.
R1(config-subif)#ip helper-address 172.20.1.2
# Tells the router to forward DHCP requests to the Wireless Controller's IP address.
```
# Switch Configuration (S2)
```bash
Switch#configure terminal
# Enters the main configuration mode for the switch.
S2(config)#vlan 10
# Creates a specific Virtual LAN with ID 10
S2(config-vlan)#name staff
# Names the VLAN "staff" for identification.
S2(config)#ip default-gateway 172.20.4.1
# Configures the management gateway so the switch can be reached from other networks.
S2(config-if)#switchport mode trunk
# Sets a port to carry traffic for multiple VLANs at once.
S2(config-if)#switchport trunk native vlan 90
# Designates VLAN 90 as the native (untagged) VLAN for management traffic on the trunk.
```
# Verification Commands
```bash
R1#show ip interface brief
# Provides a summary table of all interfaces and their current status/IPs.
C:\>ipconfig /renew
# (On the Laptop) Forces the device to ask the WLC/DHCP server for a new IP address.
```