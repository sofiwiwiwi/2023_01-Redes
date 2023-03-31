import socket
host = "jdiaz.inf.santiago.usm.cl"
port = 50008

msj = "GET NEW IMG DATA".encode()
arr = []
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(msj, (host,port))
respuesta = s.recvfrom(1024)[0].decode()
res = respuesta.strip().split()
s.close()
#ID:X W:X H:X P1TCP:X P2UDP:X PV:X
#ID:X W:X H:X P1TCP:X P2UDP:X P3UDP:X PV:X
for elem in res:
    arr.append(elem.split(":")[1])
buff = int(arr[1])*int(arr[2]) *3
arr = [int(i) for i in arr]
port = arr[3]
if(len(arr) == 6): #este corresponde al primer input
    msg =f"GET 1/2 IMG ID:{str(arr[0])}"
else:
    msg=f"GET 1/3 IMG ID:{str(arr[0])}"
d=socket.socket(socket.AF_INET,socket.SOCK_STREAM )  #conexion por tcp
d.connect((host,port))
d.sendto(msg.encode(), (host,port))
respuesta = d.recvfrom(int(buff))[0]
image = open("image.png", "wb")
image.write(respuesta)
d.close()

if(len(arr) == 6): #este corresponde al primer input
    msg =f"GET 2/2 IMG ID:{str(arr[0])}"
else:
    msg=f"GET 2/3 IMG ID:{str(arr[0])}"
port =arr[4]
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(msg.encode(), (host,port))
respuesta = s.recvfrom(buff)[0]
image.write(respuesta)
s.close()
if(len(arr) == 7): #este corresponde al primer input
    port = arr[5]
    msg=f"GET 3/3 IMG ID:{str(arr[0])}"
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.sendto(msg.encode(), (host,port))
    respuesta = s.recvfrom(buff)[0]
    image.write(respuesta)
    s.close()

