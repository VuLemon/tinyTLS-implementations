hex_dump = "82 a5 8b 70 b7 a7 bc 6b 6e 81 e8 9e 2c 3f 3d 50 dc 24 9f 5d 12 a6 65 d8 00 7e 15 6a bc a8 07 0c 9d 96 16 60 4f 7a d2 04 26 4a 34 3f e1 8c d7 a3 16"
byte_count = len(hex_dump.replace(" ", "")) // 2
print(f"Number of bytes: {byte_count}")
