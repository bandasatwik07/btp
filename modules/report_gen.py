# modules/report_gen.py

import datetime

def generate_report(url, recon_data, sqlmap_result, xsstrike_result):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'report_{timestamp}.md'

    with open(filename, 'w') as report:
        report.write(f"# Vulnerability Assessment Report\n")
        report.write(f"**Target URL:** {url}\n")
        report.write(f"**Scan Date:** {timestamp}\n\n")

        report.write("## 1. Reconnaissance\n")
        report.write("### WHOIS Data:\n")
        report.write(f"```\n{recon_data.get('whois', 'N/A')}\n```\n")

        report.write("### HTTP Headers:\n")
        report.write(f"```\n{recon_data.get('headers', 'N/A')}\n```\n")

        report.write("### Detected Technologies:\n")
        report.write(f"```\n{recon_data.get('technologies', 'N/A')}\n```\n")

        report.write("## 2. SQLMap Findings\n")
        report.write(f"```\n{sqlmap_result}\n```\n")

        report.write("## 3. XSStrike Findings\n")
        report.write(f"```\n{xsstrike_result}\n```\n")

        # report.write("## 4. Client-Side Vulnerable Components (Retire.js)\n")
        # if isinstance(retire_findings, list):
        #     for item in retire_findings:
        #         report.write(f"- **Component**: {item['component']} v{item['version']}\n")
        #         report.write(f"  - CVEs: {', '.join(item['cve'])}\n")
        #         report.write(f"  - Info: {', '.join(item['info'])}\n")
        # else:
        #     report.write(f"```\n{retire_findings}\n```\n")

        # report.write("## 5. Server-Side Vulnerable Dependencies (Dependency-Check)\n")
        # if isinstance(dep_check_findings, list):
        #     for item in dep_check_findings:
        #         report.write(f"- **File**: {item['fileName']}\n")
        #         report.write(f"  - Vulnerability: {item['vulnName']} ({item['severity']})\n")
        #         report.write(f"  - CWE: {item['cwe']}\n")
        #         report.write(f"  - Description: {item['description'][:200]}...\n")
        # else:
        #     report.write(f"```\n{dep_check_findings}\n```\n")

    print(f"[+] Report saved as {filename}")
