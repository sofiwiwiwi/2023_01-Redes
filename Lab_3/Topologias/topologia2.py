from mininet.topo import Topo
class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        sw = []
        for i in range(4):
            sw.append(self.addSwitch(f's{i+1}', dpid = f'{i+1}'))

        hsts = []
        for i in range(5):
            hsts.append(self.addHost(f'h{i+1}',mac = f'10:00:00:00:00:0{i+1}'))

        for i in range(3):
            self.addLink(sw[i], sw[i-1], 3, 4)
        self.addLink(sw[2], sw[3], 3, 4)#conexion bidireccional

        for k in range(5):
            if k == 3:
                self.addLink(hsts[k-1], sw[k-1], 100, 2)
            elif  k == 4:
            	self.addLink(hsts[k-1], sw[k-1], 100, 1)
            else:   	
                self.addLink(hsts[k-1], sw[k], 100, 1)


topos = {'MyTopo': (lambda: MyTopo())}




# PARA HACER EL SERVIDOR HTTP en mininet: <nombre host> python -m SimpleHTTPServer 80 & (creara un servidor http simple en el puerto 80)
# PARA HACER UN wget al servidor HTTP en mininet: <host origen> wget -O - <Nombre del host que es servidor HTTP>