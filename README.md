# CyberSecurityProject

# CVE Vulnerability Checker for Project Libraries

## Overview

The **CVE Vulnerability Checker** is a Python script that scans a list of project dependencies and checks them against known vulnerabilities using the [National Vulnerability Database (NVD) API](https://nvd.nist.gov/). It helps developers and security engineers to identify vulnerable libraries and take action before issues impact production environments.

## Features

- **CVE Lookup:** Fetches real-time CVE data from NVD API.
- **Dependency Scanning:** Automatically scans a list of project libraries (e.g., Flask, Requests, Numpy) and identifies known vulnerabilities for the specific versions in use.
- **Detailed Reporting:** Outputs vulnerability information, including CVE ID, description, and affected versions.
- **Easy Integration:** Can be integrated into your CI/CD pipeline to automate vulnerability checking.

## Prerequisites

To run the CVE Vulnerability Checker, you'll need:

- Python 3.x
- Required libraries (listed in requirements.txt)

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/cve-vulnerability-checker.git
cd cve-vulnerability-checker
```

### Install Dependencies

You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

### Example Configuration

To use the script, define your project's dependencies and their versions inside the `project_libs` dictionary in the script:

```python
project_libs = {
    "requests": "2.26.0",
    "flask": "2.0.1",
    "numpy": "1.21.0",
    "sendmail": "5.58"  # Simulated vulnerable library
}
```

### Run the Script

To check for vulnerabilities, simply run the `cve_checker.py` script:

```bash
python cve_checker.py
```

The script will output the list of libraries affected by known CVEs, along with their descriptions and affected versions.

### Example Output

```bash
[!] requests 2.26.0 is affected by CVE-2023-0001
    CPE: cpe:2.3:a:requests:requests:2.26.0
    Description: Fake RCE in requests library

[!] flask 2.0.1 is affected by CVE-2023-0002
    CPE: cpe:2.3:a:palletsprojects:flask:2.0.1
    Description: Fake DoS in flask

[!] sendmail 5.58 is affected by CVE-2023-0003
    CPE: cpe:2.3:a:sendmail:sendmail:5.58
    Description: Fake buffer overflow in sendmail
```

## Contributing

If you’d like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request with your changes. Please ensure that any new features or bug fixes are well-documented and have corresponding tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [NVD API](https://nvd.nist.gov/) for providing CVE data
- [Requests Library](https://requests.readthedocs.io/en/master/) for making HTTP requests

---

Feel free to replace the placeholders (e.g., `yourusername`) and tweak the sections as necessary. Let me know if you'd like further customization!
