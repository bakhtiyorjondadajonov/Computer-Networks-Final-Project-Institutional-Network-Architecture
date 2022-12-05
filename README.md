# Computer-Networks-Final-Project-Institutional-Network-Architecture

##The following tasks are performed on the server:


1. Establishing a connection with a client: It is the server's responsibility to establish a connection with a client. This is possible with the Python socket module. Access to the BSD socket interface is provided by the socket module. The server will need to know the client's host address and port number.
The server can begin sending and receiving data from the client once the connection is established.


2. Receiving files from the client: Receiving files from the client will be handled by the server.
This is possible with the Python socket module.
The server will need to know the client's host address and port number. The data received from the client will then be deserialized by the server.

3. File distribution to multiple clients:

The server will be in charge of distributing files to multiple clients. This is possible with the Python socket module. The server must specify the destination clients' host address and port number.
The data will then be serialized and sent to the destination clients by the server.

4. Keeping a list of connected clients: The server will be in charge of keeping a list of connected clients.
This is possible with the Python list data structure.
The server must keep a list of each client's host address and port number.



## Description
In order to demonstrate the proposed 
P2P system, the following tools will be used:

1. Cisco Packet Tracer: This will be used to create 
a network topology for the P2P system Packet Tracer
is a network simulator developed by Cisco Systems. 
It allows users to design, configure, and simulate 
a network topology. This can be used to create a network
topology for the proposed P2P system.

2. Wireshark: This will be used to capture the network traffic
and analyze the results. Wireshark is a network protocol
analyzer. It allows users to capture and analyze network
traffic. This can be used to capture the network traffic of 
the proposed P2P system and analyze the results.


Well commented code will be used throughout the 
development of the proposed system in order to
make the code more readable and understandable.
Comments are lines of code that are not executed 
by the interpreter but are used to explain the code.
This makes it easy for someone who is not familiar
with the code to understand what the code is doing. 
This will help to ensure that the proposed system is
developed correctly and is easy to maintain.

In conclusion, the proposed Python 3- based P2P
system using TCP protocol consists of two main tasks: 
client-side operations and server-side operations.
The client-side operations involve tasks such as sending 
and receiving files, broadcasting files to multiple clients, 
and displaying a menu form that allows the user to select 
choices. The server- side operations involve tasks such as
establishing a connection with a client, receiving files from
the client, broadcasting files to multiple clients, and maintaining 
a list of connected clients. The proposed system will be
demonstrated using Cisco Packet Tracer and Wireshark.
Well commented code will also be used throughout 
the development of the proposed system.
