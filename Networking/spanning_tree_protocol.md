# Spanning Tree Protocol (STP)

## Objective
To understand how Spanning Tree Protocol prevents switching loops in Ethernet networks.

## What is STP?
Spanning Tree Protocol (STP) is a Layer 2 network protocol that prevents loops when switches have multiple connections between them.

## Why is STP Needed?
Redundant links provide alternative paths if a connection fails. However, they can create switching loops. STP helps prevent these loops by placing selected redundant paths into a non-forwarding state.

## How STP Works
1. Switches exchange Bridge Protocol Data Units (BPDUs).
2. They elect a Root Bridge.
3. They determine the best paths to the Root Bridge.
4. Redundant paths are placed into a non-forwarding state.
5. If the active path fails, STP can recalculate the network topology.

## Important Terms
- Root Bridge – The central reference switch selected by STP.
- BPDU – Messages exchanged by switches.
- Root Port – The best path towards the Root Bridge.
- Designated Port – The forwarding port selected for a network segment.
- Blocking Port – A port that does not forward normal data traffic in classic STP.

## Real-Life Example
In an office network, three switches may have multiple connections for reliability. STP helps prevent loops while keeping a backup path available.

## Learning Outcomes
- Understanding Layer 2 switching loops.
- Learning the purpose of STP.
- Understanding Root Bridge election.
- Learning how redundant paths are managed.

## Result
Understood how STP helps maintain a loop-free Ethernet network.

