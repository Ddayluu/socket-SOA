import socket
import pickle

HOST = socket.gethostname()  # Standard loopback interface address (localhost)
PORT = 1234        # Port to listen on (non-privileged ports are > 1023)

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("Recieved data from client", repr(data))
                
                send_data = {
                    1: "content",
                    2: "load"
                }
                send_data = pickle.dumps(send_data)
                conn.sendall(send_data)