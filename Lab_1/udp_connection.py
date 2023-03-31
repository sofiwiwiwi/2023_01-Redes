import socket
    host = "jdiaz.inf.santiago.usm.cl"
    port = 50008
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    msj = "GET NEW IMG DATA".encode()
    s.sendto(msj, (host,port))
    respuesta = s.recvfrom(1024)[0].decode()
    #ahora hay que aplicar string handle para sacar la info
    #ID:X W:X H:X P1TCP:X P2UDP:X PV:X
    #ID:X W:X H:X P1TCP:X P2UDP:X P3UDP:X PV:X
    res = respuesta.strip().split()
    arr = []
    for elem in res:
       arr.append(elem.split(":")[1])
    buff = (int)arr[1]* (int)arr[2]
    #if(res[-2].split(":")[0] == "PV"): #este corresponde al primer input
    
    #else:
    print(respuesta, buff, arr, len(arr))      