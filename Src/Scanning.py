import requests
import Scanner_Python 

# Load CVE JSON data (from API)
NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
try:
    response = requests.get(NVD_API_URL)
    response.raise_for_status()
    cve_data = response.json()
except requests.RequestException as e:
    print(f"Error fetching data: {e}")
    cve_data = None

# Extract CVE vulnerabilities list
vulnerabilities = cve_data.get("vulnerabilities", [])

# List of project libraries (names only, without versions)
project_libs = Scanner_Python.get_python_dependencies_WithOutVersion()
# project_libs = ['requests', 'flask', 'numpy', 'sendmail']

# Normalize product names for matching
def normalize_name(name):
    return name.lower().replace("_", "-")

# Check if any vulnerability affects a listed library
results = []
for vuln in vulnerabilities:
    cve = vuln.get("cve", {})
    cve_id = cve.get("id", "")
    description = next((desc['value'] for desc in cve.get("descriptions", []) if desc['lang'] == 'en'), "")

    for config in cve.get("configurations", []):
        for node in config.get("nodes", []):
            for match in node.get("cpeMatch", []):
                if match.get("vulnerable"):
                    cpe = match.get("criteria", "")
                    for lib in project_libs:
                        # Check if the library name is in the CPE, and extract version if available
                        if normalize_name(lib) in cpe:
                            # Extract version from CPE string (if present)
                            version = None
                            if match.get("versionEndExcluding"):
                                version = match.get("versionEndExcluding")
                            elif match.get("versionStartExcluding"):
                                version = match.get("versionStartExcluding")

                            results.append({
                                "library": lib,
                                "cve_id": cve_id,
                                "description": description,
                                "cpe": cpe,
                                "version": version if version else "Unknown"
                            })

# Print results with library and version information
for r in results:
    print(f"[!] {r['library']} (Version: {r['version']}) is affected by {r['cve_id']}")
    print(f"    CPE: {r['cpe']}")
    print(f"    Description: {r['description']}\n")

if not results:
    print("No known vulnerabilities found for the listed libraries.")
