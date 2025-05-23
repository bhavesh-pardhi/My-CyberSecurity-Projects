import socket

def find_subdomains(domain, wordlist_file):
    print(f"\n🔍 Scanning subdomains for: {domain}\n")

    try:
        with open(wordlist_file, 'r') as file:
            words = file.read().splitlines()

        found = []

        for word in words:
            subdomain = f"{word.strip()}.{domain}"
            try:
                ip = socket.gethostbyname(subdomain)
                print(f"[+] Found: {subdomain} -> {ip}")
                found.append(subdomain)
            except socket.gaierror:
                pass  # subdomain does not exist

        if not found:
            print("\n❌ No subdomains found.")
        else:
            print(f"\n✅ Total found: {len(found)}")
    except FileNotFoundError:
        print("🚫 Wordlist file not found!")

if __name__ == "__main__":
    target = input("Enter domain (e.g. example.com): ")
    wordlist = "subdomains.txt"  # You can replace with your custom wordlist path
    find_subdomains(target, wordlist)
