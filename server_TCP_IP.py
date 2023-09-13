import socket

# Define the constants
IP = ""
PORT = ""
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializing a TCP socket.
    client.connect(ADDR) # Connect to the client
    
    file = open("data/yt.txt", "r") # Open the file tı be transfered
    data = file.read()
    
    client.send("yt.txt".encode(FORMAT))    # Send the naem of the file to the client
    msg = client.recv(SIZE).decode(FORMAT)  # Recieve the confirmation message
    print(f"[SERVER]: {msg}")
    
    client.send(data.encode(FORMAT))        # Send the data of the file
    msg = client.recv(SIZE).decode(FORMAT)  # Recieve the confirmation message
    print(f"[SERVER]: {msg}")
    
    file.close()    # Close the file
    client.close()  # Close the connection
if __name__ == "__main__":
    main()