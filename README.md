# CyberSecurityProject

# CVE Vulnerability Checker for Project Libraries

## Overview

The **CVE Vulnerability Checker** is a Python script that scans a list of project dependencies and checks them against known vulnerabilities using the [National Vulnerability Database (NVD) API](https://nvd.nist.gov/). It helps developers and security engineers to identify vulnerable libraries and take action before issues impact production environments.

## Features

- **CVE Lookup:** Fetches real-time CVE data from NVD API.
- **Dependency Scanning:** Automatically scans a list of project libraries and identifies known vulnerabilities for the specific versions in use.
- **Detailed Reporting:** Outputs vulnerability information, including CVE ID, description, and affected versions.
- **Easy Integration:** Can be integrated into your CI/CD pipeline to automate vulnerability checking.


## 📦 Installation & Usage

### 🔽 Download or Clone the Project

You can get the project in one of the following ways:

#### Option 1: Clone via Git

```bash
git clone https://github.com/mastafakamel/CyberSecurityProject.git
cd CyberSecurityProject
```

#### Option 2: Download as ZIP

1. Go to the [GitHub repository](https://github.com/mastafakamel/CyberSecurityProject.git)
2. Click the green **Code** button
3. Select **Download ZIP**
4. Extract the ZIP file and navigate into the project folder

---

## Usage

### Example Configuration

To use the script, define your project's dependencies your project **[requirements.txt can]** and copy it next to  Folder Src

![2025-04-09 211059](https://github.com/user-attachments/assets/b6e9eb24-bb08-4556-a090-a8c418897487)


### Run the Script

To check for vulnerabilities, simply run the `Scanning.py` script:

```bash
cd Src
python Scanning.py
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

---

## Acknowledgments

- [NVD API](https://nvd.nist.gov/) for providing CVE data
