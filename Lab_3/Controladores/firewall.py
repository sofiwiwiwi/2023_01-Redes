from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.addresses import EthAddr


rules = [['00:00:00:00:00:01','00:00:00:00:00:04'],#primer punto
        ['00:00:00:00:00:03','00:00:00:00:00:04'],
        ['00:00:00:00:00:05','00:00:00:00:00:04'],
        ['00:00:00:00:00:05','00:00:00:00:00:02'],
        ['00:00:00:00:00:03','00:00:00:00:00:02'],
        ['00:00:00:00:00:01','00:00:00:00:00:03'],##segundo punto
        ['00:00:00:00:00:02','00:00:00:00:00:03'],
        ['00:00:00:00:00:04','00:00:00:00:00:03'],
        ['00:00:00:00:00:04','00:00:00:00:00:05'],
        ['00:00:00:00:00:03','00:00:00:00:00:01'],#tercer punto
        ['00:00:00:00:00:04','00:00:00:00:00:01'],
        ]

class SDNFirewall (EventMixin):
    
    def __init__ (self):
        self.listenTo(core.openflow)
        
    def _handle_ConnectionUp (self, event):
        for rule in rules:
            block = of.ofp_match()
            block.dl_src = EthAddr(rule[0])
            block.dl_dst = EthAddr(rule[1])
            flow_mod = of.ofp_flow_mod()
            flow_mod.match = block
            event.connection.send(flow_mod)
        
def launch ():
    core.registerNew(SDNFirewall)

#python3 pox.py log.level --DEBUG misc.full_payload forwarding.<controlador> misc.firewall openflow.discovery openflow.spanning_tree --no-flood --hold-down