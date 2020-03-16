import socket
import pickle

HOST = socket.gethostname()  # Standard loopback interface address (localhost)
PORT = 1234        # Port to listen on (non-privileged ports are > 1023)

students = [
  {
    'id': '1',
  	'name': "Phan Anh",
  	'age': '20'
  },
  {
  	'id': '2',
  	'name': "Luu Le Tuan Dat",
  	'age': '20'
  }
]

def getStudent(studentId):
	for student in students:
		print(student)
		if studentId == student['id']:
			return student

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
                
                result = getStudent(data.decode('utf-8'))

                send_data = pickle.dumps(result)
                conn.sendall(send_data)