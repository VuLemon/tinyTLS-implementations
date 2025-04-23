hex_dump = "16 03 01 00 92 01 00 00 8e 03 03 f1 c0 40 cf 93 18 f7 b3 e5 e0 aa d2 56 53 15 6b c1 16 5d aa e9 8c 37 6b 2f 71 b2 f9 47 52 29 8d 00 00 02 13 02 01 00 00 63 00 00 00 0e 00 0c 00 00 09 6c 6f 63 61 6c 68 6f 73 74"
byte_count = len(hex_dump.replace(" ", "")) // 2
print(f"Number of bytes: {byte_count}")
