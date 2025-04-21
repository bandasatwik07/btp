# modules/sqlmap_runner.py

import subprocess

def run_sqlmap(url):
    print("[*] Running SQLMap scan...")
    try:
        result = subprocess.run(
            ['python3', 'sqlmap/sqlmap.py', '-u', url, '--batch', '--level=1', '--risk=1', '--crawl=1', '--output-dir=output'],
            capture_output=True, text=True, timeout=120
        )
        output = result.stdout
        # Optionally you can parse output or just return it
        return output if output else "No output from SQLMap."
    except subprocess.TimeoutExpired:
        return "SQLMap scan timed out."
    except Exception as e:
        return f"Error running SQLMap: {e}"
