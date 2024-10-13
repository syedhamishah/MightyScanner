from scapy.all import ARP, Ether, srp

class NetworkScanner:
    def __init__(self, target, ports):
        self.target = target
        self.ports = ports.split('-')

    def scan_network(self):
        print(f"Scanning network: {self.target}...")
        ip_range = self.target.split('/')[0]
        arp_request = ARP(pdst=self.target)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]
        
        devices = []
        for element in answered_list:
            device = {'ip': element[1].psrc, 'mac': element[1].hwsrc}
            devices.append(device)
        
        print(f"Found {len(devices)} devices.")
        return devices
