# NetScope

[![Run NetScope Tests](https://github.com/brice0087/netscope/actions/workflows/tests.yml/badge.svg)](https://github.com/brice0087/netscope/actions/workflows/tests.yml)

**A lightweight Python network diagnostic toolkit for connectivity testing, DNS resolution, TCP port checks, and latency analysis.**

NetScope combines common network troubleshooting tasks into a simple command-line application. The project demonstrates practical Python development, networking fundamentals, automated testing, error handling, version control, and continuous integration.

## Features

- Internet connectivity testing
- DNS hostname resolution
- TCP port availability checks
- TCP-based latency measurement
- Local hostname and IP information
- Cross-platform connectivity testing
- Graceful network error handling
- Interactive command-line interface
- Automated unit testing
- Continuous integration with GitHub Actions

## Technologies

- Python 3
- TCP/IP
- DNS
- Socket Programming
- Python `subprocess`
- Git
- GitHub
- GitHub Actions
- Python `unittest`
- Linux

## Getting Started

### Clone the Repository

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

> Network results such as IP addresses and latency will vary depending on the system, location, and connection.

## Testing

NetScope includes automated unit tests covering core networking functionality.

Run the test suite with:

```bash
python -m unittest test_netscope.py
```

Example successful test run:

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

## How NetScope Works

NetScope separates common network diagnostics into reusable Python functions.

### Connectivity Testing

NetScope checks whether an external host is reachable and handles failed connectivity attempts without crashing the application.

### DNS Resolution

The DNS lookup function resolves a domain name to its corresponding IP address using Python's networking capabilities.

### TCP Port Testing

NetScope attempts TCP connections to ports **80** and **443** to determine whether common HTTP and HTTPS services are reachable.

### Latency Measurement

NetScope measures approximate latency by timing the establishment of a TCP connection to the target host.

### Error Handling

Network operations can fail for many reasons. NetScope uses exception handling so failed DNS lookups, unreachable ports, timeouts, and connection errors can be reported without terminating the entire application.

## Software Engineering Practices

This project incorporates several software engineering practices beyond the core networking functionality:

- Modular Python functions
- Automated unit testing
- Git version control
- GitHub repository management
- Continuous integration
- GitHub Actions workflows
- Error and exception handling
- Technical documentation
- Incremental development and debugging

## What I Learned

Building NetScope gave me hands-on experience working with Python networking, DNS resolution, TCP connections, port testing, latency measurement, exception handling, and command-line applications.

I also gained practical experience writing automated tests, debugging network behavior across different environments, using Git for version control, and configuring GitHub Actions to automatically validate code after changes are pushed.

The project reinforced how testing, documentation, version control, debugging, and continuous integration work together in a software development workflow.

## Future Improvements

Planned improvements include:

- Command-line arguments for custom hosts and ports
- More detailed latency statistics
- Network interface diagnostics
- Configurable multi-port testing
- Diagnostic report generation
- Logging support
- Expanded automated test coverage
- Desktop graphical interface
- Packaged executable version

## License

This project is intended for educational and portfolio purposes.