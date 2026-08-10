# NetScope

[![Run NetScope Tests](https://github.com/brice0087/netscope/actions/workflows/tests.yml/badge.svg)](https://github.com/brice0087/netscope/actions/workflows/tests.yml)

**A lightweight Python network diagnostic toolkit for connectivity testing, DNS resolution, TCP port checks, and latency analysis.**

NetScope combines common network troubleshooting tasks into a simple command-line application. The project was built to demonstrate practical Python development, networking fundamentals, automated testing, error handling, and continuous integration.

## Features

- Internet connectivity testing
- DNS hostname resolution
- TCP port availability checks
- TCP-based latency measurement
- Local hostname and IP information
- Cross-platform connectivity support
- Graceful error handling
- Interactive command-line interface
- Automated unit testing
- Continuous integration with GitHub Actions

## Technologies

- Python 3
- TCP/IP
- DNS
- Python Socket Programming
- Python `subprocess`
- Git
- GitHub
- GitHub Actions
- `unittest`
- Linux

## Getting Started

### Clone the repository

```bash
git clone https://github.com/brice0087/netscope.git
cd netscope
```

### Run NetScope

```bash
python netscope.py
```

When prompted, enter a domain:

```text
Enter a domain to diagnose (example.com): google.com
```

## Example Output

```text
================================================
                  NETSCOPE
          Network Diagnostic Toolkit
================================================

[+] Local Network Information
Hostname: workstation
Local IP: 192.168.1.10

[+] Testing connectivity to 8.8.8.8...
[✓] Host is reachable.

Enter a domain to diagnose (example.com): google.com

[+] Resolving google.com...
[✓] google.com -> 142.x.x.x

[+] Checking google.com:80...
[✓] Port 80 is reachable.

[+] Checking google.com:443...
[✓] Port 443 is reachable.

[+] Measuring latency to google.com...
[✓] Approximate latency: 11.27 ms

================================================
Diagnostic complete.
================================================
```

> Network results such as IP addresses and latency will vary depending on the system and connection.

## Testing

NetScope includes automated unit tests for core networking functionality.

Run the test suite with:

```bash
python -m unittest test_netscope.py
```

Example:

```text
....
----------------------------------------------------------------------
Ran 4 tests

OK
```

Tests are also automatically executed through **GitHub Actions** whenever changes are pushed to the `main` branch or submitted through a pull request.

## Project Structure

```text
netscope/
├── .github/
│   └── workflows/
│       └── tests.yml
├── .gitignore
├── netscope.py
├── test_netscope.py
├── requirements.txt
└── README.md
```

## How It Works

NetScope breaks common network diagnostics into reusable Python functions.

**Connectivity testing** checks whether an external host can be reached.

**DNS resolution** converts a domain name into its corresponding IP address.

**Port testing** attempts TCP connections to ports 80 and 443 to determine whether common HTTP and HTTPS services are reachable.

**Latency measurement** measures the approximate time required to establish a TCP connection with the target host.

Each diagnostic operation includes exception handling so that failed network requests do not cause the application to crash.

## What I Learned

Building NetScope gave me hands-on experience with:

- Python networking and socket programming
- DNS resolution
- TCP connections and ports
- Network troubleshooting
- Exception handling
- Modular Python functions
- Unit testing
- Git version control
- GitHub workflows
- Continuous integration with GitHub Actions
- Technical documentation
- Debugging applications across different environments

This project also helped me understand how software engineering practices such as testing, version control, documentation, and continuous integration can be applied to practical networking tools.

## Future Improvements

Planned improvements include:

- Command-line arguments for custom hosts and ports
- More detailed latency statistics
- Network interface diagnostics
- Configurable multi-port testing
- Diagnostic report generation
- Logging support
- Additional automated test coverage
- Desktop graphical interface
- Packaged executable version

## License

This project is available for educational and portfolio purposes.