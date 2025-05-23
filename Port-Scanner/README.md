
# 🔍 Python Port Scanner

A simple, beginner-friendly **TCP Port Scanner** written in Python.  
This tool allows you to scan either the **top 1000 common ports** or **all 65535 ports** on a given IP address or domain. It uses raw socket connections and prints colorful, real-time results.

---

## 🎯 Features

- ✅ Scan top 1000 ports or full 65535 ports
- 🌐 Accepts both IP address and domain name
- 🌈 Colorful output using `colorama`
- ⚠️ Clean exit on Ctrl+C
- 📚 Beginner-friendly and easy to understand
- 🐍 Built with basic Python (no heavy libraries)

---

## 🛠️ Installation

```bash
git clone https://github.com/bhavesh-pardhi/My-CyberSecurity-Projects.git
cd My-CyberSecurity-Projects
cd Port Scanner
pip install colorama
````

> Make sure you are using Python 3.

---

## 🚀 Usage

```bash
python3 scanner.py [flag] [target]
```

### 🔹 Flags

| Flag | Description                   |
| ---- | ----------------------------- |
| `-t` | Scan top 1000 ports (faster)  |
| `-a` | Scan all 65535 ports (slower) |

### 🔹 Examples

```bash
# Scan top 1000 ports of localhost
python3 scanner.py -t 127.0.0.1

# Scan all ports of a domain
python3 scanner.py -a google.com
```

---

## 📸 Screenshot

![Scanner Output](https://github.com/bhavesh-pardhi/port-scanner/blob/main/port-scanner.png)

---

## 💡 How It Works (In Simple Words)

* The script tries to connect to each port one by one using Python's socket.
* If a connection is successful, that means the port is **open**.
* If it fails or times out, it is **closed** or **filtered**.
* It uses `argparse` to let you choose between scanning 1000 or 65535 ports.

---

## 👨‍💻 For Beginners

This project is **perfect for learning**:

* Python scripting
* Socket programming
* CLI tool development
* Cybersecurity fundamentals

Feel free to explore and modify the code!

---

# 🧾 Code Breakdown & Explanation

---

## 🔍 OVERALL PURPOSE

This script is a **TCP Port Scanner** that:

* Takes a target IP/domain (like `127.0.0.1` or `google.com`)
* Scans either:

  * Top 1000 ports (`-t` flag)
  * All 65535 ports (`-a` flag)
* Tells you which ports are open (i.e., accessible)
* Uses **colorful output**, and you can **stop it anytime with Ctrl+C**

---

## 📜 LINE-BY-LINE EXPLANATION

---

### 🔸 IMPORTING MODULES

```python
import socket
import argparse
from colorama import init, Fore
from datetime import datetime
```

* `socket`: For creating network connections to each port.
* `argparse`: For accepting command-line inputs like `-t`, `-a`, and the IP/domain.
* `colorama`: To add **color to terminal output** (like red for errors, green for open ports).
* `datetime`: Just to print when the scan started.

---

### 🔸 INITIALIZE COLORAMA

```python
init(autoreset=True)
```

* This sets up `colorama` so that colors reset automatically after each print.
* You do not have to manually reset the color every time.

---

### 🔸 MAIN SCANNING FUNCTION

```python
def scan_ports(target, ports):
    print(Fore.YELLOW + f"\n[~] Starting scan on {target}")
    print(Fore.YELLOW + f"[~] Time started: {datetime.now()}\n")
```

* This function will scan each port on the target.
* It prints the target and the current time before starting.

---

### 🔁 LOOP THROUGH PORTS

```python
    try:
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(Fore.GREEN + f"[+] Port {port} is open")
            s.close()
```

* `for port in ports`: Scans one port at a time.
* `socket.socket(...)`: Creates a TCP socket.
* `s.settimeout(0.5)`: Sets a 0.5-second timeout (so it does not hang).
* `s.connect_ex((target, port))`: Tries to connect to the port.

  * Returns `0` if successful → means **port is open**
* If open, it prints in green.
* Then the socket is closed for the next attempt.

---

### 🔐 HANDLE ERRORS AND EXIT

```python
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Scan interrupted by user. Exiting...")
        exit()
    except socket.gaierror:
        print(Fore.RED + "[!] Hostname could not be resolved.")
        exit()
    except socket.error:
        print(Fore.RED + "[!] Could not connect to server.")
        exit()
```

* If you press `Ctrl+C` → exits cleanly.
* If the domain is wrong → gives an error.
* If server is unreachable → shows message and exits.

---

### 🎯 ARGUMENT HANDLING

```python
def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--top", action="store_true", help="Scan top 1000 ports")
    group.add_argument("-a", "--all", action="store_true", help="Scan all 65535 ports")
    parser.add_argument("target", help="Target IP or domain")
```

* This handles what you type in the terminal.
* You must use either:

  * `-t` for top 1000 ports
  * `-a` for all 65535 ports
* You also give a `target` (IP/domain)

---

### 💻 CONVERT DOMAIN TO IP

```python
    args = parser.parse_args()
    target = socket.gethostbyname(args.target)
```

* Parses what you entered in command line.
* `socket.gethostbyname()` converts domain to IP (e.g., `google.com` → `142.250.190.14`)

---

### 🎯 SELECT WHICH PORTS TO SCAN

```python
    if args.top:
        ports = range(1, 1001)
    elif args.all:
        ports = range(1, 65536)
```

* `-t` → scan port 1 to 1000
* `-a` → scan port 1 to 65535

---

### 🔁 RUN SCAN FUNCTION + FINAL ERROR HANDLING

```python
    try:
        scan_ports(target, ports)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] User aborted. Bye! 💔")
        exit()
```

* Calls the `scan_ports()` function with the target and port range.
* Catches `Ctrl+C` again in case something goes wrong outside the function.

---

### 🚀 SCRIPT ENTRY POINT

```python
if __name__ == "__main__":
    main()
```

* This line means: Run the `main()` function when you execute `python3 scanner.py`
* It is standard in all Python scripts

---

## 🧠 SUMMARY

| Thing            | Meaning                                      |
| ---------------- | -------------------------------------------- |
| `-t`             | Scan only top 1000 ports                     |
| `-a`             | Scan all ports                               |
| `s.connect_ex()` | Try to connect to a port                     |
| Result `0`       | Port is open                                 |
| Colorama         | Makes the output colorful and easy to read   |
| Ctrl+C           | You can now safely stop the scan any time! ✅ |

---

## 💡 You Learned:

* How TCP port scanning works
* Basics of `socket` in Python
* How to use `argparse` for CLI tools
* How to add colors and handle errors
* How to create a real cybersecurity tool for GitHub

---


## 📬 Contribute

If you have any suggestions, feel free to open issues or pull requests.
Want to make it multi-threaded or export results to a file? Go ahead!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ❤️ Credits

Created with love by Bhavesh Pardhi
Follow for more Python + Hacking projects.
