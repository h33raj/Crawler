import argparse
import os

__author__ = 'Heeraj'

class Info():
    """
    Information Gathering
    """
    def __init__(self):
        i=0
        #Future

    def info_collect(self):   
        print "IP Info : "
        print os.system("dig +short "+args.u)

def main():
    info = Info()
    info.info_collect()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Information Gathering software')
    parser.add_argument('-u', '-url', type=str, help='Target URL')
    args = parser.parse_args()
    if not args.u:
        print "ERROR : Input url"
        exit(0)
   
main()
