# modules/xsstrike_runner.py

import subprocess

def run_xsstrike(url):
    print("[*] Running XSStrike scan...")
    try:
        result = subprocess.run(
            ['python3', 'XSStrike/xsstrike.py', '-u', url, '--crawl'],
            capture_output=True, text=True, timeout=120
        )
        output = result.stdout
        return output if output else "No output from XSStrike."
    except subprocess.TimeoutExpired:
        return "XSStrike scan timed out."
    except Exception as e:
        return f"Error running XSStrike: {e}"
