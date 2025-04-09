# Read the file and extract data

def get_python_dependencies_WithVersion():
    requirements = {}
    with open("requirements.txt", "r") as file:
        for line in file:
            line = line.strip()  # Remove whitespace
            if not line or line.startswith("#"):
                continue  # Skip empty lines and comments
            
            # Split into library and version (handling inline comments)
            if "==" in line:
                lib, version = line.split("==", 1)  # Split on first "=="
                version = version.split("#")[0].strip()  # Remove comments after version
                requirements[lib.strip()] = version.strip()
    # Now the data is stored in the `requirements` variable
    return requirements


def get_python_dependencies_WithOutVersion():
    with open("requirements.txt", "r") as file:
        # dependencies = [line.strip().split("==")[0] for line in file if line.strip()]
        dependencies = [line.strip().split(">=")[0] for line in file if line.strip()]
        dependencies = [line.strip().split("==")[0] for line in dependencies if line.strip()]
        dependencies = [line.strip().split("<=")[0] for line in dependencies if line.strip()]
    return dependencies

# print(get_python_dependencies_WithVersion())
# print(get_python_dependencies_WithOutVersion())
