# Script to test ClientHello validity
# To test the ClientHello:
# 1. cd into debugging folder
# 2. Run an openSSL server using this command: openssl s_server -accept 4433 -cert server.crt -key server.key -tls1_3 -debug -msg -state -www
# 3. Passphrase is ArnoDurian2604
# 3. In a separate terminal, also cd into debugging folder and run this script: python openSSL_debug.py

import socket
import time

# Host an openSSL server in localhost
host = '127.0.0.1'
port = 4433

# Run the tinyTLS inplementation, paste the clientHello here to test
client_hello = bytes.fromhex(
    '16 03 01 00 92 01 00 00 8e 03 03 e9 0d ca 92 54 25 a4 38 c6 03 96 70 6d f4 2f 31 40 17 81 09 bf 9f d1 9b a8 3e a2 cd 4f 56 e6 df 00 00 02 13 01 01 00 00 63 00 00 00 0e 00 0c 00 00 09 6c 6f 63 61 6c 68 6f 73 74 00 0a 00 04 00 02 00 1d 00 0d 00 14 00 12 04 03 08 04 04 01 05 03 08 05 05 01 08 06 06 01 02 01 00 33 00 26 00 24 00 1d 00 20 38 72 2b 87 8c 43 73 4c ed 9c 47 21 82 d4 fe 62 ec 74 ad f8 5a 97 ae 34 07 ce 53 2e 1f 41 51 01 00 2b 00 03 02 03 04'


)

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        print(f"Attempting to connect to {host}:{port}")
        s.connect((host, port))
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