# hash_identifier.py

def identify_hash(hash_string):
    hash_types = {
        32: ["MD5", "NTLM"],
        40: ["SHA-1"],
        56: ["SHA-224"],
        64: ["SHA-256", "SHA3-256"],
        96: ["SHA-384"],
        128: ["SHA-512", "SHA3-512"],
        16: ["MySQL (Old)"],
        20: ["CRC-160"],
        8: ["CRC-32", "DES (Salted)"],
        13: ["Unix DES"],
        34: ["MD5 (Unix)"],
        60: ["bcrypt"],
        86: ["SHA512 (Unix)"],
        98: ["SHA256 (Unix)"]
    }

    possible_hashes = []

    length = len(hash_string)

    # Check for bcrypt prefix
    if hash_string.startswith("$2a$") or hash_string.startswith("$2b$"):
        possible_hashes.append("bcrypt")

    # Match by length
    if length in hash_types:
        possible_hashes.extend(hash_types[length])

    return list(set(possible_hashes))


if __name__ == "__main__":
    print("🔍 Hash Identifier Tool")
    print("------------------------")
    hash_input = input("Enter the hash: ").strip()

    detected = identify_hash(hash_input)

    if detected:
        print("\n[+] Detected Hash Type(s):")
        for algo in detected:
            print(f" - {algo}")
    else:
        print("\n[!] Could not identify the hash type.")
