import socket

success = "gatito uwu"
attempt = 1
while(success != "200: SUCCESS"):
    host = "jdiaz.inf.santiago.usm.cl"
    port = 50008
    print(f"\n** NUEVO INTENTO: INTENTO NUMERO {attempt}**")

    #obtención de datos de la imagen por udp
    msg = "GET NEW IMG DATA".encode()
    image_properties = []
    u1=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    u1.sendto(msg, (host,port))
    print(f"Mensaje enviado a {host}:{port} por UDP: {msg}")
    response = u1.recvfrom(1024)[0].decode()
    res = response.strip().split()
    print(f"Mensaje recidibo de {host}:{port} por UDP: {response}")
    u1.close()
    print("Comenzando escritura de la imagen :o")

    for i in res:
        image_properties.append(i.split(":")[1])

    #calculo del tamaño de la imagen
    buff = int(image_properties[1])*int(image_properties[2]) *3
    image_properties = [int(i) for i in image_properties]
    port = image_properties[3]

    if(len(image_properties) == 6): #este corresponde al primer input
        msg =f"GET 1/2 IMG ID:{str(image_properties[0])}"
    else:
        msg=f"GET 1/3 IMG ID:{str(image_properties[0])}"  

    #obtencion primera parte de la imagen por tcp
    t1=socket.socket(socket.AF_INET,socket.SOCK_STREAM )  #conexion por tcp
    t1.connect((host,port))
    t1.sendto(msg.encode(), (host,port))
    print(f"Mensaje enviado a {host}:{port} por TCP: {msg}")
    part1 = t1.recvfrom(int(buff))[0]
    print(f"Mensaje recidibo de {host}:{port} por TCP")
    t1.close()

    #obtencion segunda parte de la imagen con udp
    if(len(image_properties) == 6): 
        msg =f"GET 2/2 IMG ID:{str(image_properties[0])}"
    else:
        msg=f"GET 2/3 IMG ID:{str(image_properties[0])}"
    port =image_properties[4]
    u2=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    u2.sendto(msg.encode(), (host,port))
    print(f"Mensaje enviado a {host}:{port} por UDP: {msg}")
    part2 = u2.recvfrom(buff)[0] 
    print(f"Mensaje recidibo de {host}:{port} por UDP")
    u2.close()

    #obtencion tercera parte de la imagen con udp
    flag = False
    if(len(image_properties) == 7): 
        flag = True
        port = image_properties[5]
        msg=f"GET 3/3 IMG ID:{str(image_properties[0])}"
        u3=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        u3.sendto(msg.encode(), (host,port))
        print(f"Mensaje enviado a {host}:{port} por UDP: {msg}")
        part3 = u3.recvfrom(buff)[0]
        print(f"Mensaje recidibo de {host}:{port} por UDP")
        u3.close()

    #mensaje de verificación por tcp
    port = image_properties[-1]
    t2=socket.socket(socket.AF_INET,socket.SOCK_STREAM )  #conexion por tcp
    t2.connect((host,port)) 
    if flag:
        complete_image = part1 + part2 + part3
    complete_image= part1 + part2
    
    t2.sendto(complete_image, (host,port))
    print(f"Mensaje enviado a {host}:{port} por TCP")
    success = t2.recvfrom(1024)[0].decode()
    print(f"Mensaje recibido de {host}:{port} por TCP: {success}")
    print(F"** FIN DE INTENTO {attempt}**\n")
    attempt += 1
    t2.close()


#Escritura de la imagen
name = f"{image_properties[0]}.png"
image = open(name, "wb")
image.write(complete_image)
image.close()
print("Imagen recibida y escritura finalizada :D")