from typing import List

import nslookup

__all__ = ['resolve_domain']


def resolve_domain(domain: str) -> List[str]:
    """
    Get IP addresses by domain name using nslookup library
    :param domain: domain name without http/s
    :return: list of IP addresses
    """
    ips_record: nslookup.DNSresponse = nslookup.Nslookup(verbose=False, tcp=False).dns_lookup(domain)
    return ips_record.answer
