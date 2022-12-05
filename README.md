# Computer-Networks-Final-Project-Institutional-Network-Architecture

Connection with a server establishment: The client is in charge of making the connection with the server. The socket module for Python can be used for this. Access to the BSD socket interface is made available by the socket module. The host address and port number of the server must be provided by the client.
The client can start transmitting and receiving data to and from the server as soon as the connection is made.

2. Sending photos, CSV, and JSON files to another client: The customer is in charge of sending files to another client, including images, CSV, and JSON files. The socket module for Python can be used for this. The host address and port number of the destination client must be specified by the client.


The data will then be serialized by the client and sent to the target client.

3. Distributing a file to several clients: Distributing a file to numerous clients will be the client's responsibility. The socket module for Python can be used for this. The host address and port number of the destination clients must be specified by the client. The data will then be serialized by the client and sent to the target clients.

4. Displaying a menu form that enables choice-making by the user: The client is in charge of displaying a menu form that enables choice-making by the user. Using the Python Tkinter module, this is possible. For applications, the Tkinter package offers a GUI (graphical user interface).


A window and widgets like text boxes and buttons must be created by the client. The user can then choose from a variety of options on the menu form.

5. Establishing a timeout before transferring a file and calculating the end-to-end delay for each scenario: Each scenario's end-to-end latency must be calculated by the client, who must also set a timeout before transmitting a file.
The Python time module can be used to accomplish this. The time module offers tools for handling dates and time. Following that, the client can determine how long it takes for a file to be sent and received. If it takes too long, the client can also set a timeout for sending a file.





## The following tasks are performed on the server:


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

P2P system, the giving tools will be utilised:

1. Cisco Packet Tracer: This will be used to compose 
a network topology for the P2P system Packet Tracer
is a network simulator developed by Cisco Systems. 
It gives a chance users to design, configure, and simulate 
a network topology. This can be used to create a network
topology for the proposed P2P system.

2. Wireshark: This will be used to gain the network traffic
and make analyzation the results. Wireshark is a network protocol
analyzer. It makes users to capture and analyze network
traffic. This can be used to capture the network traffic of 
the suggested P2P system and analyze the results.

Well commented code will be utilized throughout the 
development of the suggested system in order to
make the code more readable and understandable.
Comments are lines of code that are not executed 
by the interpreter but are used to explain the code.
This makes it easy for someone who is not simiiliar
with the code to understand what the code is doing. 
This will help to ensure that the proposed system is
developed correctly and is easy to maintain.

In conclusion, the proposed Python 3- based P2P
system using TCP protocol consists of two main tasks: 
client-side operations and server-side operations.
The client-side operations include tasks such as sending 
and receiving files, broadcasting files to multiple clients, 
and displaying a menu form that allows the user to select 
choices. The server- side operations involve tasks such as
establishing a connection with a client, receiving files from
the client, broadcasting files to multiple clients, and maintaining 
a list of connected clients. The suggested system will be
demonstrated using Cisco Packet Tracer and Wireshark.
Well being commented code will also be used throughout 
the development of the suggested system
