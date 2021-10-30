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
         3. ping(ip_address)
         4. portScanner(ip_address, port)
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

     def ping(self, ip_addr):
        """
            ping(ip_address)
            ICMP pings an IP for the status of connectivity
            ip_address can be an IP address or URL
        """
        icmp = IP(dst=ip_addr) / ICMP()
        res = sr1(icmp, timeout=2, verbose=False)
        if str(type(res)) == "<class 'NoneType'>":
            print(
                f"{missing} system with ip `{ip_addr}` is either down or doesn't exist"
            )
            return False
        else:
            print(f"{result}: system with ip {res.src} is live")
            return True

    def portScanner(self, ip_addr, port):
        """
            portScanner(ip_address, port)
            Scans the ip_address for the status of the port passed
            ip_address can be an IP address or URL
            port must be an integer
        """
        try:
            res = self.scanner(ip_addr, port)
            if str(type(res)) == "<class 'NoneType'>":
                print(f"{missing} port {port} closed on {ip_addr}", end="")
                return False
            else:
                if res.sprintf("%TCP.flags%") == "SA":
                    print(f"{result}: port {res.sport} is open on {ip_addr} :", end="")
                    return True
                else:
                    print(f"{missing}: port {port} closed on {ip_addr} :", end="")
                    return False

        except socket.gaierror:
            print(f"{error} {ip_addr} Name or service not known")
            sys.exit()

    

if __name__ == "__main__":
    work = Networker()