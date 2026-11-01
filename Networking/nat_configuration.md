# Network Address Translation (NAT)

## Objective
To understand how NAT allows devices in a private network to communicate with external networks using translated IP addresses.

## What is NAT?
Network Address Translation (NAT) is a networking technique that translates IP addresses between private and public networks.

## Types of NAT
1. Static NAT – Maps one private IP address to one public IP address.
2. Dynamic NAT – Maps private addresses using a pool of public addresses.
3. PAT (Port Address Translation) – Allows multiple private devices to share a public IP address using port numbers.

## Requirements
- Cisco Packet Tracer
- Router
- Switch
- PCs
- External network/server

## Working
1. A PC sends data to an external network.
2. The router receives the packet.
3. NAT translates the private source IP address.
4. The translated packet is sent to the external network.
5. The router uses its translation information to deliver returning traffic to the correct internal device.

## Real-Life Example
Multiple devices at home use private IP addresses but share one public IP address to access the internet through a router. This commonly uses PAT.

## Learning Outcomes
- Understanding private and public IP addresses.
- Learning how NAT works.
- Understanding Static NAT, Dynamic NAT, and PAT.
- Introduction to router-based address translation.

## Result
Understood the purpose and basic working of Network Address Translation.


