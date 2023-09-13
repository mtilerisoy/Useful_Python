import socket

# Define the constants
IP = ""
PORT = ""
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    print("Server is starting.")
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializing a TCP socket.
    server.bind(ADDR) # Bind the IP and PORT to the server.
    server.listen() # Server is listening for new connections

    print("Server is listening.")
    
    while True:

        conn, addr = server.accept() # Accept incoming connections
        print(f"[NEW CONNECTION] {addr} connected.")
        
        filename = conn.recv(SIZE).decode(FORMAT) # Recieve the file name
        print(f"[RECV] Receiving the filename.")
        file = open(filename, "w")
        
        conn.send("Filename received.".encode(FORMAT)) # Send the confirmation message to the server
        
        data = conn.recv(SIZE).decode(FORMAT) #  Recieve the data from the server
        print(f"[RECV] Receiving the file data.")
        file.write(data)
        
        conn.send("File data received".encode(FORMAT)) # Send the confirmation message to the server
        
        file.close() # Close the file
        conn.close() # Close the connection
        print(f"[DISCONNECTED] {addr} disconnected.")

if __name__ == "__main__":
    main()