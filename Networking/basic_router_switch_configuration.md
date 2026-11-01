# Basic Router and Switch Configuration

## Objective
To understand how to connect and configure a router, switch, and PCs using Cisco Packet Tracer.

## Requirements
- Cisco Packet Tracer
- 1 Router
- 1 Switch
- 2 PCs
- Ethernet cables

## Network Topology
PC0 → Switch → Router

PC1 → Switch

## Procedure
1. Open Cisco Packet Tracer.
2. Place one router, one switch, and two PCs.
3. Connect both PCs to the switch using copper straight-through cables.
4. Connect the switch to the router using a copper straight-through cable.
5. Configure suitable IP addresses for the PCs.
6. Configure the router interface with an IP address.
7. Enable the router interface.
8. Test connectivity using the ping command.

## Example IP Addressing

| Device | IP Address |
|---|---|
| Router LAN interface | 192.168.1.1 |
| PC0 | 192.168.1.2 |
| PC1 | 192.168.1.3 |

Subnet mask for all devices: 255.255.255.0

Default gateway for both PCs: 192.168.1.1

## Verification
Use the `ping` command between the PCs and the router to check connectivity.

## Learning Outcomes
- Understanding router and switch connections.
- Basic IP addressing.
- Router interface configuration.
- Testing network connectivity.

## Result
Successfully learned the basic process of connecting and configuring a router, switch, and PCs in Cisco Packet Tracer.

