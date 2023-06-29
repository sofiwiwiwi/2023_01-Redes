Integrantes: 
    - Sofía Riquelme
    202073615-4

    - Javier Pérez
    202004533-k

Instrucciones
Esta tarea fue hecha con linux 22.04
- Primero instalar mininet:
        git clone https://github.com/mininet/mininet

- Luego, dentro de la carpeta mininet instalar pox:
        git clone https://github.com/noxrepo/pox

- Luego, ejecutar el comando:
        sudo apt install mininet

- Mover los siguientes archivos dentro de la carpeta mininet:
        topologia1.py
        topologia2.py

- Mover los siguientes archivos dentro de la carpeta pox/pox/forwarding
        controller1.py
        controller2.py
        antihorario.py
        firewall.py

Abrir dos consolas dentro de la carpeta mininet
- En la primera ejecutar: 
        python3 pox/pox.py --verbose openflow.spanning_tree --no-flood --hold-down openflow.discovery forwarding.<nombre_controlador>

- Dejarla abierta, y en la otra ejecutar: 
        sudo mn --custom <nombre_topologia>.py --topo MyTopo --mac --controller remote --switch ovsk

- Comando para matar un enlace:
        link s1 s2 down

Por ejemplo, para la parte 1, con el primer controlador, los comandos serían los siguientes:
    python3 pox/pox.py --verbose openflow.spanning_tree --no-flood --hold-down openflow.discovery forwarding.l2_learning

    python3 pox/pox.py --verbose openflow.spanning_tree --no-flood --hold-down openflow.discovery forwarding.<nombre_controlador>