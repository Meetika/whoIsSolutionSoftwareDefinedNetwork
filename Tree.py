from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):

        Topo.__init__( self )

        H1 = self.addHost('h1', ip='10.0.0.1')
        H2 = self.addHost('h2', ip='10.0.0.2')
		
		S1 = self.addSwitch( 's1' )

        self.addLink( H1, S1 )
        self.addLink( H2, S1 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
