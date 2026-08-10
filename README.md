# NetScope

A lightweight Python network diagnostic toolkit built to make common network troubleshooting tasks faster and easier.

NetScope combines several useful diagnostics into one command-line application, including connectivity testing, DNS resolution, port checking, latency measurement, and local network information.

## Features

- Connectivity testing
- DNS hostname resolution
- TCP port checking
- Latency measurement
- Local hostname and IP information
- Cross-platform ping support
- Error handling for failed connections and DNS lookups
- Simple command-line interface

## Technologies

- Python 3
- Python `socket` module
- `subprocess`
- `platform`
- `time`

## Getting Started

Clone the repository:

    git clone https://github.com/brice0087/netscope.git

Move into the project directory:

    cd netscope

Run NetScope:

    python netscope.py

## Example

    ================================================
                      NETSCOPE
              Network Diagnostic Toolkit
    ================================================

    [+] Local Network Information
    Hostname: workstation
    Local IP: 192.168.1.10

    [+] Testing connectivity to 8.8.8.8...
    [✓] Host is reachable.

    Enter a domain to diagnose (example.com): example.com

    [+] Resolving example.com...
    [✓] example.com -> 93.184.216.34

    [+] Checking example.com:80...
    [✓] Port 80 is reachable.

    [+] Checking example.com:443...
    [✓] Port 443 is reachable.

## Project Structure

    netscope/
    ├── netscope.py
    └── README.md

## What I Learned

Building NetScope helped me practice breaking network troubleshooting tasks into reusable Python functions, working with sockets, handling exceptions, processing user input, and designing clear command-line output.

The project also connects software engineering concepts with practical network troubleshooting.

## Roadmap

Future improvements may include:

- Command-line arguments
- Multiple-host diagnostics
- Additional DNS information
- Exportable diagnostic reports
- Improved latency statistics
- Automated tests
- Modular project structure

## License

This project is intended for educational and portfolio purposes.

## Example Output

A typical NetScope diagnostic session:

```text
$ python netscope.py

[+] Checking example.com:443...
[✓] Port 443 is reachable.

[+] Measuring latency to example.com...
[X] Unable to measure latency.

========================================
Diagnostic complete.
========================================

## How to Run

Clone the repository:

```bash
git clone https://github.com/brice0087/netscope.git
cd netscope

```

Run NetScope:

```bash
python netscope.py
```

## Project Structure

```text
netscope/
├── netscope.py
├── README.md
├── requirements.txt
└── .gitignore
```

## What I Learned

Building NetScope gave me hands-on experience with Python networking, DNS resolution, TCP connections, latency testing, exception handling, and command-line applications.

I also gained experience organizing a software project, documenting technical functionality, testing network operations, and handling situations where network requests fail without causing the application to crash.

## Future Improvements

- Add command-line arguments for custom hosts and ports
- Provide more detailed latency statistics
- Add network interface diagnostics
- Add configurable multi-port testing
- Generate diagnostic reports and logs
- Add automated unit tests