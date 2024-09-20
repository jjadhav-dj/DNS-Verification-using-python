import dns.resolver

def verify_dns(domain, record_type, expected_value):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        for rdata in answers:
            if rdata.to_text() == expected_value:
                return True
    except dns.resolver.NXDOMAIN:
        pass
    return False
verify_dns('google.com','TXT',"v=spf1 include:_spf.google.com ~all")
