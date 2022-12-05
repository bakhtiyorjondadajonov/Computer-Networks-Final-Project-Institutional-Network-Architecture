import time
import csv
import json
import socket
Python code for the proposed P2P system

# Importing the necessary libraries

# Creating a socket object
s = socket.socket()

# Defining the port on which the connection will be established
port = 12345

# Connecting to the server using the connect() function
s.connect(('127.0.0.1', port))

# Receiving the data from the server
data = s.recv(1024)

# Printing the data received from the server
print("Data received from the server : " + str(data.decode()))

# Sending the data to the server
s.send(str.encode("Hello from Client!"))

# Receiving the data from the server
data = s.recv(1024)

# Printing the data received from the server
print("Data received from the server : " + str(data.decode()))

# Sending the data to the server
s.send(str.encode("Send me a JSON file"))

# Receiving the data from the server
data = s.recv(1024)

# Printing the data received from the server
print("Data received from the server : " + str(data.decode()))

# Calculating the end to end latency
start_time = time.time()

# Converting the data received from the server into a JSON object
json_data = json.loads(data.decode())

# Printing the JSON object
print("JSON object : " + str(json_data))

# Calculating the end to end latency
end_time = time.time()

# Calculating the total latency
total_time = end_time - start_time

# Printing the total latency
print("Total latency : " + str(total_time))

# Setting a timeout for sending a file
timeout = 10

# Sending the data to the server
s.send(str.encode("Send me a CSV file"))

# Receiving the data from the server
data = s.recv(1024)

# Printing the data received from the server
print("Data received from the server : " + str(data.decode()))

# Calculating the end to end latency
start_time = time.time()

# Converting the data received from the server into a CSV object
csv_data = csv.reader(data.decode().splitlines(), delimiter=',')

# Printing the CSV object
print("CSV object : " + str(csv_data))

# Calculating the end to end latency
end_time = time.time()

# Calculating the total latency
total_time = end_time - start_time

# Printing the total latency
print("Total latency : " + str(total_time))

# Setting a timeout for sending a file
timeout = 10

# Sending the data to the server
s.send(str.encode("Broadcast the file to multiple clients"))

# Receiving the data from the server
data = s.recv(1024)

# Printing the data received from the server
print("Data received from the server : " + str(data.decode()))

# Calculating the end to end latency
start_time = time.time()

# Broadcasting the file to multiple clients
for client in clients:
    s.send(data)

# Calculating the end to end latency
end_time = time.time()

# Calculating the total latency
total_time = end_time - start_time

# Printing the total latency
print("Total latency : " + str(total_time))

# Setting a timeout for sending a file
timeout = 10

# Closing the connection
s.close()
