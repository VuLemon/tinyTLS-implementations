# Script to test ClientHello validity
# To test the ClientHello:
# 1. cd into debugging folder
# 2. Run an openSSL server using this command: openssl s_server -accept 4433 -cert server.crt -key server.key -tls1_3 -debug -msg -state -www
# 3. Passphrase is ArnoDurian2604
# 3. In a separate terminal, also cd into debugging folder and run this script: python openSSL_debug.py

import socket
import time
from urllib.parse import urlparse

# Parse the URL to get the hostname
parsed_url = urlparse('https://www.cloudflare.com/')
host = parsed_url.hostname  # This will extract 'www.brandeis.edu'
port = 443  # Standard HTTPS port

# Your existing client_hello remains the same
client_hello = bytes.fromhex(
    '16 03 01 00 9b 01 00 00 97 03 03 d6 b8 ec be 4e 54 ee 10 24 26 00 0f 44 b3 b3 d5 37 aa 64 b5 12 5b 6c 47 1e fb 10 56 f8 d9 64 96 00 00 02 13 02 01 00 00 6c 00 00 00 17 00 15 00 00 12 77 77 77 2e 63 6c 6f 75 64 66 6c 61 72 65 2e 63 6f 6d 00 0a 00 04 00 02 00 1d 00 0d 00 14 00 12 04 03 08 04 04 01 05 03 08 05 05 01 08 06 06 01 02 01 00 33 00 26 00 24 00 1d 00 20 df 3d 3e 88 58 60 b3 89 5a e4 70 47 87 e3 b2 b4 bb 59 dc b9 c1 00 b9 16 5d ac ae 0f a6 d5 86 2b 00 2b 00 03 02 03 04'
)

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        print(f"Attempting to connect to {host}:{port}")
        s.connect((host, port))  # Now passing a proper (host, port) tuple
        print("Connected to server.")
        
        bytes_sent = s.sendall(client_hello)
        print(f"Sent ClientHello ({len(client_hello)} bytes)")
        
        print("Waiting for server response...")
        try:
            while True:
                data = s.recv(4096)
                if not data:
                    print("Server closed connection without sending data.")
                    break
                print(f"Received {len(data)} bytes:")
                print(' '.join(f'{b:02x}' for b in data))
                
        except socket.timeout:
            print("Timeout while waiting for server response")
            
except ConnectionRefusedError:
    print("Connection refused. Is the OpenSSL server running?")
except socket.timeout:
    print("Connection attempt timed out")
except Exception as e:
    print(f"Error: {e}")