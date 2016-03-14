import argparse
import os

print "-"*140
print "-"*140

parser = argparse.ArgumentParser(description='Information Gathering software')
parser.add_argument('-u', '-url', type=str, help='Target URL')
args = parser.parse_args()

if not args.u:
    print "ERROR : Input url"
    exit(0)

print os.system("dig +short "+args.u);
