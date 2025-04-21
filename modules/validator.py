# modules/validator.py

from urllib.parse import urlparse

def is_government_domain(url):
    try:
        domain = urlparse(url).netloc.lower()

        # List of valid government domain patterns
        gov_domains = ['.gov.in', '.nic.in', '.mp.gov.in']

        return any(domain.endswith(gov) for gov in gov_domains)

    except Exception as e:
        print(f"[!] Error while validating domain: {e}")
        return False
