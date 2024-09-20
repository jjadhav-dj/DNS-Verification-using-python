import requests
import whois

def check_domain(domain):
    try:
    # Attempt to retrieve information about the given domain using the     'whois' library.
        domain_info = whois.whois(domain)

    # Check if the domain status is 'ok' (verified).
        if domain_info.status == 'ok':
            print(f"{domain} is a verified domain.")
        else:
            print(f"{domain} is not a verified domain.")

    except whois.parser.PywhoisError:
        print(f"Error checking {domain}.")


check_domain("google.com")


