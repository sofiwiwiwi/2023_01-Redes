import socket
success = "poto"

while(success != "200: SUCCESS"):
    #MENSAJE PARA OBTENER DATOS DE LA IMAGEN
    host = "jdiaz.inf.santiago.usm.cl"
    port = 50008
    print("\n** NUEVO INTENTO **")
    msg = "GET NEW IMG DATA".encode()
    arr = []
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.sendto(msg, (host,port))
    print(f"Mensaje enviado a {host}:{port} por UDP: {msg}")
    respuesta = s.recvfrom(1024)[0].decode()
    res = respuesta.strip().split()
    print(f"Mensaje recidibo de {host}:{port} por UDP: {respuesta}")
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
    print(f"Mensaje enviado a {host}:{port} por TCP: {msg}")
    respuesta1 = d.recvfrom(int(buff))[0]
    print(f"Mensaje recidibo de {host}:{port} por TCP")
    name = f"{arr[0]}.png"
    image = open(name, "wb")
    print("Comenzando escritura de la imagen :o")
    image.write(respuesta1)
    d.close()

    if(len(arr) == 6): #este corresponde al primer input
        msg =f"GET 2/2 IMG ID:{str(arr[0])}"
    else:
        msg=f"GET 2/3 IMG ID:{str(arr[0])}"
    port =arr[4]
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.sendto(msg.encode(), (host,port))
    print(f"Mensaje enviado a {host}:{port} por UDP: {msg}")
    respuesta2 = s.recvfrom(buff)[0] 
    print(f"Mensaje recidibo de {host}:{port} por UDP")
    image.write(respuesta2)
    s.close()

    flag = False
    if(len(arr) == 7): #este corresponde al primer input
        flag = True
        port = arr[5]
        msg=f"GET 3/3 IMG ID:{str(arr[0])}"
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.sendto(msg.encode(), (host,port))
        print(f"Mensaje enviado a {host}:{port} por UDP: {msg}")
        respuesta3 = s.recvfrom(buff)[0]
        print(f"Mensaje recidibo de {host}:{port} por UDP")
        image.write(respuesta3)
        s.close()
    
    port = arr[-1]
    d=socket.socket(socket.AF_INET,socket.SOCK_STREAM )  #conexion por tcp
    d.connect((host,port)) 
    if flag:
        complete_image = f"{respuesta1}{respuesta2}{respuesta3}"
    complete_image= f"{respuesta1}{respuesta2}"
        
    d.sendto(complete_image.encode(), (host,port))
    print(f"Mensaje enviado a {host}:{port} por TCP")
    success = d.recvfrom(1024)[0].decode()
    print(f"Mensaje recibido de {host}:{port} por TCP: {success}")
    print("** FIN **\n")
    d.close()
    image.close()

print("Imagen recibida :D")
