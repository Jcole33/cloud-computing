from mininet.topo import Topo

class BinaryTreeTopo( Topo ):
    "Binary Tree Topology Class."

    def __init__( self ):
        "Create the binary tree topology."

        # Initialize topology
        Topo.__init__( self )
    
        # Add hosts
        hosts = list()
        switches = list()
	#add hosts
        for i in range(1, 9):
            hosts.append(self.addHost('h' + str(i)))
	#add switches
        for i in range(1, 8):
            switches.append(self.addSwitch('s' + str(i)))
	#add links
        self.addLink(switches[2], hosts[0])
        self.addLink(switches[2], hosts[1])
        self.addLink(switches[3], hosts[2])
        self.addLink(switches[3], hosts[3])
        self.addLink(switches[5], hosts[4])
        self.addLink(switches[5], hosts[5])
        self.addLink(switches[6], hosts[6])
        self.addLink(switches[6], hosts[7])
        self.addLink(switches[1], switches[2])
        self.addLink(switches[1], switches[3])
        self.addLink(switches[4], switches[5])
        self.addLink(switches[4], switches[6])
        self.addLink(switches[0], switches[1])
        self.addLink(switches[0], switches[4])

topos = { 'binary_tree': ( lambda: BinaryTreeTopo() ) }
