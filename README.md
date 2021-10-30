# NetScanner
Network Scanner written in Python. #Hacktoberfest 21 submissions allowed

______________________________________________________________________________



        Netscanner class with modules for various networking jobs
         1. scanner(ip_address, port)
         2. networkScanner(gateway_ip)
         3. ping(ip_address)
         4. portScanner(ip_address, port)
         5. commonPortsScanner(ip_address)
         6. allPortsScanner(ip_address)
         7. webscan(URL)


            ## scanner(ip_address, port)
            Simply Scans whatever is passed and returns a TCP scan reply
            ip_address can be an IP address or URL
            port must be an integer

            ## networkScanner(gateway_ip)
            Scans for all the systems on a network for a particular gateway
            gateway_ip can be the actual gateway IP or any node on the gateway's network

            ## ping(ip_address)
            ICMP pings an IP for the status of connectivity
            ip_address can be an IP address or URL

            ## portScanner(ip_address, port)
            Scans the ip_address for the status of the port passed
            ip_address can be an IP address or URL
            port must be an integer

            ## allPortsScanner(ip_address)
            Scans the ip_address for the status of all possible ports
            ip_address can be an IP address or URL

            ## commonPortsScanner(ip_address)
            Scans the ip_address for the status of few common ports
            ip_address can be an IP address or URL
   
            ## webscan(URL)
            Scans the URL for the status of common web hosting/service ports [80(http), 443(https), 8080(dev)]
            ip_address can be an IP address or URL
            port must be an integer
        