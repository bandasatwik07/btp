# main.py
from modules.validator import is_government_domain
from modules.recon import perform_recon
from modules.sqlmap_runner import run_sqlmap
from modules.xsstrike_runner import run_xsstrike
from modules.cve_checker import check_components_for_cves
from modules.report_gen import generate_report

def main():
    target_url = input("Enter target URL: ").strip()

    if not is_government_domain(target_url):
        print("[!] Not a government domain. Aborting.")
        return

    print("[*] Starting Recon...")
    recon_data = perform_recon(target_url)

    print("[*] Running SQLMap...")
    sqlmap_result = run_sqlmap(target_url)

    print("[*] Running XSStrike...")
    xsstrike_result = run_xsstrike(target_url)

    # print("[*] Checking for vulnerable components...")
    # cve_result = check_components_for_cves(target_url)

    print("[*] Generating report...")
    generate_report(target_url, recon_data, sqlmap_result, xsstrike_result)
    # generate_report(target_url, recon_data, sqlmap_result, xsstrike_result, cve_result)

    # print("[+] Done! Report saved.")

if __name__ == "__main__":
    main()
