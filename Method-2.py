import socket

import requests


def verify_domain(url):
   try:
       response = requests.get(url)
       if response.status_code == 200:
           return True
       else:
           return False
   except:
       return False

print(verify_domain("https://www.google.com"))

def verify_domain_with_socket(hostname):
   try:
       ip_address = socket.gethostbyname(hostname)
       socket.create_connection((ip_address, 80))
       return True
   except:
       return False

verify_domain_with_socket(8.8)

def test_domain():
   print("response of domain verification is:  ",verify_domain_with_socket("google.net"))

# print(test_domain())
