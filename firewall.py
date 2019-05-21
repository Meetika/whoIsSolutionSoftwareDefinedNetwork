from pox.core import core
import pox.lib.packet as pkt
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.addresses import IPAddr

rules = [['10.0.0.1','10.0.0.3']]

class SDNFirewall (EventMixin):
    
    def __init__ (self):
        self.listenTo(core.openflow)
        
    def _handle_ConnectionUp (self, event):
        for rule in rules:
            block = of.ofp_match(dl_type = 0x800,nw_proto = pkt.ipv4.ICMP_PROTOCOL)
            block.nw_src = IPAddr(rule[0])
            block.nw_dst = IPAddr(rule[1])
            flow_mod = of.ofp_flow_mod()
            flow_mod.match = block
            event.connection.send(flow_mod)
        
def launch ():
    core.registerNew(SDNFirewall)