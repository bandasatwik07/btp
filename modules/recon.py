# modules/recon.py

import requests
import socket
import whois
from bs4 import BeautifulSoup

def perform_recon(url):
    recon_data = {}

    try:
        print("[+] Fetching WHOIS info...")
        domain = url.split("//")[-1].split("/")[0]
        whois_data = whois.whois(domain)
        recon_data['whois'] = {
            'domain_name': whois_data.domain_name,
            'registrar': whois_data.registrar,
            'creation_date': str(whois_data.creation_date),
            'emails': whois_data.emails
        }
    except Exception as e:
        recon_data['whois'] = f"Error fetching WHOIS: {e}"

    try:
        print("[+] Fetching HTTP headers...")
        headers = requests.get(url, timeout=10).headers
        recon_data['headers'] = dict(headers)
    except Exception as e:
        recon_data['headers'] = f"Error fetching headers: {e}"

    try:
        print("[+] Detecting Technologies...")
        tech_used = []
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        html = response.text.lower()

        # Basic keyword detection
        if 'wp-content' in html:
            tech_used.append('WordPress')
        if 'jquery' in html:
            tech_used.append('jQuery')
        if 'bootstrap' in html:
            tech_used.append('Bootstrap')
        if 'angular' in html:
            tech_used.append('Angular')
        if 'react' in html:
            tech_used.append('React')
        if 'vue' in html:
            tech_used.append('Vue.js')

        recon_data['technologies'] = list(set(tech_used))
    except Exception as e:
        recon_data['technologies'] = f"Error detecting technologies: {e}"

    return recon_data
