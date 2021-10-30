#!/usr/bin/env python3
from scapy.all import *
import sys
from colorama import init, Fore, Back, Style


# Colorama globals settings
init()
missing = Style.RESET_ALL + Fore.RED + Style.DIM
error = Style.RESET_ALL + Back.RED + Fore.BLACK
result = Style.RESET_ALL + Back.GREEN + Fore.BLACK
info = Style.RESET_ALL + Fore.CYAN


class Networker:
    """
        Networker class with modules for various networking jobs
         1. scanner(ip_address, port)
         2. networkScanner(gateway_ip)
    """

    def __init__(self):
        pass

    def scanner(self, ip_addr, port):
        """
            scanner(ip_address, port)
            Simply Scans whatever is passed and returns a TCP scan reply
            ip_address can be an IP address or URL
            port must be an integer
        """
        tcp = IP(dst=ip_addr) / TCP(dport=port)
        res = sr1(tcp, timeout=5, verbose=False)
        return res

    def networkScanner(self, gateway_ip):
        """
            networkScanner(gateway_ip)
            Scans for all the systems on a network for a particular gateway
            gateway_ip can be the actual gateway IP or any node on the gateway's network
        """
        if self.ping(gateway_ip):
            ip_seg = gateway_ip.split(".")
            ip_seq = ".".join(ip_seg[0:3])
            for machine_id in range(1, 256):
                self.ping(f"{ip_seq}.{machine_id}")

    


if __name__ == "__main__":
    work = Networker()