"""
======================= NW DIAGNOSTIC UTILITY ==================================
https://github.com/denisecase/nw-diagnostics-python/
================================================================================

PURPOSE:
Generate diagnostic information about the Python virtual environment. 

ORIGIN:
This is an instructor-generated script. You do not need to edit or understand 
  the code in this file. 

USAGE:
In the terminal, run the following command:  

python 00_check_env.py

OUTPUT:
See the new file named `00_check_env.txt` in your local repository.

REQUIREMENTS:
An active internet connection is required to fetch the diagnostic utility from 
  the GitHub repository.

CAUTION:
This script fetches and executes Python code from a remote source using 
  the `exec` function. While efforts have been made to ensure the security and 
  integrity of the hosted code, always be cautious and aware of the potential 
  risks associated with executing remote code. Ensure that the URL 
  (https://github.com/denisecase/nw-diagnostics-python/) is trusted before running the script.

================================================================================
"""

# Python Standard Library
import os
import urllib.request


# List of web addresses (URLs) for remote code files
URLS = [
    "https://raw.githubusercontent.com/denisecase/nw-diagnostics-python/basic/00_check_core.py",
    "https://raw.githubusercontent.com/denisecase/nw-diagnostics-python/basic/00_check_env.py",
]

# List of output files generated by the remote code
report_files = [
    "00_check_core.txt",
    "00_check_env.txt",
]


def delete_report_files():
    """
    Delete the report files from the current directory.
    """
    for file in report_files:
        try:
            os.remove(file)
        except FileNotFoundError:
            pass


def fetch_code(url):
    """
    Fetches the code from the URL but doesn't execute it.

    Args:
    - url (str): The URL to fetch the Python code from.

    Returns:
    - str: The fetched code as a string.
    """
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        print(f"ERROR: Failed to fetch code from {url}. Reason: {e}")
        return None


def execute_diagnostic(url, function_name):
    """
    Fetches, executes, and runs the diagnostic function from the given URL.

    Args:
    - url (str): The URL to fetch the Python code from.
    - function_name (str): The name of the diagnostic function to call.

    Returns:
    - bool: True if successful, False otherwise.
    """
    code = fetch_code(url)
    if code is None:
        return False

    namespace = {}
    exec(code, {}, namespace)
    run_diagnostic = namespace.get(function_name)

    if callable(run_diagnostic):
        run_diagnostic()
        return True
    else:
        print(f"ERROR: Failed to find {function_name} in {url}.")
        return False


# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    delete_report_files()

    if not execute_diagnostic(URLS[0], "run_diagnostic_core"):
        exit(1)

    if not execute_diagnostic(URLS[1], "run_diagnostic_env"):
        exit(1)