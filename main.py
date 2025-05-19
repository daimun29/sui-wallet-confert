from bech32 import bech32_encode, convertbits

def hex_to_suiprivkey(hex_key):
    try:
        key_bytes = bytes.fromhex(hex_key.strip())
        if len(key_bytes) != 32:
            raise ValueError("Key is not 32 bytes")
        key_with_prefix = b'\x00' + key_bytes  # 0x00 = Ed25519 prefix
        data = convertbits(key_with_prefix, 8, 5, True)
        return bech32_encode("suiprivkey", data)
    except Exception as e:
        return f"Invalid key ({hex_key}): {e}"

def main():
    with open("wallet.txt", "r") as infile, open("hasil.txt", "w") as outfile:
        for line in infile:
            result = hex_to_suiprivkey(line)
            outfile.write(result + "\n")

if __name__ == "__main__":
    main()
