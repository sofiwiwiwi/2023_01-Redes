from mininet.topo import Topo
class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        sw = []
        for i in range(4):
            sw.append(self.addSwitch(f's{i+1}', dpid = f'{i+1}'))

        hsts = []
        for i in range(8):
            hsts.append(self.addHost(f'h{i+1}',mac = f'10:00:00:00:00:0{i+1}'))

        for i in range(4):
            self.addLink(sw[i], sw[i-1], 3, 4)
        self.addLink(sw[1], sw[3], 5, 6)#conexion extra

        for k in range(4):
            for i in range(2):
               self.addLink(hsts[i+(k*2)], sw[k], 100, i+1)

topos = {'MyTopo': (lambda: MyTopo())}
