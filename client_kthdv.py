import socket
import pickle

HOST = socket.gethostname()  # The server's hostname or IP address
PORT = 1234        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    student_id = '123'
    send_data = bytes(student_id, 'utf-8')

    s.sendall(send_data)
    data = s.recv(1024)
    data = pickle.loads(data)

print('Received:\n', repr(data))