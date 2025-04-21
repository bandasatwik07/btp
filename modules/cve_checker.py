# modules/cve_checker.py

import subprocess
import json
import tempfile
import os

def check_components_for_cves(url):
    print("[*] Running Retire.js on URL...")
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
            output_file = tmp.name

        # Run Retire.js and store output
        result = subprocess.run(
            ['retire', '--url', url, '--outputformat', 'json', '--outputpath', output_file],
            capture_output=True,
            text=True
        )

        # Load JSON output
        with open(output_file, 'r') as f:
            data = json.load(f)

        os.remove(output_file)  # Clean up temp file

        findings = []

        for vulnerability in data.get("data", []):
            component = vulnerability.get("component", "Unknown")
            version = vulnerability.get("version", "Unknown")
            for vuln in vulnerability.get("vulnerabilities", []):
                findings.append({
                    "component": component,
                    "version": version,
                    "cve": vuln.get("identifiers", {}).get("CVE", []),
                    "info": vuln.get("info", [])
                })

        if not findings:
            return "No known vulnerable components found."
        return findings

    except Exception as e:
        return f"Error running Retire.js: {e}"
