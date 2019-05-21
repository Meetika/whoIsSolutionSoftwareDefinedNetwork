from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):

        Topo.__init__( self )

        H3 = self.addHost('h3', ip='10.0.0.3' )
        H4 = self.addHost('h4', ip='10.0.0.4' )
		
		S2 = self.addSwitch( 's2' )

        self.addLink( H3, S2 )
        self.addLink( H4, S2 )

topos = { 'mytopo': ( lambda: MyTopo() ) }